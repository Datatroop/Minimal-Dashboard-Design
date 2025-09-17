import reflex as rx
import httpx
import os
import logging
from typing import TypedDict


class Record(TypedDict):
    _record_id: str
    _latitude: float
    _longitude: float
    _status: str


class DashboardState(rx.State):
    sidebar_collapsed: bool = False
    records: list[Record] = []
    error_message: str = ""
    is_loading: bool = False
    fulcrum_key: str = os.getenv("fulcrum_key", "YOUR_FALLBACK_KEY")

    @rx.var
    def total_records(self) -> int:
        return len(self.records)

    @rx.var
    def new_records(self) -> int:
        return sum((1 for r in self.records if r.get("_status") == "New"))

    @rx.var
    def in_progress_records(self) -> int:
        return sum((1 for r in self.records if r.get("_status") == "In Progress"))

    @rx.var
    def completed_records(self) -> int:
        return sum((1 for r in self.records if r.get("_status") == "Completed"))

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed

    @rx.event(background=True)
    async def fetch_data(self):
        if self.records:
            return
        async with self:
            self.is_loading = True
            self.error_message = ""
        try:
            database_name = "Vector Job DB"
            query = f'SELECT _record_id, _latitude, _longitude, _status FROM "{database_name}"'
            url = f"https://api.fulcrumapp.com/api/v2/query?token={self.fulcrum_key}&q={query}&format=json"
            async with httpx.AsyncClient() as client:
                response = await client.get(url, timeout=30)
                response.raise_for_status()
                data = response.json()
                fetched_records = [
                    {
                        "_record_id": r.get("_record_id"),
                        "_latitude": r.get("_latitude"),
                        "_longitude": r.get("_longitude"),
                        "_status": r.get("_status"),
                    }
                    for r in data.get("rows", [])
                    if r.get("_latitude") is not None
                    and r.get("_longitude") is not None
                ]
            async with self:
                self.records = fetched_records
                if not self.records:
                    self.error_message = "No records with location data found."
        except httpx.HTTPStatusError as e:
            logging.exception(e)
            async with self:
                self.error_message = (
                    f"HTTP error: {e.response.status_code} - {e.response.text}"
                )
        except Exception as e:
            logging.exception(e)
            async with self:
                self.error_message = f"An unexpected error occurred: {str(e)}"
        finally:
            async with self:
                self.is_loading = False
import reflex as rx
import reflex_enterprise as rxe
from reflex_enterprise.components.map.types import latlng
from app.components.layout import layout
from app.states.dashboard_state import DashboardState


def map_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Map View", class_name="text-3xl font-bold text-gray-800 mb-6"),
        rx.el.div(
            rx.el.button(
                "Fetch Fulcrum Data",
                on_click=DashboardState.fetch_data,
                is_loading=DashboardState.is_loading,
                class_name="bg-emerald-600 text-white py-2 px-4 rounded-md hover:bg-emerald-700 font-semibold shadow-sm mb-6",
            ),
            rx.cond(
                DashboardState.error_message != "",
                rx.el.div(
                    rx.icon(
                        tag="flag_triangle_right", class_name="w-5 h-5 text-red-500"
                    ),
                    rx.el.p(DashboardState.error_message, class_name="text-red-700"),
                    class_name="flex items-center gap-2 p-4 bg-red-100 border border-red-200 rounded-lg mb-6",
                ),
                rx.el.div(),
            ),
            rx.el.div(
                rxe.map(
                    rxe.map.tile_layer(
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                    ),
                    rx.foreach(
                        DashboardState.records,
                        lambda record: rxe.map.marker(
                            position=latlng(
                                lat=record["_latitude"], lng=record["_longitude"]
                            ),
                            rxe_map_popup=rxe.map.popup(
                                f"Record ID: {record['_record_id']}"
                            ),
                        ),
                    ),
                    id="map-view",
                    center=latlng(lat=39.8283, lng=-98.5795),
                    zoom=4.0,
                    height="70vh",
                    width="100%",
                    class_name="rounded-lg shadow-sm border border-gray-200",
                ),
                class_name="w-full",
            ),
            class_name="flex flex-col",
        ),
    )


def map_view() -> rx.Component:
    return layout(map_content())
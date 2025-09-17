import reflex as rx
from app.states.dashboard_state import DashboardState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon(tag="menu", class_name="w-6 h-6"),
                on_click=DashboardState.toggle_sidebar,
                class_name="p-2 rounded-md text-gray-600 hover:bg-gray-100 hover:text-gray-800",
            )
        ),
        class_name="h-16 flex items-center px-4 bg-white/50 backdrop-blur-sm border-b border-gray-200",
    )
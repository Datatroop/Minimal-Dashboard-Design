import reflex as rx
from app.components.layout import layout
from app.states.dashboard_state import DashboardState


def summary_card(title: str, value: rx.Var[int], icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(title, class_name="text-sm font-medium text-gray-500"),
            rx.el.p(value, class_name="text-3xl font-bold text-gray-800"),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.icon(tag=icon, class_name="w-8 h-8 text-white"),
            class_name=f"p-3 rounded-full {color}",
        ),
        class_name="flex items-center justify-between p-6 bg-white rounded-lg shadow-sm border border-gray-200",
    )


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Dashboard", class_name="text-3xl font-bold text-gray-800 mb-6"),
        rx.cond(
            DashboardState.is_loading,
            rx.el.div(
                rx.el.div(
                    class_name="w-full h-24 bg-gray-200 rounded-md animate-pulse"
                ),
                rx.el.div(
                    class_name="w-full h-24 bg-gray-200 rounded-md animate-pulse"
                ),
                rx.el.div(
                    class_name="w-full h-24 bg-gray-200 rounded-md animate-pulse"
                ),
                rx.el.div(
                    class_name="w-full h-24 bg-gray-200 rounded-md animate-pulse"
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6",
            ),
            rx.el.div(
                summary_card(
                    "Total Records",
                    DashboardState.total_records,
                    "bar-chart-2",
                    "bg-blue-500",
                ),
                summary_card(
                    "New", DashboardState.new_records, "circle_plus", "bg-green-500"
                ),
                summary_card(
                    "In Progress",
                    DashboardState.in_progress_records,
                    "refresh-cw",
                    "bg-yellow-500",
                ),
                summary_card(
                    "Completed",
                    DashboardState.completed_records,
                    "square_check",
                    "bg-emerald-500",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6",
            ),
        ),
        rx.cond(
            DashboardState.error_message != "",
            rx.el.div(
                rx.icon(tag="flag_triangle_right", class_name="w-5 h-5 text-red-500"),
                rx.el.p(DashboardState.error_message, class_name="text-red-700"),
                class_name="flex items-center gap-2 p-4 bg-red-100 border border-red-200 rounded-lg",
            ),
            rx.el.div(),
        ),
        class_name="flex flex-col",
    )


def dashboard() -> rx.Component:
    return layout(dashboard_content())
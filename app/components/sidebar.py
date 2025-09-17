import reflex as rx
from app.states.dashboard_state import DashboardState
from app.states.auth_state import AuthState


def sidebar_item(text: str, href: str, icon: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(tag=icon, class_name="w-5 h-5"),
            rx.el.span(
                text,
                class_name=rx.cond(
                    DashboardState.sidebar_collapsed, "hidden", "whitespace-nowrap"
                ),
            ),
            class_name="flex items-center gap-3 p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors",
        ),
        href=href,
        class_name="block w-full",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon(tag="bar-chart-2", class_name="w-8 h-8 text-emerald-600"),
                rx.el.h2(
                    "Dashboard",
                    class_name=rx.cond(
                        DashboardState.sidebar_collapsed,
                        "hidden",
                        "text-2xl font-bold text-gray-800",
                    ),
                ),
                class_name="flex items-center gap-3 p-4 border-b border-gray-200",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "/", "layout-dashboard"),
                sidebar_item("Map View", "/map", "map"),
                sidebar_item("Page One", "/page-one", "file"),
                sidebar_item("Page Two", "/page-two", "file"),
                sidebar_item("Page Three", "/page-three", "file"),
                class_name="flex flex-col gap-1 p-2",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            sidebar_item("Sign Out", "#", "log-out"),
            on_click=AuthState.sign_out,
            class_name="p-2 border-t border-gray-200",
        ),
        class_name=rx.cond(
            DashboardState.sidebar_collapsed,
            "w-20 bg-white border-r border-gray-200 flex flex-col transition-all duration-300",
            "w-64 bg-white border-r border-gray-200 flex flex-col transition-all duration-300",
        ),
    )
import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def layout(main_content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(
                main_content,
                class_name="flex-1 p-4 sm:p-6 lg:p-8 bg-gray-50 overflow-y-auto",
            ),
            class_name="flex-1 flex flex-col h-screen",
        ),
        class_name="flex font-['Roboto']",
        on_mount=[AuthState.check_session, DashboardState.fetch_data],
    )
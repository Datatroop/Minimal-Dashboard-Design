import reflex as rx
from app.states.auth_state import AuthState


def sign_in_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Sign In", class_name="text-2xl font-bold text-center text-gray-800"
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Email", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        type="email",
                        id="email",
                        placeholder="user@example.com",
                        class_name="w-full px-3 py-2 mt-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Password", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        type="password",
                        id="password",
                        placeholder="••••••••",
                        class_name="w-full px-3 py-2 mt-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500",
                    ),
                    class_name="mb-6",
                ),
                rx.el.button(
                    "Sign In",
                    type="submit",
                    class_name="w-full bg-emerald-600 text-white py-2 px-4 rounded-md hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 font-semibold",
                ),
                on_submit=AuthState.sign_in,
            ),
            rx.el.p(
                "Don't have an account? ",
                rx.el.a(
                    "Sign Up",
                    href="/sign-up",
                    class_name="font-medium text-emerald-600 hover:text-emerald-500",
                ),
                class_name="mt-4 text-center text-sm text-gray-600",
            ),
            class_name="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-sm",
        ),
        class_name="min-h-screen flex items-center justify-center bg-gray-50 font-['Roboto']",
    )
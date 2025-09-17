import reflex as rx
from app.components.layout import layout


def page_two_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Page Two", class_name="text-3xl font-bold text-gray-800 mb-6"),
        rx.el.p("This is page two.", class_name="text-gray-600"),
        class_name="flex flex-col",
    )


def page_two() -> rx.Component:
    return layout(page_two_content())
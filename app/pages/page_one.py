import reflex as rx
from app.components.layout import layout


def page_one_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Page One", class_name="text-3xl font-bold text-gray-800 mb-6"),
        rx.el.p("This is page one.", class_name="text-gray-600"),
        class_name="flex flex-col",
    )


def page_one() -> rx.Component:
    return layout(page_one_content())
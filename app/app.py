import reflex as rx
import reflex_enterprise as rxe
from app.pages.sign_in import sign_in_page
from app.pages.sign_up import sign_up_page
from app.pages.dashboard import dashboard
from app.pages.map_view import map_view
from app.pages.page_one import page_one
from app.pages.page_two import page_two
from app.pages.page_three import page_three

app = rxe.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(dashboard, route="/")
app.add_page(map_view, route="/map")
app.add_page(page_one, route="/page-one")
app.add_page(page_two, route="/page-two")
app.add_page(page_three, route="/page-three")
app.add_page(sign_in_page, route="/sign-in")
app.add_page(sign_up_page, route="/sign-up")
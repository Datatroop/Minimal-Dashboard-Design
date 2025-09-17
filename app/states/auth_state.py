import reflex as rx
import os


class AuthState(rx.State):
    users: dict[str, str] = {"user@example.com": "password123"}
    in_session: bool = False
    error_message: str = ""

    @rx.event
    def sign_up(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]
        if email in self.users:
            self.error_message = "Email already in use."
            yield rx.toast.error(self.error_message)
            return
        self.users[email] = password
        self.in_session = True
        self.error_message = ""
        return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]
        if email in self.users and self.users[email] == password:
            self.in_session = True
            self.error_message = ""
            return rx.redirect("/")
        else:
            self.in_session = False
            self.error_message = "Invalid email or password."
            yield rx.toast.error(self.error_message)

    @rx.event
    def sign_out(self):
        self.in_session = False
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        if not self.in_session:
            return rx.redirect("/sign-in")
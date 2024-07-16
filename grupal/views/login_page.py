import reflex as rx

from ..modelos.estudiantes import *
from ..servicios.user_servicio import *

class PageState(rx.State):
    username: str = ""
    password: str = ""
    error_message: str = ""

    def handle_submit(self, form_data: dict):
        if servicio_autentificacion(form_data["username"], form_data["password"]):
            return rx.redirect("/estudiante")
        else:
            self.error_message = "Credenciales incorrectas"

    def clear_error(self, _=None):
        self.error_message = ""


@rx.page(route="/login")
def login_page() -> rx.Component:
    return rx.container(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Iniciar Sesion", value="login"),
                rx.tabs.trigger("Registrarse", value="signup"),
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("nombre de usuario", "Ingrese su usuario", "text", "username"),
                        form_fields("contraseña", "Ingrese su contraseña", "password", "password"),
                        rx.button("Iniciar Sesion", type="submit", color_scheme="blue"),
                        #Condicional
                        rx.cond(
                            PageState.error_message != "", 
                            rx.text(PageState.error_message, color="red", font_size="14px"),
                        ),
                        spacing="2",
                    ),
                    on_submit=PageState.handle_submit,
                ),
                value="login"
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("Email", "Ingrese su email", "email", "correo"),
                        form_fields("Nombre de usuario", "Ingrese su usuario", "text", "username"),
                        form_fields("contraseña", "Ingrese su contraseña", "password", "password"),
                        rx.button("Registrarse", type="submit", color_scheme="blue"),
                        spacing="2",
                        ),
                    ),
                    value="signup"
                ),
                    background="gray.800",
                    padding="20px",
                    border_radius="20px",
                    box_shadow="rgba(0,0,0,0.25) 0px 3px 8px",
                    width="500px",
                    margin="auto",
                    margin_top="100px",
                    border="2px solid gray",
            )
        )

def form_fields(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.form.label(label),
        rx.input(
            placeholder=placeholder,
            type = type,
            name = name,
            #on_focus = LoginState.clear_error,
            ),
            align_items = "flex-start",
            width="100%",
    )
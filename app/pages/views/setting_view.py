from flet import *

class settings_view(Container):
    def __init__(self, page: Page):
        self.page = page
    def build(self):
        return Container(
            content=Column(
                [
                    Text("Settings", size=30, weight="bold"),
                    Image(
                        src="https://via.placeholder.com/150",  # Enlace a una imagen de perfil temporal
                        width=150,
                        height=150,
                        fit="contain",
                    ),
                    Text("Nombre del Usuario", size=20, weight="bold"),
                    Text("usuario@email.com", size=16, color="gray"),
                    ElevatedButton(
                        text="Cerrar Sesión",
                        icon=icons.LOGOUT,
                        on_click=lambda e: print("Cerrando sesión..."),
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
            ),
            alignment=alignment.center,
            padding=20,
            bgcolor="green",
            expand=True,
        )

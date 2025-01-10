import flet as ft


# Componente para la vista Settings
def settings_view():
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Settings", size=30, weight="bold"),
                ft.Image(
                    src="https://via.placeholder.com/150",  # Enlace a una imagen de perfil temporal
                    width=150,
                    height=150,
                    fit="contain",
                ),
                ft.Text("Nombre del Usuario", size=20, weight="bold"),
                ft.Text("usuario@email.com", size=16, color="gray"),
                ft.ElevatedButton(
                    text="Cerrar Sesión",
                    icon=ft.icons.LOGOUT,
                    on_click=lambda e: print("Cerrando sesión..."),
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
        ),
        alignment=ft.alignment.center,
        padding=20,
    )

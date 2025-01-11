import flet as ft
from components.menu import menu
from components.titlebar import titlebar
from components.setting import settings_view
from components.home import home_view


def main_view(page: ft.Page):
    page.window.width = 600
    page.window.height = 400
    page.window.maximized = True
    page.padding = 0

    # Función para manejar la selección del menú
    def on_menu_item_click(item):
        if item == "home":
            content.controls.clear()  # Limpiar controles
            content.controls.append(home_view())  # Agregar vista Home
        elif item == "settings":
            content.controls.clear()  # Limpiar controles
            content.controls.append(settings_view())  # Agregar vista Settings
        else:
            content.controls.clear()
            content.controls.append(
                ft.Text(f"View: {item}", size=24))  # Vista no definida
        content.update()

    # Contenedor dinámico para las vistas
    content = ft.Column(
        [
            ft.Text("Welcome to the main view!", size=24),
        ],
        expand=True,
        alignment=ft.alignment.center,
    )

    # Estructura principal
    return ft.Column(
        [
            titlebar(page),
            ft.Row(
                [
                    menu(on_menu_item_click),  # Menú lateral
                    ft.Container(content=content, expand=True,
                                 padding=16, bgcolor=ft.colors.BLACK26),
                ],
                expand=True,
                spacing=0,
            ),
        ],
        expand=True,
        spacing=0,
    )

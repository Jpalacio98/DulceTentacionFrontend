import flet as ft
from components.menu import menu
from components.titlebar import titlebar


def main_view(page: ft.Page):
    page.window.width = 1024
    page.window.height = 768
    page.window.maximized = True
    page.padding = 0

    def on_menu_item_click(item):
        content.value = f"Selected: {item}"
        page.update()

    content = ft.Text("Welcome to the main view!", size=24)
    return ft.Column([
        titlebar(page),
        ft.Row(
            [
                menu(on_menu_item_click),
                ft.Container(content=content, expand=True, padding=16),
            ],
            expand=True,
        )], expand=True,)

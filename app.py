import flet as ft
from views.login_view import login_view
from views.main_view import main_view

def main(page: ft.Page):
    def switch_to_main_view():
        page.clean()
        page.add(main_view(page))

    page.title = "App with Sidebar"
    page.window.width = 400
    page.window.height = 700
    ft.Window
    page.window.center()
    page.window.resizable = False
    page.window.title_bar_buttons_hidden = True
    page.window.title_bar_hidden = True
    page.window.frameless = True
    # Fondo transparente para mostrar bordes redondeados
    page.window.bgcolor = "transparent"
    page.bgcolor = "transparent"
    page.add(login_view(page, switch_to_main_view))


ft.app(target=main)

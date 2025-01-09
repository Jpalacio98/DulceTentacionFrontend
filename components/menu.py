import flet as ft

def menu(on_menu_item_click):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Menu", size=20, weight="bold"),
                ft.ListTile(title=ft.Text("Home"), on_click=lambda e: on_menu_item_click("home")),
                ft.ListTile(title=ft.Text("Settings"), on_click=lambda e: on_menu_item_click("settings")),
            ],
            alignment="start",
        ),
        width=200,
        padding=16,
    )

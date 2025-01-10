import flet as ft


def titlebar(page: ft.Page):
    # Inicializar el estado maximizado como un atributo del objeto `page`
    page.is_maximized = True

    def on_close_click(e):
        page.window.close()

    def on_max_click(e):
        if page.is_maximized:
            # Restaurar la ventana a un tamaño específico
            page.window.center()
            max_button.content = ft.Image(src="src/image/maximize.png", width=20, height=20)
            max_button.tooltip = "Restaurar"
            page.window.maximized = False
            page.is_maximized = False
        else:
            # Maximizar la ventana
            max_button.content = ft.Image(src="src/image/restore.png", width=20, height=20)
            max_button.tooltip = "Restaurar"
            page.window.maximized = True
            page.is_maximized = True
        page.update()

    def on_min_click(e):
        page.window.minimized = True
        page.update()

    max_button = ft.IconButton(
        content=ft.Image(src="src/image/restore.png", width=20, height=20),
        tooltip="Maximizar",on_click=on_max_click
    )
    min_button = ft.IconButton(
        content=ft.Image(src="src/image/minimize.png", width=20, height=20),
        tooltip="Minimizar",on_click=on_min_click
    )
    close_button = ft.IconButton(
        content=ft.Image(src="src/image/close.png", width=20, height=20),
        tooltip="Cerrar",on_click=on_close_click
    )
    return ft.Container(
        padding=ft.Padding(20,0,5,0),
        bgcolor=ft.colors.BLACK,
        height=50,
        content=ft.Row(
            [
                ft.Image(src="src\\image\\facebook.png", width=40, height=40),
                ft.WindowDragArea(
                    ft.Container(bgcolor=ft.Colors.TRANSPARENT, padding=10),
                    expand=True,
                ),
                min_button,
                max_button,
                close_button,
            ],alignment=ft.alignment.center,
        ),
    )

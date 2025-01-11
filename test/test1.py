import flet as ft

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "App de Escritorio con Bordes Redondeados"
    page.window.width = 400
    page.window.height = 700
    page.window.center()
    page.window.frameless = True  # Elimina el marco del sistema operativo
    page.window.bgcolor = "transparent"  # Fondo transparente para mostrar bordes redondeados
    page.bgcolor = "transparent"

    # Contenedor principal con bordes redondeados
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("¡Bienvenido a tu App!", size=20, color="white"),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Minimizar", on_click=lambda e: page.window.minimize()),
                        ft.ElevatedButton("Cerrar", on_click=lambda e: page.window.close()),
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
        bgcolor="#4A90E2",  # Color del contenedor
        border_radius=30,   # Bordes redondeados
        padding=20,
        expand=True,
    )

    # Agregar contenedor a la página
    page.add(
        ft.Stack(
            controls=[
                container,
            ],
            expand=True,
        )
    )

ft.app(target=main)

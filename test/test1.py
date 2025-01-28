# import flet as ft

import flet as ft

def main(page: ft.Page):
    # Define el diálogo secundario
    secondary_dialog = ft.AlertDialog(
        title=ft.Text("Diálogo Secundario"),
        content=ft.Text("Este es el diálogo secundario que se abre sin cerrar el primero."),
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.close(secondary_dialog)),
        ],
    )

    # Define el diálogo principal
    primary_dialog = ft.AlertDialog(
        title=ft.Text("Diálogo Principal"),
        content=ft.Text("Este es el diálogo principal. Puedes abrir otro desde aquí."),
        actions=[
            ft.TextButton("Abrir Secundario", on_click=lambda e: page.open(secondary_dialog)),
            ft.TextButton("Cerrar", on_click=lambda e: page.close(primary_dialog)),
        ],
    )

    # Botón para abrir el diálogo principal
    open_dialog_button = ft.ElevatedButton(
        "Abrir Diálogo Principal",
        on_click=lambda e: page.open(primary_dialog),
    )

    # Agregar el botón al contenido de la página
    page.add(open_dialog_button)

    # Configurar los diálogos en la página
    page.dialog = primary_dialog
    page.overlay.append(secondary_dialog)  # Asegúrate de agregar el secundario al overlay

    page.update()

ft.app(main)

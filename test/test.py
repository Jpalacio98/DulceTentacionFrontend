import flet as ft

def main(page: ft.Page):
    class TextFieldCustom(ft.TextField):
        def __init__(self, label, **kwargs):
            super().__init__(
                label=label,
                selection_color="#D91E2E",  # Color de selección
                focus_color= ft.Colors.BLACK,
                bgcolor="#D91E2E",
                filled= False,
                **kwargs
            )

    def on_submit(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Escribiste: {textfield.value}"))
        page.snack_bar.open = True
        page.update()

    textfield = TextFieldCustom(label="Ingresa texto", on_submit=on_submit)

    page.add(
        ft.Column([
            textfield,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)

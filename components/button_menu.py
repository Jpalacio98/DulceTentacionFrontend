import flet as ft


class button_menu(ft.Container):

    def __init__(self, icon, label, on_click, expanded=False):
        self.text_widget = ft.Text(
            label, opacity=1 if expanded else 0, animate_opacity=300)
        super().__init__(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Image(src=icon, width=24, height=24),
                        self.text_widget

                    ],
                    spacing=10,
                    alignment="start"
                ),
                on_click=on_click,
                padding=8,


            ))
        self.expand = expanded

    def set_expanded(self, expanded):
        self.expand = expanded
        self.text_widget.opacity = 1 if expanded else 0
        self.text_widget.update()

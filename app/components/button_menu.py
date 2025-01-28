import flet as ft


class ButtonMenu(ft.Container):
    def __init__(self, icon, label, on_click, OnHover=False): 
        self.icon_widget =ft.Image(
            src=icon,
            width=25 if OnHover  else 40,
            height=25 if OnHover else 40,
            animate_size=150
            )
        self.text_widget = ft.Text(
            label,
            opacity=1 if OnHover else 0,
            animate_opacity=300
        )
       
        super().__init__(
            content=ft.Container(
                content=ft.Row(
                    [
                        self.icon_widget,
                        self.text_widget

                    ],
                    spacing=10,
                    alignment="start"
                ),
                on_click=on_click,
                padding=8, ink=True, ink_color='#D91E2E'

            ))
        self.isOnHover = OnHover

    def set_OnHover(self, OnHover):
        self.text_widget.opacity = 1 if OnHover else 0
        self.icon_widget.width = 25 if OnHover else 40
        self.icon_widget.height = 25 if OnHover else 40
        self.icon_widget.update()
        self.text_widget.update()
        

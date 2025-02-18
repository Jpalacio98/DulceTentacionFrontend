

from flet import *

from app.components.text_field import TextFieldCustom3


class BillingDataClientView(Container):
    def __init__(self, page=Page):
        super().__init__()

    def build(self):
        return Container(
            expand=1,
            alignment=alignment.center,
            content=Container(
                padding=20,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        Image(
                            "static/images/user.png",
                            width=75,
                            height=75,
                            fit=ImageFit.FILL,
                            border_radius=10
                        ),

                        TextFieldCustom3(hint_text="Cedula"),
                        TextFieldCustom3(hint_text="Nombre"),
                        TextFieldCustom3(hint_text="Correo"),
                        TextFieldCustom3(hint_text="Telefono"),

                    ]
                )
            )
        )



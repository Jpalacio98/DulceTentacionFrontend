from flet import *
from ...utils.color_schema import *


class EmployeeCard(Card):
    def __init__(self, data, page=Page, on_delete=None, on_edit=None):
        super().__init__()
        self.page = page
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.data = {
            "name": data.get("name", "Sin nombre"),
            "email": data.get("email", ""),
            "role": data.get("role", ""),
            "phone": data.get("phone", ""),
        }

    def handle_delete(self, e):
        if self.on_delete:
            self.on_delete(self.data)

    def handle_edit(self, e):
        if self.on_edit:
            self.on_edit(self.data)

    def build(self):
        return Card(
            elevation=0,
            content=Container(
                bgcolor="#FEFAE9",
                border_radius=10,
                width=300,
                content=Column(
                    [
                        # Header rojo con nombre
                        Container(
                            bgcolor=color_h1,
                            padding=padding.symmetric(horizontal=15, vertical=10),
                            border_radius=border_radius.only(top_left=10, top_right=10),
                            content=Row(
                                [
                                    Text(
                                        self.data["name"],
                                        color=colors.WHITE,
                                        weight=FontWeight.BOLD,
                                        size=14,
                                    )
                                ]
                            ),
                        ),
                        # Contenido con la información
                        Container(
                            padding=padding.all(15),
                            content=Column(
                                [
                                    Row(
                                        [
                                            Text(
                                                "Correo:",
                                                weight=FontWeight.BOLD,
                                                color=colors.BLACK,
                                            ),
                                            Text(
                                                self.data["email"], color=colors.BLACK
                                            ),
                                        ]
                                    ),
                                    Row(
                                        [
                                            Text(
                                                "Rol:",
                                                weight=FontWeight.BOLD,
                                                color=colors.BLACK,
                                            ),
                                            Text(self.data["role"], color=colors.BLACK),
                                        ]
                                    ),
                                    Row(
                                        [
                                            Text(
                                                "Teléfono:",
                                                weight=FontWeight.BOLD,
                                                color=colors.BLACK,
                                            ),
                                            Text(
                                                self.data["phone"], color=colors.BLACK
                                            ),
                                        ]
                                    ),
                                    # Botones de acción
                                    Container(
                                        content=Row(
                                            [
                                                IconButton(
                                                    icon=icons.DELETE_OUTLINE,
                                                    icon_color=color_h1,
                                                    tooltip="Eliminar",
                                                    on_click=self.handle_delete,
                                                ),
                                                IconButton(
                                                    icon=icons.EDIT,
                                                    icon_color=color_h1,
                                                    tooltip="Editar",
                                                    on_click=self.handle_edit,
                                                ),
                                            ],
                                            alignment=MainAxisAlignment.CENTER,
                                        )
                                    ),
                                ],
                                spacing=10,
                            ),
                        ),
                    ]
                ),
            ),
        )

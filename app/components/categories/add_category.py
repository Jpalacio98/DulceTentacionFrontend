from flet import *
from ...components.text_field import TextFieldCustom3
from ...utils.color_schema import *


class AddCategory(AlertDialog):
    def __init__(self, page=Page):
        super().__init__()
        self.page = page
        self.open = False
        self.shape = RoundedRectangleBorder(radius=15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        self.is_editing = False
        self.on_save = None

        # Campos del formulario
        self.code_field = TextFieldCustom3("Código", width=400)
        self.name_field = TextFieldCustom3("Nombre", width=400)

        # Textos dinámicos
        self.modal_title = Text(
            value="Registrar Categoría",
            size=18,
            color=text_color_2,
            weight=FontWeight.BOLD,
        )

        self.save_button = ElevatedButton(
            text="Guardar",
            bgcolor=color_h1,
            color=text_color_2,
            width=200,
            on_click=self.save_category,
        )

        # Título del modal con logo y botón cerrar
        self.title = Container(
            bgcolor=color_h1,
            border_radius=BorderRadius(15, 15, 0, 0),
            expand=True,
            width=450,
            content=Row(
                [
                    Image(
                        "static/images/logo.png",
                        width=70,
                        height=40,
                        fit=ImageFit.CONTAIN,
                    ),
                    Container(
                        content=self.modal_title,
                        alignment=alignment.center,
                        expand=True,
                    ),
                    IconButton(
                        icon=icons.CLOSE,
                        icon_color=text_color_2,
                        on_click=self.close_dlg,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=padding.only(left=15, right=10),
            height=70,
        )

        # Contenido del modal
        self.content = Container(
            width=450,
            height=220,
            bgcolor="#FEFAE9",
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=padding.only(top=20, left=20, right=20, bottom=30),
            content=Column(
                [
                    Column(
                        [
                            self.code_field,
                            self.name_field,
                        ],
                        spacing=15,
                    ),
                    Container(height=20),
                    Row([self.save_button], alignment=MainAxisAlignment.CENTER),
                ]
            ),
        )

    def save_category(self, e):
        data = {
            "code": self.code_field.value,
            "name": self.name_field.value,
        }
        if self.on_save:
            self.on_save(data)
        self.close_dlg(e)

    def show_for_edit(self, category_data, on_save):
        self.is_editing = True
        self.on_save = on_save
        self.modal_title.value = "Editar Categoría"
        self.save_button.text = "Actualizar"
        self.code_field.value = category_data["code"]
        self.code_field.read_only = True
        self.name_field.value = category_data["name"]
        self.page.update()
        self.page.open(self)

    def show_for_add(self, on_save):
        self.is_editing = False
        self.on_save = on_save
        self.modal_title.value = "Registrar Categoría"
        self.save_button.text = "Guardar"
        self.code_field.read_only = False
        self.code_field.value = ""
        self.name_field.value = ""
        self.page.update()
        self.page.open(self)

    def close_dlg(self, e):
        self.open = False
        self.page.update()

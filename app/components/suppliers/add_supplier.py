from flet import *
from app.components.text_field import TextFieldCustom3
from app.utils.color_schema import *


class AddSupplier(AlertDialog):
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
        self.nit_field = TextFieldCustom3("NIT", width=400)
        self.name_field = TextFieldCustom3("Nombre", width=400)
        self.email_field = TextFieldCustom3("Correo", width=400)
        self.phone_field = TextFieldCustom3("Teléfono", width=400)

        # Textos dinámicos
        self.modal_title = Text(
            value="Registrar Proveedor",
            size=18,
            color=text_color_2,
            weight=FontWeight.BOLD,
        )

        self.save_button = ElevatedButton(
            text="Guardar",
            bgcolor=color_h1,
            color=text_color_2,
            width=200,
            on_click=self.save_supplier,
        )

        # Título del modal
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
                    self.modal_title,
                    IconButton(
                        icon=icons.CLOSE,
                        icon_color=text_color_2,
                        on_click=self.close_dlg,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=padding.only(left=15, right=10),
            height=70,  # Altura ajustada del modal
        )

        # Contenido del modal
        self.content = Container(
            width=450,
            height=400,  # Definir alto fijo para el modal
            bgcolor="#FEFAE9",
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=padding.only(top=20, left=20, right=20, bottom=30),
            content=Column(
                [
                    Column(
                        [
                            self.code_field,
                            self.nit_field,
                            self.name_field,
                            self.email_field,
                            self.phone_field,
                        ],
                        spacing=15,  # Espaciado entre campos
                    ),
                    Container(height=20),
                    Row(
                        [self.save_button],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ]
            ),
        )

    def save_supplier(self, e):
        data = {
            "code": self.code_field.value,
            "nit": self.nit_field.value,
            "name": self.name_field.value,
            "email": self.email_field.value,
            "phone": self.phone_field.value,
        }
        if self.on_save:
            self.on_save(data)
        self.close_dlg(e)

    def show_for_edit(self, supplier_data, on_save):
        """Configura y muestra el modal para editar un proveedor"""
        self.is_editing = True
        self.on_save = on_save

        # Cambiar textos para modo edición
        self.modal_title.value = "Editar Proveedor"
        self.save_button.text = "Actualizar"

        # Llenar los campos con los datos del proveedor
        self.code_field.value = supplier_data["code"]
        self.code_field.read_only = True  # El código no se puede editar
        self.nit_field.value = supplier_data["nit"]
        self.name_field.value = supplier_data["name"]
        self.email_field.value = supplier_data["email"]
        self.phone_field.value = supplier_data["phone"]

        self.page.update()
        self.page.open(self)

    def show_for_add(self, on_save):
        """Configura y muestra el modal para agregar un proveedor"""
        self.is_editing = False
        self.on_save = on_save

        # Cambiar textos para modo agregar
        self.modal_title.value = "Registrar Proveedor"
        self.save_button.text = "Guardar"

        self.code_field.read_only = False

        # Limpiar campos
        self.code_field.value = ""
        self.nit_field.value = ""
        self.name_field.value = ""
        self.email_field.value = ""
        self.phone_field.value = ""

        self.page.update()
        self.page.open(self)

    def close_dlg(self, e):
        self.open = False
        self.page.update()

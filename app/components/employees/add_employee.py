from flet import *
from ...components.text_field import TextFieldCustom3
from ...utils.color_schema import *


class AddEmployee(AlertDialog):
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
        self.photo_path = None

        # Campos del formulario
        self.name_field = TextFieldCustom3("Nombre", width=400)
        self.email_field = TextFieldCustom3("Correo", width=400)
        self.role_field = TextFieldCustom3("Rol", width=400)
        self.phone_field = TextFieldCustom3("Teléfono", width=400)

        # FilePicker para la foto
        self.file_picker = FilePicker(on_result=self.on_file_selected)
        self.photo_preview = Image(
            src="",
            width=80,
            height=80,
            border_radius=40,
            fit=ImageFit.COVER,
            visible=False,
        )
        self.pick_button = ElevatedButton(
            text="Seleccionar Foto",
            bgcolor=color_h1,
            color=text_color_2,
            width=200,
            on_click=lambda e: self.file_picker.pick_files(
                allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg"]
            ),
        )

        # Textos dinámicos
        self.modal_title = Text(
            value="Registrar Empleado",
            size=18,
            color=text_color_2,
            weight=FontWeight.BOLD,
        )

        self.save_button = ElevatedButton(
            text="Guardar",
            bgcolor=color_h1,
            color=text_color_2,
            width=200,
            on_click=self.save_employee,
        )

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

        self.content = Container(
            width=450,
            height=540,
            bgcolor="#FEFAE9",
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=padding.only(top=20, left=20, right=20, bottom=30),
            content=Column(
                [
                    Row(
                        [self.photo_preview],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    self.pick_button,
                    self.name_field,
                    self.email_field,
                    self.role_field,
                    self.phone_field,
                    Container(height=20),
                    Row(
                        [self.save_button],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=15,
            ),
        )
        self.controls = [self.file_picker]
        if self.file_picker not in self.page.overlay:
            self.page.overlay.append(self.file_picker)
            self.page.update()

    def on_file_selected(self, e):
        if e.files and len(e.files) > 0:
            self.photo_path = e.files[0].path
            self.photo_preview.src = self.photo_path
            self.photo_preview.visible = True
            self.page.update()

    def save_employee(self, e):
        data = {
            "name": self.name_field.value,
            "email": self.email_field.value,
            "role": self.role_field.value,
            "phone": self.phone_field.value,
            "photo": self.photo_path,
        }
        if self.on_save:
            self.on_save(data)
        self.close_dlg(e)

    def show_for_edit(self, employee_data, on_save):
        self.is_editing = True
        self.on_save = on_save
        self.modal_title.value = "Editar Empleado"
        self.save_button.text = "Actualizar"
        self.name_field.value = employee_data["name"]
        self.email_field.value = employee_data["email"]
        self.role_field.value = employee_data["role"]
        self.phone_field.value = employee_data["phone"]
        self.photo_path = employee_data.get("photo", None)
        if self.photo_path:
            self.photo_preview.src = self.photo_path
            self.photo_preview.visible = True
        else:
            self.photo_preview.visible = False
        self.page.update()
        self.page.open(self)

    def show_for_add(self, on_save):
        self.is_editing = False
        self.on_save = on_save
        self.modal_title.value = "Registrar Empleado"
        self.save_button.text = "Guardar"
        self.name_field.value = ""
        self.email_field.value = ""
        self.role_field.value = ""
        self.phone_field.value = ""
        self.photo_path = None
        self.photo_preview.visible = False
        self.page.update()
        self.page.open(self)

    def close_dlg(self, e):
        self.open = False
        self.page.update()

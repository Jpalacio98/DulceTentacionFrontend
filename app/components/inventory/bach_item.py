from flet import *

class BatchForm(Container):
    def __init__(self, on_save, on_cancel, form_data=None,page=Page):
        super().__init__()
        self.page = page
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.form_data = form_data or {}
        

    def build(self):
        # Campos del formulario
        self.id_field = TextField(label="ID", value=self.form_data.get("id", ""), disabled=True)
        self.name_field = TextField(label="Nombre", value=self.form_data.get("name", ""))
        self.unit_field = TextField(
            label="Unidad", value=self.form_data.get("unit", ""), keyboard_type=KeyboardType.NUMBER
        )
        self.price_field = TextField(
            label="Precio", value=self.form_data.get("price", ""), keyboard_type=KeyboardType.NUMBER
        )
        self.quantity_field = TextField(
            label="Cantidad", value=self.form_data.get("quantity", ""), keyboard_type=KeyboardType.NUMBER
        )
        self.expiry_date_field = TextField(
            label="Fecha de Vencimiento", value=self.form_data.get("expiry_date", "")
        )
        self.supplier_field = TextField(label="Proveedor", value=self.form_data.get("supplier", ""))
        self.title=Text("Añadir un lote",size=18,weight=FontWeight.BOLD)
        print(self.form_data)
        # Contenedor del formulario
        return Container(
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    self.title,
                    Container(width=1,height=10),
                    self.id_field,
                    self.name_field,
                    self.unit_field,
                    self.price_field,
                    self.quantity_field,
                    self.expiry_date_field,
                    self.supplier_field,
                    Container(width=1,height=20),
                    Row(
                        spacing=50,
                        controls=[
                            ElevatedButton("Guardar", on_click=self.on_save),
                            ElevatedButton("Cancelar", on_click=self.on_cancel),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER
                    ),
                ]
            ),
            bgcolor=Colors.SURFACE,
            width=400,
            padding=20,
            border_radius=15,
            offset=Offset(3, 0),  # Oculto inicialmente
            animate_offset=Animation(300, AnimationCurve.EASE),
        )
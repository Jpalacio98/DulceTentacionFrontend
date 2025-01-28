from flet import *

from app.components.custom_button import IconButtonAction
from app.components.custom_data_table import CustomDataTable
from app.components.dividerCustom import DivCustom
from app.components.products.product_detail_add import ProductDetail
from app.components.text_field import PlainTextField, SearchTextFieldCustom, TextFieldCustom3
from app.models.inventory import Inventory


class AddProduct(AlertDialog):
    def __init__(self, page=Page):
        super().__init__()
        self.inventoryInstance = Inventory()
        self.page = page
        self.open = False
        self.shape = RoundedRectangleBorder(15)
        self.title_padding = 0
        self.content_padding = 0
        self.actions_padding = 0
        self.actions = None
        self.elevation = 100
        self.shadow_color = Colors.RED_300
        self.ref = TextFieldCustom3("Referencia", width=150)
        self.name = TextFieldCustom3("Nombre", width=150)
        self.stock_min = TextFieldCustom3("Precio", width=150)
        self.category = TextFieldCustom3("Categoria", width=150)
        self.description = PlainTextField("descripcion", width=310)
        data = [
        {"nombre": "Manzanas", "ref": "PROD-000001",
            "precio": 41.16, "stock": 245, "unidad": "cm3"},
        {"nombre": "Leche", "ref": "PROD-000002",
            "precio": 33.08, "stock": 403, "unidad": "unidades"},
        {"nombre": "Pan", "ref": "PROD-000003", "precio": 97.94,
            "stock": 234, "unidad": "kilogramos"},
        {"nombre": "Huevos", "ref": "PROD-000004",
            "precio": 70.69, "stock": 264, "unidad": "kilogramos"},
        {"nombre": "Arroz", "ref": "PROD-000005",
            "precio": 34.59, "stock": 37, "unidad": "litros"},
        {"nombre": "Frijoles", "ref": "PROD-000006",
            "precio": 5.9, "stock": 173, "unidad": "unidades"},
        {"nombre": "Harina", "ref": "PROD-000007",
            "precio": 89.24, "stock": 286, "unidad": "gramos"},
        {"nombre": "Azúcar", "ref": "PROD-000008",
            "precio": 65.88, "stock": 273, "unidad": "litros"},
        {"nombre": "Sal", "ref": "PROD-000009",
            "precio": 13.79, "stock": 284, "unidad": "gramos"},
        {"nombre": "Aceite", "ref": "PROD-000010",
            "precio": 31.76, "stock": 225, "unidad": "cm3"},
        {"nombre": "Carne de Res", "ref": "PROD-000011",
            "precio": 61.2, "stock": 191, "unidad": "gramos"},
        {"nombre": "Pescado", "ref": "PROD-000012",
            "precio": 86.14, "stock": 61, "unidad": "kilogramos"},
        {"nombre": "Pollo", "ref": "PROD-000013",
            "precio": 91.71, "stock": 430, "unidad": "cm3"},
        {"nombre": "Queso", "ref": "PROD-000014", "precio": 99.83,
            "stock": 348, "unidad": "kilogramos"},
        {"nombre": "Yogur", "ref": "PROD-000015",
            "precio": 21.46, "stock": 351, "unidad": "unidades"},
        {"nombre": "Café", "ref": "PROD-000016",
            "precio": 54.04, "stock": 51, "unidad": "unidades"},
        {"nombre": "Té", "ref": "PROD-000017",
            "precio": 16.14, "stock": 153, "unidad": "litros"},
        {"nombre": "Cereal", "ref": "PROD-000018",
            "precio": 40.67, "stock": 345, "unidad": "unidades"},
        {"nombre": "Jugo de Naranja", "ref": "PROD-000019",
            "precio": 59.15, "stock": 257, "unidad": "litros"},
        {"nombre": "Chocolate", "ref": "PROD-000020",
            "precio": 2.38, "stock": 426, "unidad": "cm3"}
    ]

   
        self.product_details =  ProductDetail(data, page)
        
        self.image_container = Container(
            width=150,
            height=150,
            border_radius=75,
            border=border.all(color="black", width=1),
            content=Icon(name=Icons.CAMERA, size=50),
        )

        
        # Selector de archivos
        self.file_picker = FilePicker(on_result=self.load_image)
        self.page.overlay.append(self.file_picker)

        self.title = Container(
            bgcolor="red",
            border_radius=BorderRadius(15, 15, 0, 0),
            expand=True,
            width=1300,

            content=Row(
                [
                    Image(
                        "static/images/logo.png",
                        width=70,
                        height=40,
                        fit=ImageFit.CONTAIN
                    ),
                    Text(value="Añadir un producto al menu", size=18,
                         weight=FontWeight.BOLD, color=Colors.WHITE),
                    Container(height=1, expand=True, bgcolor=Colors.WHITE),
                    IconButton(
                        icon_color=Colors.WHITE,
                        icon=icons.CLOSE,
                        on_click=lambda x: self.page.close(self)
                    )
                ]
            )
        )
        self.content = Container(
            content=Column(
                controls=[
                    Row(
                        spacing=0,
                        controls=[
                            Container(
                                padding=10,
                                height=580,
                                width=350,
                                
                                bgcolor=Colors.WHITE,
                                content=Column(
                                    alignment=MainAxisAlignment.START,
                                    controls=[
                                        DivCustom("Informacion Basica"),
                                        Container(width=1,
                                                  height=20),
                                        Column(
                                            controls=[
                                                GestureDetector(
                                                    content=self.image_container,
                                                    on_tap=lambda e: self.file_picker.pick_files(
                                                    ),
                                                ),
                                                Container(
                                                    padding=0, 
                                                    height=150, 
                                                    content=Column(
                                                    controls=[
                                                        Row(
                                                            controls=[
                                                                self.ref,
                                                                self.name
                                                            ], alignment=MainAxisAlignment.CENTER, expand_loose=True
                                                        ),
                                                        Container(
                                                            height=10, width=1,),
                                                        Row(
                                                            controls=[
                                                                self.stock_min,
                                                                self.category
                                                            ], alignment=MainAxisAlignment.CENTER, expand_loose=True
                                                        )
                                                    ], alignment=MainAxisAlignment.CENTER, expand_loose=True,
                                                ),
                                                ),
                                                self.description
                                            ], spacing=20, horizontal_alignment=CrossAxisAlignment.CENTER, alignment=MainAxisAlignment.CENTER
                                        ),
                                    ]
                                )
                            ),
                            self.product_details.build(),

                        ]
                    ),
                    Container(width=1,
                              height=10),
                    IconButtonAction(
                        "Guardar", "static/images/disk.png", on_click=lambda e: ()),
                    Container(width=1,
                              height=40),
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,spacing=0,
            ),
            
            bgcolor=Colors.GREEN,
            border_radius=BorderRadius(0, 0, 15, 15),
            padding=20, height=850
        )

     # Función para cargar la imagen en el contenedor
    def load_image(self, e):
        if self.file_picker.result and self.file_picker.result.files:
            selected_file = self.file_picker.result.files[0].path
            self.image_container.content = Image(
                src=selected_file, fit="cover")
            self.page.update()

    # def add_new(self):
    #     data = {
    #         "ref": self.ref.value,
    #         "name": self.name.value,
    #         "category": self.category.value,
    #         "stock_min": int(self.stock_min.value),
    #         "unit": self.unit.value,
    #         "description": self.description.value,
    #         "branch_id": "ratQVKAJpFUZNVFzQS1Pqkanvoz2"
    #     }

    #     res = self.inventoryInstance.add(data)
    #     if res:
    #         self.page.close(self)

    def build(self):
        return super().build()

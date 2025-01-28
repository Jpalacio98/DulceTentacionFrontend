# from flet import *

# from app.components.custom_data_table import CustomDataTable, CustomDataTableEdit
# from app.components.dividerCustom import DivCustom
# from app.components.inventory.inventory_item import ItemInventory, ProductoItemInventory
# from app.components.products.product_detail_add import ProductDetail
# from app.components.text_field import SearchTextFieldCustom

# # from app.components.inventory.inventory_add import AddInventory
# # from app.components.inventory.inventory_item import ItemInventory
# # from app.components.inventory.inventory_replenish import ReplenishInventory


# # def main(page: Page):
# #     page.title = "AlertDialog examples"
# #     page.window.maximized = False
# #     page.horizontal_alignment = CrossAxisAlignment.CENTER
# #     page.bgcolor="#001E2E"
# #     data = [
# #         {"nombre": "Manzanas", "ref": "PROD-000001",
# #             "precio": 41.16, "stock": 245, "unidad": "cm3"},
# #         {"nombre": "Leche", "ref": "PROD-000002",
# #             "precio": 33.08, "stock": 403, "unidad": "unidades"},
# #         {"nombre": "Pan", "ref": "PROD-000003", "precio": 97.94,
# #             "stock": 234, "unidad": "kilogramos"},
# #         {"nombre": "Huevos", "ref": "PROD-000004",
# #             "precio": 70.69, "stock": 264, "unidad": "kilogramos"},
# #         {"nombre": "Arroz", "ref": "PROD-000005",
# #             "precio": 34.59, "stock": 37, "unidad": "litros"},
# #         {"nombre": "Frijoles", "ref": "PROD-000006",
# #             "precio": 5.9, "stock": 173, "unidad": "unidades"},
# #         {"nombre": "Harina", "ref": "PROD-000007",
# #             "precio": 89.24, "stock": 286, "unidad": "gramos"},
# #         {"nombre": "Azúcar", "ref": "PROD-000008",
# #             "precio": 65.88, "stock": 273, "unidad": "litros"},
# #         {"nombre": "Sal", "ref": "PROD-000009",
# #             "precio": 13.79, "stock": 284, "unidad": "gramos"},
# #         {"nombre": "Aceite", "ref": "PROD-000010",
# #             "precio": 31.76, "stock": 225, "unidad": "cm3"},
# #         {"nombre": "Carne de Res", "ref": "PROD-000011",
# #             "precio": 61.2, "stock": 191, "unidad": "gramos"},
# #         {"nombre": "Pescado", "ref": "PROD-000012",
# #             "precio": 86.14, "stock": 61, "unidad": "kilogramos"},
# #         {"nombre": "Pollo", "ref": "PROD-000013",
# #             "precio": 91.71, "stock": 430, "unidad": "cm3"},
# #         {"nombre": "Queso", "ref": "PROD-000014", "precio": 99.83,
# #             "stock": 348, "unidad": "kilogramos"},
# #         {"nombre": "Yogur", "ref": "PROD-000015",
# #             "precio": 21.46, "stock": 351, "unidad": "unidades"},
# #         {"nombre": "Café", "ref": "PROD-000016",
# #             "precio": 54.04, "stock": 51, "unidad": "unidades"},
# #         {"nombre": "Té", "ref": "PROD-000017",
# #             "precio": 16.14, "stock": 153, "unidad": "litros"},
# #         {"nombre": "Cereal", "ref": "PROD-000018",
# #             "precio": 40.67, "stock": 345, "unidad": "unidades"},
# #         {"nombre": "Jugo de Naranja", "ref": "PROD-000019",
# #             "precio": 59.15, "stock": 257, "unidad": "litros"},
# #         {"nombre": "Chocolate", "ref": "PROD-000020",
# #             "precio": 2.38, "stock": 426, "unidad": "cm3"}
# #     ]

# #     dlg =ReplenishInventory(data,page).build()
# #     page.add(
# #        ElevatedButton("reabastecer",on_click= lambda x: page.open(dlg))
# #     )


# # app(main)


# # from flet import *

# # from app.components.custom_data_table import CustomDataTable
# # from app.components.inventory.inventory_add import AddInventory
# # from app.components.inventory.inventory_item import ItemInventory
# # from app.components.inventory.inventory_replenish import ReplenishInventory

# # class bachView(Container):
# #     def __init__(self, data,page=Page):
# #         super().__init__()

# #         self.table = CustomDataTable(
# #             columns=["Unidades", "Precio", "Cantidad",
# #                      "Fecha de Vencimiento", "Proveedor"],
# #             data=[  # Datos iniciales
# #                 ["300gr", 35.50, 10, "2025-12-01", "Proveedor A"],
# #                 ["1kg", 50.25, 25, "2024-07-15", "Proveedor B"],
# #                 ["500ml", 12.00, 100, "2026-03-30", "Proveedor C"],
# #             ],
# #             #on_item_selected=self.update_buttons,  # Llamada al actualizar la selección

# #         )
# #         self.add_button = IconButton(
# #             icon=icons.ADD,
# #             tooltip="Añadir",
# #             on_click=lambda e: self.add_item(),
# #         )
# #         self.edit_button = IconButton(
# #             icon=icons.EDIT,
# #             tooltip="Editar",
# #             on_click=lambda e: self.edit_item(),
# #             disabled=True,  # Deshabilitado por defecto
# #         )
# #         self.delete_button = IconButton(
# #             icon=icons.DELETE,
# #             tooltip="Eliminar",
# #             on_click=lambda e: self.delete_item(),
# #             disabled=True,  # Deshabilitado por defecto
# #         )
# #         self.buttons = Column(
# #             controls=[self.add_button, self.edit_button, self.delete_button])

# #         self.table_widget = Row(
# #             scroll=ScrollMode.HIDDEN,

# #             controls=[
# #                 Row(
# #                     controls=[
# #                         self.table.build(),
# #                         #self.buttons,
# #                     ]
# #                 )

# #             ]
# #         )

# #     def build(self):

# #         return Container(
# #             padding=10,
# #             expand=True,
# #             content=Column(
# #                 controls=[
# #                     self.table_widget,
# #                 ]
# #             )
# #         )


# def main(page: Page):
#     page.title = "AlertDialog examples"
#     page.window.maximized = False
#     page.window.height =800
#     page.horizontal_alignment = CrossAxisAlignment.CENTER
#     page.bgcolor = "#a1a1a1"
#     data = [
#         {"nombre": "Manzanas", "ref": "PROD-000001",
#             "precio": 41.16, "stock": 245, "unidad": "cm3"},
#         {"nombre": "Leche", "ref": "PROD-000002",
#             "precio": 33.08, "stock": 403, "unidad": "unidades"},
#         {"nombre": "Pan", "ref": "PROD-000003", "precio": 97.94,
#             "stock": 234, "unidad": "kilogramos"},
#         {"nombre": "Huevos", "ref": "PROD-000004",
#             "precio": 70.69, "stock": 264, "unidad": "kilogramos"},
#         {"nombre": "Arroz", "ref": "PROD-000005",
#             "precio": 34.59, "stock": 37, "unidad": "litros"},
#         {"nombre": "Frijoles", "ref": "PROD-000006",
#             "precio": 5.9, "stock": 173, "unidad": "unidades"},
#         {"nombre": "Harina", "ref": "PROD-000007",
#             "precio": 89.24, "stock": 286, "unidad": "gramos"},
#         {"nombre": "Azúcar", "ref": "PROD-000008",
#             "precio": 65.88, "stock": 273, "unidad": "litros"},
#         {"nombre": "Sal", "ref": "PROD-000009",
#             "precio": 13.79, "stock": 284, "unidad": "gramos"},
#         {"nombre": "Aceite", "ref": "PROD-000010",
#             "precio": 31.76, "stock": 225, "unidad": "cm3"},
#         {"nombre": "Carne de Res", "ref": "PROD-000011",
#             "precio": 61.2, "stock": 191, "unidad": "gramos"},
#         {"nombre": "Pescado", "ref": "PROD-000012",
#             "precio": 86.14, "stock": 61, "unidad": "kilogramos"},
#         {"nombre": "Pollo", "ref": "PROD-000013",
#             "precio": 91.71, "stock": 430, "unidad": "cm3"},
#         {"nombre": "Queso", "ref": "PROD-000014", "precio": 99.83,
#             "stock": 348, "unidad": "kilogramos"},
#         {"nombre": "Yogur", "ref": "PROD-000015",
#             "precio": 21.46, "stock": 351, "unidad": "unidades"},
#         {"nombre": "Café", "ref": "PROD-000016",
#             "precio": 54.04, "stock": 51, "unidad": "unidades"},
#         {"nombre": "Té", "ref": "PROD-000017",
#             "precio": 16.14, "stock": 153, "unidad": "litros"},
#         {"nombre": "Cereal", "ref": "PROD-000018",
#             "precio": 40.67, "stock": 345, "unidad": "unidades"},
#         {"nombre": "Jugo de Naranja", "ref": "PROD-000019",
#             "precio": 59.15, "stock": 257, "unidad": "litros"},
#         {"nombre": "Chocolate", "ref": "PROD-000020",
#             "precio": 2.38, "stock": 426, "unidad": "cm3"}
#     ]

#     dlg = ProductoItemInventory(data[0],page)

#     page.add(
#         dlg.build()
#     )


# app(main)

# # def main(page=Page):
# #     def suma(a, b):
# #         return a + b

# #     def multiplicacion(a, b):
# #         return a * b

# #     columns = ["ID", "Nombre", "Cantidad", "Precio"]
# #     data = [
# #         [1, "Manzana", 10, 2.5],
# #         [2, "Pera", 5, 3.0],
# #         [3, "Banana", 8, 1.2]
# #     ]

# #     computed_column = {
# #         "name": "Total",
# #         "operation": multiplicacion,
# #         "columns": [2, 3]  # Índices de las columnas 'Cantidad' y 'Precio'
# #     }

# #     def on_item_selected(item):
# #         print(f"Seleccionado: {item}")

# #     table = CustomDataTableEdit(columns, data, on_item_selected, editable_columns=[2, 3], computed_column=computed_column)

# #     # Construir tabla
# #     page.add(table.build())

# # app(main)


# # from flet import Page, Row, Container, colors, alignment, Text

# # def main(page: Page):
# #     page.title = "Row with Horizontal Scroll"
# #     page.horizontal_alignment = "center"
# #     page.vertical_alignment = "center"

# #     # Contenedor desplazable con una fila dentro
# #     scrollable_container = Container(
# #         content=Row(
# #             scroll=ScrollMode.ALWAYS,
# #             controls=[
# #                 Container(
# #                     content=Text(f"Item {i + 1}", color=colors.WHITE),
# #                     width=150,
# #                     height=150,
# #                     bgcolor=colors.BLUE if i % 2 == 0 else colors.GREEN,
# #                     alignment=alignment.center,
# #                     border_radius=8,
# #                 )
# #                 for i in range(20)  # Crear 20 elementos en la fila
# #             ],
# #             spacing=10,
# #             alignment="start",
# #         ),
# #         width=600,  # Ancho del contenedor visible
# #         height=200,  # Alto del contenedor visible

# #     )

# #     # Añadir el contenedor desplazable a la página
# #     page.add(scrollable_container)

# # app(main)


from flet import *
import time

from app.components.billing.deal_list_item import DealListItem
from app.components.products.product_colunm_scroll import BillingSelectProductItem, ProductScrollRow
from app.components.text_field import SearchTextFieldCustom2


class Line(Container):
    def __init__(self, width=None, height=None, page=None):
        super().__init__()
        self.page = page
        self.width = width
        self.height = height if height is not None else 10
        self.progress_width = 0  # Ancho inicial del progreso

        # Barra de progreso
        self.progress_bar = Container(
            width=self.progress_width,
            height=self.height,
            bgcolor="#00FF00",
            animate=animation.Animation(500, "ease_out"),  # Animación de 500ms
        )

        # Contenedor general
        self.content = Container(
            width=self.width,
            bgcolor=Colors.GREY_400,
            height=self.height,
            expand=True if self.width is None else False,
            expand_loose=True,
            alignment=alignment.center_left,
            content=Stack(
                controls=[
                    self.progress_bar  # Barra de progreso
                ],  # Siempre comienza desde la izquierda
            ),
        )

    def build(self):
        return self.content

    def next(self):
        for i in range(11):  # Incrementar de 0 a 1 en pasos
            self.update_progress(i / 10)

    def back(self):
        for i in range(11):  # Incrementar de 0 a 1 en pasos
            self.update_progress(1-(i / 10))

    def update_progress(self, progress: float):
        """
        Actualiza el progreso de la barra.
        :param progress: Un valor entre 0.0 y 1.0 representando el porcentaje.
        """
        self.progress_width = (
            self.content.width or self.page.window.width) * progress
        self.progress_bar.width = self.progress_width  # Actualizar ancho
        self.progress_bar.update()


class Circle(Container):
    def __init__(self, size=None, page=None, text="", text_size=12, inited=False):
        super().__init__()
        self.page = page
        self.width = size
        self.height = size
        self.text = text
        self.text_size = text_size
        self.progress_width = 0  # Ancho inicial del progreso
        # Barra de progreso
        self.progress_bar = Container(
            width=self.progress_width,
            height=self.height,
            bgcolor="0x00ff00",

            animate=animation.Animation(500, "ease_out"),  # Animación de 500ms
        )
        # Contenedor general
        self.content = Container(
            width=self.width,
            bgcolor=Colors.GREY_400,
            height=self.height,
            expand=False,
            expand_loose=True,
            border_radius=self.width/2,
            alignment=alignment.center_left,
            content=Stack(
                controls=[
                    self.progress_bar,  # Barra de progreso
                    Container(
                        width=self.width,
                        alignment=alignment.center,
                        height=self.height,
                        padding=0,
                        content=Text(self.text, weight=FontWeight.BOLD, size=self.text_size),)
                ],  # Siempre comienza desde la izquierda
            ),
        )
        if inited:
            self.progress_bar.width = self.width

    def build(self):
        return self.content

    def next(self):
        for i in range(11):  # Incrementar de 0 a 1 en pasos
            self.update_progress(i / 10)

    def back(self):
        for i in range(11):  # Incrementar de 0 a 1 en pasos
            self.update_progress(1-(i / 10))

    def update_progress(self, progress: float):
        """
        Actualiza el progreso de la barra.
        :param progress: Un valor entre 0.0 y 1.0 representando el porcentaje.
        """
        self.progress_width = (
            self.content.width or self.page.window.width) * progress
        self.progress_bar.width = self.progress_width  # Actualizar ancho
        self.progress_bar.update()


class BillingSelectProductView(Container):
    def __init__(self, page=Page):
        super().__init__()
        self.page = page
        self.search_text_field = SearchTextFieldCustom2(
            hint_text="Buscar Producto por nombre o referencia...", on_change=lambda e: ())
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
        self.list_products = ProductScrollRow(data, page, self.item_acction)
        self.list_details = BillingSelectProductList(page,self.item_remove)

    def item_remove(self,ref):
        for product in self.list_products.items:
            if product.data['ref'] == ref['ref']:
                product.return_data()
                product.update()
                break

    def item_acction(self, data):
        self.list_details.add_item_widget(data)
        self.update()

    def build(self):
        return Container(
            expand=1,
            bgcolor="blue",
            content=Column(
                scroll=ScrollMode.ALWAYS,
                expand_loose=True,
                controls=[
                    Container(
                        expand=1,
                        padding=20,
                        bgcolor="yellow",
                        content=self.search_text_field,
                    ),
                    Container(
                        padding=5,
                        expand=5,
                        bgcolor="red",
                        content=self.list_products.build(),
                    ),
                    Container(
                        expand=5,
                        bgcolor="blue",
                        content=self.list_details.build(),
                    )
                ]
            ),
            #animate_position=animation.Animation(500, "ease_out")
        )


class BillingSelectProductList(Container):
    def __init__(self, page=Page, delete_action=None):
        super().__init__()
        # self.inventoryInstance = Inventory()
        self.page = page
        self.delete_action = delete_action
        self.items = []
        self.shadow_color = Colors.RED_300
        # self.item_select = ItemViewSelect(data={}, page=self.page,)
        self.item_select_data = None
        self.listItemsWidget = []
        self.content = Container(
            padding=0,
            expand=1,
            # border=Border(left=BorderSide(1,Colors.BLACK)),
            content=Column(
                expand=1,
                scroll=ScrollMode.ALWAYS,
                controls=[item.build() for item in self.listItemsWidget] if len(
                    self.listItemsWidget) != 0 else [],
            )
        )

    def add_item_widget(self, data):
        self.listItemsWidget.append(
            BillingSelectProductListItem(data, self.page,self.delete_action))
        self.content.content.controls = [
            item.build() for item in self.listItemsWidget]
        self.content.update()
        print(len(self.listItemsWidget))

    def select_item(self, data):
        self.item_select_data = data
        # self.item_select.set_data(data)

    def build(self):
        return self.content


class BillingSelectProductListItem(Container):
    def __init__(self, data=None, page=Page,action=None):
        super().__init__()
        self.page = page
        self. data = data
        self.action = action
        self.count = 1
        self.count_text = Text(self.count, weight=FontWeight.BOLD, size=18)
        self.total_text = Text(
            f"$ {self.data['precio']}", weight=FontWeight.BOLD, size=18)

    def less(self, e):
        if self.count > 1:
            self.count -= 1
            self.count_text.value = self.count
            self.total_text.value = f"$ {round((self.data['precio']*self.count),2)}"
            self.count_text.update()
            self.total_text.update()

    def more(self, e):
        self.count += 1
        self.count_text.value = self.count
        self.total_text.value = f"$ {round((self.data['precio']*self.count),2)}"
        self.count_text.update()
        self.total_text.update()

    def delete(self,e,data):
        if self.action:
            self.action(data)

    def build(self):
        return Container(
            padding=10,
            margin=10,
            bgcolor=Colors.RED_400,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                Image(
                                    "static/images/helado.jpg",
                                    width=75,
                                    height=75,
                                    fit=ImageFit.COVER,
                                    border_radius=10
                                ),
                                Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.START,
                                    spacing=0,
                                    controls=[
                                        Text(
                                            self.data['nombre'], weight=FontWeight.BOLD, size=16),
                                        Text(
                                            self.data['ref'], weight=FontWeight.BOLD, size=10),

                                    ]
                                )
                            ]
                        )
                    ),
                    Container(
                        
                        content=Row(
                            spacing=25,
                            controls=[
                                Container(
                                    content=Row(
                                        spacing=10,
                                        controls=[
                                            IconButton(
                                                Icons.EXPOSURE_MINUS_1_SHARP,
                                                on_click=self.less,
                                                icon_size=15
                                            ),
                                            self.count_text,
                                            IconButton(
                                                Icons.EXPOSURE_PLUS_1_SHARP,
                                                on_click=self.more,
                                                icon_size=15,
                                            )
                                        ]
                                    )
                                ),
                                self.total_text,
                                IconButton(
                                    Icons.CLOSE_SHARP,
                                    on_click=lambda e:self.delete(e,self.data),
                                    icon_size=15,
                                )
                            ]
                        )
                    ),
                ]
            )
        )






class Stepper(Container):
    def __init__(self, page=Page, content=None, titles=[],):
        super().__init__()
        self.index_step = 1
        self.titles = titles
        self.step1 = Circle(30, page, "1", inited=True)
        self.way1 = Line(page=page, width=300)
        self.step2 = Circle(30, page, "2")
        self.way2 = Line(page=page, width=300)
        self.step3 = Circle(30, page, "3")
        self.button_next = ElevatedButton(
            "siguiente", on_click=lambda e: self.Next(), style=ButtonStyle(shape=RoundedRectangleBorder(5)))
        self.button_back = ElevatedButton(
            "Volver", on_click=lambda e: self.Back(), style=ButtonStyle(shape=RoundedRectangleBorder(5)))
        self.title = Text(
            "texto decripcion",
            weight=FontWeight.BOLD,
            size=25,
            opacity=1,
            animate_opacity=animation.Animation(500, "ease_out"),
        ) if len(self.titles) == 0 else Text(
            self.titles[self.index_step-1],
            weight=FontWeight.BOLD, size=25,
            opacity=1,
            animate_opacity=animation.Animation(500, "ease_out"),
        )
        self.widgets=content
        # self.stepper_content =
        # self.stepper_content = Container(
        #     expand=1,
        #     content=Stack(
        #         expand=1,
        #         controls=self.widgets
                
        #     )
        # )
        self.stepper = Container(
            expand=True,
            content=Column(
                controls=[
                    Container(
                        expand=1,
                        bgcolor="#FF0000",
                        content=Column(
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                self.title,
                                Container(
                                    bgcolor="#FFFF00",
                                    content=Row(
                                        alignment=MainAxisAlignment.CENTER,
                                        expand_loose=True,
                                        controls=[
                                            self.step1,
                                            self.way1,
                                            self.step2,
                                            self.way2,
                                            self.step3
                                        ]
                                    ))
                            ]
                        )
                    ),
                    Container(
                        expand=6,
                        bgcolor="#ffffff",
                        border_radius=15,
                        shadow=BoxShadow(1.5, 10, "0x7f7f7f", (2, 5)),
                        content=Container() if self.widgets is None else Stack(controls=self.widgets,expand_loose=True,expand=6),

                    ),
                    Container(
                        expand=1,
                        bgcolor="#0000FF",
                        padding=padding.symmetric(0, 10),
                        content=Row(
                            expand=1,
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                self.button_back, self.button_next,
                            ])
                    ),
                ]
            )
        )
   
    def Next(self):
        if self.index_step == 1:
            self.way1.next()
            self.update_text(self.titles[self.index_step])
            time.sleep(.5)
            self.step2.next()

            # añadir la logica para cambiar el contenido del paso
        elif self.index_step == 2:
            self.way2.next()
            self.update_text(self.titles[self.index_step])
            time.sleep(.5)
            self.step3.next()

            # añadir la logica para cambiar el contenido del paso
        elif self.index_step == 3:
            # añadir la logica para cambiar el contenido del paso
            pass
        else:
            pass
        if self.index_step < 3:
            self.index_step += 1

    def update_text(self, new_text):
        """
        Actualiza el texto con animación.
        :param new_text: Nuevo contenido para el texto.
        """
        self.text_value = new_text
        self.title.opacity = 0
        self.title.update()
        time.sleep(.6)
        self.title.value = self.text_value
        self.title.opacity = 1
        self.title.update()

    def Back(self):
        if self.index_step == 3:
            self.step3.back()
            time.sleep(.5)
            self.update_text(self.titles[self.index_step-2])

            self.way2.back()

            # añadir la logica para cambiar el contenido del paso

        elif self.index_step == 2:
            self.step2.back()
            time.sleep(.5)
            self.update_text(self.titles[self.index_step-2])

            self.way1.back()

            # añadir la logica para cambiar el contenido del paso
        elif self.index_step == 1:
            # añadir la logica para cambiar el contenido del paso
            pass
        else:
            pass
        if self.index_step > 1:
            self.index_step -= 1

    def build(self):
        return self.stepper


def main(page: Page):
    page.window.width = 1300
    page.window.height = 750
    # Crear una barra de carga personalizada
    # line_widget = Line(page=page)
    # circle_widget = CircleProgress(100,page)
    # # Actualizar el ancho del componente en tiempo real
    # def on_resize(e):
    #     line_widget.content.width = page.window.width - 40  # Ajustar al tamaño de la ventana
    #     line_widget.content.update()

    # page.on_resize = on_resize

    # # Evento para iniciar la animación
    # def start_animation(e):
    #     for i in range(11):  # Incrementar de 0 a 1 en pasos
    #         circle_widget.update_progress(i / 10)
    #     time.sleep(.5)
    #     for i in range(11):  # Incrementar de 0 a 1 en pasos
    #         line_widget.update_progress(i / 10)

    # def start_animation2(e):
    #     for i in range(11):  # Incrementar de 0 a 1 en pasos
    #         line_widget.update_progress(1-(i / 10))
    #     time.sleep(.5)
    #     for i in range(11):  # Incrementar de 0 a 1 en pasos
    #         circle_widget.update_progress(1-(i / 10))

    # # Botón para iniciar la carga
    # button = ElevatedButton("siguiente", on_click=start_animation)
    # button2 = ElevatedButton("anterior", on_click=start_animation2)
    #Configurar la página
    titles = ["Selección de Productos",
              "Datos del Cliente", "Opciones de Facturacion"]
    # product=BillingSelectProductView(page=page)
    # product.left=0,
    # client=BillingSelectProductView(page=page)
    # client.left=page.window.width,
    # deal=client=BillingSelectProductView(page=page)
    # deal.left=page.window.width*2
    #content = [product.build(),client.build(),deal.build()]
    
    product=Container(
        bg
    )
    product.left=0,
    client=BillingSelectProductView(page=page)
    client.left=page.window.width,
    deal=client=BillingSelectProductView(page=page)
    deal.left=page.window.width*2
    content = [product.build(),client.build(),deal.build()]
    
    
    page.add(
        Stepper(page=page, titles=titles, content=content).build()
    )
    # def returnButton(e):
    #     item.return_data()
    # item =BillingSelectProductItem(data={"nombre": "Manzanas", "ref": "PROD-000001",
    #          "precio": 41.16, "stock": 245, "unidad": "cm3"},page=page)
    
    # button=ElevatedButton("return", on_click=lambda e: returnButton(e))
    
    
    
    # page.add(
    #     item.build(),button
    # )


# Ejecutar la aplicación
if __name__ == "__main__":
    app(target=main)



# from flet import *


# class SlideAnimation(Container):
#     def __init__(self, page):
#         super().__init__()
#         self.page = page
#         self.index_step = 0  # Índice actual de la lista

#         # Crear los widgets (contenedores de colores) que ocupan todo el tamaño disponible
#         self.widgets = [
#             Container(
#                 bgcolor="red",
#                 expand=1,
#                 left=0,
#                 content=Text("x"),
#                 alignment=alignment.center,
#                 animate_position=animation.Animation(500, "ease_out"),
#             ),
#             Container(
#                 bgcolor="green",
#                 expand=1,
#                 left=self.page.width, 
#                 # content=Text("x",expand=1),# Posicionado fuera del área visible
#                 # alignment=alignment.center,
#                 animate_position=animation.Animation(500, "ease_out"),
#             ),
#             Container(
#                 bgcolor="blue",
#                 expand=1,
#                 content=Text("x"),
#                 alignment=alignment.center,
#                 left=self.page.width * 2,  # Posicionado fuera del área visible
#                 animate_position=animation.Animation(500, "ease_out"),
#             ),
#         ]

#         # Stack para manejar los widgets
#         self.stack = Stack(
#             controls=self.widgets,
#             fit= StackFit.LOOSE,
#             expand=1,  # El Stack ocupa todo el espacio disponible
#         )

#         # Botón para cambiar al siguiente widget
#         self.next_button = ElevatedButton(
#             "Siguiente",
#             on_click=self.slide_next,
#         )

#         # Agregar contenido al contenedor principal
#         self.content = Container(
#             expand=1,
#             bgcolor="0xa1a1a1",
#             content=Column(
#             controls=[
#                 Container(
#                     expand=1,
#                     bgcolor="0xffa1a1",
#                     content=self.stack,
#                 ),
#                 self.next_button,
#             ],
#             #alignment=MainAxisAlignment.SPACE_BETWEEN,
#         )
#             )

#     def slide_next(self, e):
#         """
#         Mueve los widgets de derecha a izquierda al presionar "Siguiente".
#         """
#         print()
#         self.index_step += 1

#         # Volver al inicio si se supera el último widget
#         if self.index_step >= len(self.widgets):
#             self.index_step = 0

#         # Animar la posición de los widgets
#         for i, widget in enumerate(self.widgets):
#             widget.left = (i - self.index_step) * self.page.width  # Calcular nueva posición
#             widget.update()  # Aplicar cambios con animación


# def main(page: Page):
#     # Configurar la página para que sea expansiva
#     page.window_width = 800
#     page.window_height = 600
#     page.title = "Animación de widgets"
#     page.vertical_alignment = "center"
#     page.horizontal_alignment = "center"

#     # Crear la animación de lista deslizante
#     slide_animation = SlideAnimation(page)

#     # Agregar a la página
#     page.add(
#         Container(
#             expand=True,
#             content=slide_animation.content,
#         )
#     )


# if __name__ == "__main__":
#     app(target=main)

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



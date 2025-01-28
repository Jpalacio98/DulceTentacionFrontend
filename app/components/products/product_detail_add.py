from flet import *

from app.components.custom_data_table import CustomDataTableEdit
from app.components.dividerCustom import DivCustom
from app.components.products.insumos_row_scroll import InsumosScrollColumn
from app.components.text_field import SearchTextFieldCustom


class ProductDetail(Container):
    def __init__(self, data=None, page=Page):
        super().__init__()
        self.data = data
        self.page = page
        self.page.snack_bar = SnackBar(
            content=Text("Informatiom"),
            # remove_current_snackbar=True,
            action="Alright!",
        )
        self.insumos = InsumosScrollColumn(data=data, page=page)
        self.table = CustomDataTableEdit(
            columns=["nombre", "cantidad", "unidad", "precio"], editable_columns=[1], computed_column={
                "name": "Total",
                "operation": self.multiplication,
                # Índices de las columnas 'Cantidad' y 'Precio'
                "columns": [1, 3]
            },on_item_selected=self.on_item_selected)

        self.container = Container(
            expand=True,
            height=580,
            bgcolor="0xff3462",
            border=Border(
                left=BorderSide(1, Colors.BLACK)
            ),
            padding=Padding(20, 10, 20, 10),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    DivCustom(
                        "Componentes del producto"),
                    Container(width=1,
                              height=20),
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            Container(content=self.table.build(),expand=2),

                            Container(
                                expand=1,
                                border=Border(left=BorderSide(1, Colors.BLACK)),
                                padding=Padding(20, 0, 0, 0),
                                content=Column(
                                    spacing=0,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Text("Lista de Insumos",
                                             weight=FontWeight.BOLD, size=20),
                                        SearchTextFieldCustom(
                                            "Buscar insumo por nombre", width=250, on_change=lambda e: self.insumos.filter(e.data)),  # self.search(e.data)),
                                        Container(
                                            height=5, expand=True,),
                                        self.insumos.build(),
                                        ]
                                    )
                                )
                            ]
                        ),
                    Row(
                        expand_loose=True,
                        alignment=MainAxisAlignment.CENTER,
                        spacing=100,
                        controls=[
                            IconButton(Icons.ADD_SHARP, icon_size=40,
                                       tooltip="Añadir", on_click=lambda e: self.addInsumo()),
                            IconButton(Icons.DELETE_SHARP, icon_size=40,
                                       tooltip="Eliminar", on_click=self.delete_selected),
                        ])
                ]
            )

        )
    
    def delete_selected(self, e):
        if self.table.selected_index is not None:
            self.table.delete_item(self.table.selected_index)
        self.page.update()
    
    def on_item_selected(self, row):
        print(f"Fila seleccionada: {row}")

    def multiplication(self, a, b):
        return round(a * b,2)

    def addInsumo(self):
        if self.insumos.selet_data == None:
            snack_bar = SnackBar(content=Text(
                f"Debe selecionar un item de la lista de insumos para añadir..."), show_close_icon=True)
            self.page.open(snack_bar)
        elif self.insumos.selet_data != None:
            data = [
                self.insumos.selet_data['nombre'],
                1,
                self.insumos.selet_data['unidad'],
                float(self.insumos.selet_data['precio']),
            ]
            self.table.add_item(data)
            self.page.update()

    def deleteInsumo(self):
        if self.insumos.selet_data == None:
            snack_bar = SnackBar(content=Text(
                f"Debe selecionar un item de la tabla para eliminar..."), show_close_icon=True)
            self.page.open(snack_bar)

    def build(self):
        return self.container

from flet import *

from app.components.inventory.inventory_item import ProductoItemInventory


class ProductScrollRow(Container):
    def __init__(self, data=None, page=Page, item_acction=None):
        super().__init__()
        self.item_acction = item_acction
        self.data = data
        self.page = page
        self.selet_data = None
        self.items = []
        # if self.data is not None:
        #     self.load(self.data)
        self.container = Container(
            height=350,
            bgcolor="0x00000000",
            padding=Padding(10, 5, 10, 5),
            content=Row(
                spacing=10,
                scroll=ScrollMode.ALWAYS,
                controls=[]
            )
        )

    def load(self, data):
        self.items = [
            BillingSelectProductItem(
                    data=item, 
                    page=self.page,
                    acction=self.item_acction)
            for item in data]

    def filter(self, data):
        filter_items = []

        for item in self.items:
            if data in item.content.data['ref'] or data in item.content.data['nombre']:
                filter_items.append(item)
        self.container.content.controls.clear()
        self.container.content.controls = filter_items
        self.container.update()
        # self.page.update()

    def select(self, index):
        for item in self.items:
            if item.data == index:
                item.border_radius = 15
                item.bgcolor = '0xff9191'
                item.padding = 5
            else:
                item.border_radius = None
                item.bgcolor = None
                item.padding = Padding(5, 5, 5, 10)
            item.update()
        self.selet_data = self.data[index]
        print(self.selet_data)

    def build(self):
        # print(len(self.items))

        if self.data != None:
            self.load(self.data)
            self.container.content.controls = [item.build() for item in self.items]
            self.container.col = (len(self.items)//2)+1
            return self.container
        else:
            return Container(
                expand=True,
                content=Text("sin invenario\no\ninventario no cargado",
                             weight=FontWeight.BOLD, size=40, text_align="center")
            )


class BillingSelectProductItem(Card):
    def __init__(self, data={}, page=Page,acction=None):
        super().__init__()
        self.page = page
        self.page = page
        self.acction = acction
        self.data = {
            "nombre": data.get("nombre", "Sin nombre") if data.get("nombre") else "Sin nombre",
            "ref": data.get("ref", "PROD-XXXXXX") if data.get("ref") else "PROD-XXXXXX",
            "precio": data.get("precio", 0.0) if isinstance(data.get("precio"), (int, float)) else 0.0,
            "stock": data.get("stock", 0) if isinstance(data.get("stock"), int) else 0,
            "unidad": data.get("unidad", "unidades") if data.get("unidad") else "unidades"
        }
        self.button= SelectProductButton(page=Page, on_click=self.clicked_button,data=self.data)

    def clicked_button(self,data):
        if self.acction:
            self.acction(data)
    
    def return_data(self):
        self.button.retunr_add()
    
    def build(self):
        return Card(
            width=250,
            height=300,
            data=self.data,
            margin=0,
            content=Container(
                expand=True,
                bgcolor=Colors.RED_200,
                border_radius=10,
                content=Column(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Container(
                            width=250,
                            height=150,
                            bgcolor="0x00000000",
                            border_radius=10,
                            alignment=alignment.center,
                            padding=5,
                            content=Image(
                                "static/images/helado.png",
                                expand=1,
                                width=250,
                                height=150,
                                fit=ImageFit.CONTAIN,
                                border_radius=10),
                        ),
                        Container(
                            bgcolor="0x550f0f0f",
                            padding=padding.symmetric(10,10),
                            content=Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(
                                        content=Column(
                                            spacing=0,
                                            controls=[
                                                Container(
                                                    content=Text(
                                                        self.data['nombre'],
                                                        size=18,
                                                        weight=FontWeight.BOLD,
                                                        color= Colors.WHITE,
                                                        
                                                    ),
                                                ),
                                                Container(
                                                    content=Text(
                                                        f"Ref: {self.data['ref']}",
                                                        size=10,
                                                        weight=FontWeight.BOLD,
                                                        color= Colors.WHITE,
                                                    ),
                                                ),
                                                Container(
                                                    width=1,height=10),
                                                Container(
                                                    content=Text(
                                                        f"$ { self.data['precio']}",
                                                        size=18,
                                                        weight=FontWeight.NORMAL,
                                                        color="0xd91e2e",
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                    self.button.build(),
                                ]
                            )
                        ),
                    ]
                )
            )
        )


class SelectProductButton(IconButton):
    def __init__(self, on_click=None,data=None, page=Page):
        super().__init__()
        self.data = data
        self.acction = on_click
        self.icon_button = IconButton(
            icon=Icons.ADD_SHARP,
            tooltip="Agregar",
            icon_size=35,
            on_click=lambda e: self.acction_button()
        )

    def retunr_add(self):
        self.icon_button.icon = Icons.ADD_SHARP
        self.icon_button.tooltip = "Agregar"
        self.icon_button.update()
    
    def acction_button(self):
        if self.acction:
            self.acction(self.data)
        self.icon_button.icon = Icons.DONE_SHARP
        self.icon_button.tooltip = "Agregado"
        self.icon_button.update()

    def build(self):
        return self.icon_button

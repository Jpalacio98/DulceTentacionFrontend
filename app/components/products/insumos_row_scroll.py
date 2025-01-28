from flet import *

from app.components.inventory.inventory_item import ProductoItemInventory



class InsumosScrollColumn(Container):
    def __init__(self, data=None, page=Page):
        super().__init__()
        self.data = data
        self.page = page
        self.selet_data = None
        self.items = []
        # if self.data is not None:
        #     self.load(self.data)
        self.container = Container(
            bgcolor=Colors.BLACK,
            padding=Padding(10, 10, 10, 5),
            content=Column(
                height=300,
                
                spacing=10,
                scroll=ScrollMode.ALWAYS,
                controls=self.items
            )
        )

    def load(self, data):
        self.items = [
            Container(
                padding=Padding(5, 5,5, 10),
                content=ProductoItemInventory(data=item, page=self.page).build(),
                ink=True, ink_color="0xff3462",
                data=index,
                on_click=lambda e, index=index: self.select(index),
            )
            for index, item in enumerate(data)]

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
                item.padding = Padding(5, 5,5, 10)
            item.update()
        self.selet_data = self.data[index]
        print(self.selet_data)

    def build(self):
        # print(len(self.items))

        if self.data != None:
            self.load(self.data)
            self.container.content.controls = self.items
            self.container.col=(len(self.items)//2)+1
            return self.container
        else:
            return Container(
                expand=True,
                content=Text("sin invenario\no\ninventario no cargado",
                             weight=FontWeight.BOLD, size=40, text_align="center")
            )
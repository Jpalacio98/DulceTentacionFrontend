from flet import *


class ItemInventory(Card):
    def __init__(self, data, page=Page):
        super().__init__()
        self.page = page
        self.data = {
            "nombre": data.get("nombre", "Sin nombre") if data.get("nombre") else "Sin nombre",
            "ref": data.get("ref", "PROD-XXXXXX") if data.get("ref") else "PROD-XXXXXX",
            "precio": data.get("precio", 0.0) if isinstance(data.get("precio"), (int, float)) else 0.0,
            "stock": data.get("stock", 0) if isinstance(data.get("stock"), int) else 0,
            "unidad": data.get("unidad", "unidades") if data.get("unidad") else "unidades"
        }

    def build(self):
        return Card(
            width=200,
            # margin=0,
            data=self.data,
            height=300,
            content=Container(
                width=200,
                height=300,
                expand=True,
                alignment=Alignment(0, 0),
                content=Stack(
                    alignment=Alignment(0, 0),
                    controls=[
                        Image(
                            "static/images/helado.png",
                            width=200,
                            height=300,
                            fit=ImageFit.COVER,
                            border_radius=10),
                        Container(
                            bgcolor="#50D91E2E",
                            padding=10,
                            border_radius=BorderRadius(15, 0, 15, 0),
                            content=Text(
                                self.data['ref'], weight=FontWeight.BOLD),
                            offset=Offset(.25, -2.5),
                            width=128,
                        ),
                        Container(
                            height=55,
                            bgcolor="#50D91E2E",
                            border_radius=BorderRadius(0, 0, 10, 10),
                            alignment=Alignment(0, 0),
                            offset=Offset(0, 2.15),
                            content=Stack(
                                alignment=Alignment(0, 0),
                                controls=[
                                    Container(content=Text(
                                        self.data['nombre'], size=18, weight=FontWeight.BOLD), alignment=Alignment(-.8, -.9)),
                                    Container(content=Text(
                                        f"Precio:{ self.data['precio']}", size=10, weight=FontWeight.NORMAL), alignment=Alignment(-.83, .25)),
                                    Container(
                                        width=50, height=30,
                                        offset=Offset(1.2, 0),
                                        content=Column(
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            spacing=0,
                                            controls=[
                                                Text(
                                                    self.data['stock'],
                                                    size=10,
                                                    weight=FontWeight.NORMAL,
                                                    expand_loose=True,
                                                    text_align=TextAlign.CENTER,
                                                ),
                                                Text(
                                                    self.data['unidad'],
                                                    size=10,
                                                    weight=FontWeight.NORMAL,
                                                    text_align=TextAlign.CENTER
                                                )
                                            ]
                                        ),

                                        expand=False, expand_loose=False,
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
        )


class ProductoItemInventory(Card):
    def __init__(self, data, page=Page):
        super().__init__()
        self.page = page
        self.data = {
            "nombre": data.get("nombre", "Sin nombre") if data.get("nombre") else "Sin nombre",
            "ref": data.get("ref", "PROD-XXXXXX") if data.get("ref") else "PROD-XXXXXX",
            "precio": data.get("precio", 0.0) if isinstance(data.get("precio"), (int, float)) else 0.0,
            "stock": data.get("stock", 0) if isinstance(data.get("stock"), int) else 0,
            "unidad": data.get("unidad", "unidades") if data.get("unidad") else "unidades"
        }

    def build(self):
        return Card(
            width=90,
            # margin=0,
            data=self.data,
            height=180,
            content=Container(
                width=90,
                height=180,
                expand=True,
                alignment=Alignment(0, 0),
                content=Stack(
                    alignment=Alignment(0, 0),
                    controls=[
                        Image(
                            "static/images/helado.png",
                            width=90,
                            height=180,
                            fit=ImageFit.COVER,
                            border_radius=10),
                        Container(
                            bgcolor="#50D91E2E",
                            padding=5,
                            border_radius=BorderRadius(5, 0, 5, 0),
                            content=Text(
                                self.data['ref'], weight=FontWeight.BOLD,size=6),
                            offset=Offset(.245, -3.5),
                            width=55,
                        ),
                        Container(
                            height=35,
                            bgcolor="#50D91E2E",
                            border_radius=BorderRadius(0, 0, 10, 10),
                            alignment=Alignment(0, 0),
                            offset=Offset(0, 1.96),
                            content=Stack(
                                alignment=Alignment(0, 0),
                                controls=[
                                    Container(content=Text(
                                        self.data['nombre'], size=10, weight=FontWeight.BOLD), alignment=Alignment(-.8, -.9)),
                                    Container(content=Text(
                                        f"Precio:{ self.data['precio']}", size=8, weight=FontWeight.NORMAL), alignment=Alignment(-.83, .25)),
                                   
                                ]
                            )
                        )
                    ]
                )
            )
        )


from flet import *


class ReplenishItemInventory(Card):
    def __init__(self, data, page=Page, on_select=None):
        super().__init__()
        self.page = page
        self.data = {
            "nombre": data.get("nombre", "Sin nombre") if data.get("nombre") else "Sin nombre",
            "ref": data.get("ref", "PROD-XXXXXX") if data.get("ref") else "PROD-XXXXXX",
            "precio": data.get("precio", 0.0) if isinstance(data.get("precio"), (int, float)) else 0.0,
            "stock": data.get("stock", 0) if isinstance(data.get("stock"), int) else 0,
            "unidad": data.get("unidad", "unidades") if data.get("unidad") else "unidades"
        }
        self.on_select = on_select
        
    def selected(self):
        if self.on_select:
            self.on_select(self.data)
            print(self.data)

    def build(self):
        return Card(
            margin=Margin(5, 5, 30, 5),
            width=400,
            elevation=5,
            expand=True,
            color=Colors.RED_200,
            content=Container(
                width=400,
                padding=5,
                expand=True,
                content=ListTile(
                    bgcolor=Colors.RED_200,
                    content_padding=0,
                    leading=Image(
                        "static/images/helado.png",
                        width=50,
                        height=50,
                        fit=ImageFit.COVER,
                        border_radius=10
                    ),
                    title=Text(
                        self.data['nombre'],weight=FontWeight.BOLD),
                    subtitle=Text(self.data['ref']),
                    trailing=IconButton(
                        Icons.ARROW_RIGHT_ALT_SHARP, icon_size=30,on_click=lambda x: self.selected()),
                    width=400
                )
            )
        )

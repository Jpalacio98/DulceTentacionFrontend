from flet import *

class ViewItemInventory(AlertDialog):
    def __init__(self, data,page=Page):
        super().__init__()
        self.page = page
        self.title = Text(f"{data['nombre']}")
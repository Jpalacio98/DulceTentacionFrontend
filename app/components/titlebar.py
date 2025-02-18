from flet import *
from app.utils.color_schema import *

class TitleBar(Container):
    def __init__(self, page=Page):
        super().__init__()
        self.page = page
        self.page.is_maximized = True
        self.max_button = IconButton(
            content=Image(src="static/icons/restore.png", width=20, height=20),
            tooltip="Maximizar", on_click=lambda x: self.on_max_click(),bgcolor=color_h1a
        )
        self.min_button = IconButton(
            content=Image(src="static/icons/minimize.png",
                          width=20, height=20),
            tooltip="Minimizar", on_click=lambda x: self.on_min_click(),bgcolor=color_h1a
        )
        self.close_button = IconButton(
            content=Image(src="static/icons/close.png", width=20, height=20),
            tooltip="Cerrar", on_click=lambda x: self.on_close_click(),bgcolor=color_h1a
        )

    def on_close_click(self):
        self.page.window.close()

    def on_max_click(self):
        if self.page.is_maximized:
            # Restaurar la ventana a un tamaño específico
            self.page.window.center()
            self.max_button.content = Image(
                src="static/icons/maximize.png", width=20, height=20)
            self.max_button.tooltip = "Restaurar"
            self.page.window.maximized = False
            self.page.is_maximized = False
        else:
            # Maximizar la ventana
            self.max_button.content = Image(
                src="static/icons/restore.png", width=20, height=20)
            self.max_button.tooltip = "Restaurar"
            self.page.window.maximized = True
            self.page.is_maximized = True
        self.page.update()

    def on_min_click(self):
        self.page.window.minimized = True
        self.page.update()

    def build(self):
        return Container(
            padding=Padding(20, 0, 5, 0),
            bgcolor=bg_color_2,
            height=50,
            content=Row(
                [
                    Image(src="static/images/logo.png", width=50, height=60),
                    WindowDragArea(
                        Container(bgcolor=Colors.TRANSPARENT, padding=10),
                        expand=True,
                    ),
                    self.min_button,
                    self.max_button,
                    self.close_button,
                ], alignment=alignment.center,
            ),
        )

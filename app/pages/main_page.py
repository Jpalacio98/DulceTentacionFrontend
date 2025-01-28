from flet import *


from app.components.menu import menu
from app.components.titlebar import titlebar
from app.pages.views.bill_view import bill_view
from app.pages.views.inventory_view import inventory_view
from app.pages.views.product_view import product_view
from app.pages.views.setting_view import settings_view
from app.pages.views.home_view import home_view


class MainPage(Column):
    def __init__(self, page: Page):
        self.page = page
        self.page.window.width = 600
        self.page.window.height = 400
        self.page.window.maximized = True
        self.page.window.frameless = True
        self.page.padding = 0
        self.content = self._create_content()
        self.main_view = self._create_main_view()

    def _create_content(self):
        """Crea el contenedor dinámico para las vistas"""
        return Column(
            [
                Text("Welcome to the main view!", size=24),
            ],

            #alignment=MainAxisAlignment.CENTER,
            #horizontal_alignment=CrossAxisAlignment.CENTER
        )

    def on_menu_item_click(self, item):
        """Maneja la selección del menú"""
        self.content.controls.clear()

        if item == "home":
            self.content.controls.append(home_view())
        elif item == "billing":
            self.content.controls.append(bill_view(self.page).build())
        elif item == "inventory":
            self.content.controls.append(inventory_view(self.page).build())
        elif item == "menu":
            self.content.controls.append(product_view(self.page).build())
        elif item == "settings":
            self.content.controls.append(settings_view(self.page).build())
        else:
            self.content.controls.append(
                Text(f"View: {item}", size=24)
            )

        self.content.update()

    def _create_main_view(self):
        """Crea la estructura principal de la vista"""
        return Column(
            adaptive=True,
                controls=[
                    titlebar(self.page),
                    Row(
                        [
                            menu(self.on_menu_item_click),
                            Container(
                                content=self.content,
                                expand=True,
                                padding=0,
                                bgcolor=colors.BLACK26
                            ),
                        ],
                        expand=True,
                        spacing=0,
                    ),
                ],
                expand=True,
                spacing=0,
               
            )
        

    def build(self):
        """Retorna la vista principal"""
        return self.main_view

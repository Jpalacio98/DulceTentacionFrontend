import flet as ft
from .category_card import CategoryCard


class CategoriesGrid(ft.Container):
    def __init__(self, items=None, page=ft.Page, on_delete=None, on_edit=None):
        super().__init__()
        self.page = page
        self.items = items if items else []
        self.items_count = len(self.items)
        self.cols = 4
        self.selected_item = None
        self.rows = self.items_count // self.cols
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.grid = ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            controls=[],
            spacing=10,  # Espaciado reducido
        )
        self.content = self.grid
        self.expand = True
        self.padding = ft.padding.all(10)  # Padding reducido

    def build(self):
        self.loadGrid()
        return ft.Container(
            content=self.grid, expand=True, padding=10
        )  # Padding reducido

    def loadGrid(self):
        self.grid.controls.clear()
        row_count = 0
        row_grid = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY, expand=True, spacing=10
        )  # Espaciado reducido

        for item in self.items:
            item_w = CategoryCard(
                item,
                self.page,
                on_delete=self.on_delete,
                on_edit=self.on_edit,
            )
            if row_count < self.cols:
                row_grid.controls.append(item_w.build())
                row_count += 1
            else:
                self.grid.controls.append(row_grid)
                row_grid = ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY, expand=True, spacing=10
                )
                row_grid.controls.append(item_w.build())
                row_count = 1

        if row_grid.controls:
            self.grid.controls.append(row_grid)

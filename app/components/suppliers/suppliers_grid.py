from flet import *
from app.components.suppliers.supplier_card import SupplierCard


class SuppliersGrid(Container):
    def __init__(self, items=list | None, page=Page, on_delete=None, on_edit=None):
        super().__init__()
        self.page = page
        self.items = items if items else []
        self.items_count = len(self.items)
        self.cols = 4
        self.selected_item = None
        self.rows = self.items_count // self.cols
        self.on_delete = on_delete
        self.on_edit = on_edit
        self.grid = Column(
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ScrollMode.ALWAYS,
            controls=[],
        )
        self.content = self.grid
        self.expand = True
        self.padding = padding.all(20)
        self.loadGrid()

    def build(self):
        return Container(content=self.grid, expand=True, padding=20)

    def loadGrid(self):
        self.grid.controls.clear()
        row_count = 0
        row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)

        for item in self.items:
            item_w = SupplierCard(
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
                row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)
                row_grid.controls.append(item_w.build())
                row_count = 1

        if row_grid.controls:
            self.grid.controls.append(row_grid)

    def filter(self, e):
        search = e.control.value.lower()
        filtered_items = [item for item in self.items if search in item["name"].lower()]
        self.grid.controls.clear()
        self.loadGridFilter(filtered_items)
        self.grid.update()

    def loadGridFilter(self, items):
        row_count = 0
        row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)

        for item in items:
            item_w = SupplierCard(
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
                row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)
                row_grid.controls.append(item_w.build())
                row_count = 1

        if row_grid.controls:
            self.grid.controls.append(row_grid)

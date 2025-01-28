from flet import *

from app.components.inventory.inventory_item import ItemInventory
from app.components.inventory.inventory_view_item import ViewItemInventory


class CustomGrid(Container):
    def __init__(self, items = list| None, page=Page):
        super().__init__()
        self.page = page
        self.items = items
        self.items_count = (len(items))
        self.cols = 4
        self.selected_item=None
        self.rows = self.items_count//self.cols
        self.grid = Column(
            alignment=MainAxisAlignment.START, horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ScrollMode.ALWAYS,
            controls=[
            ]
        )
        self.loadGrid()

    def build(self):
        return Container(content=self.grid, expand=True,padding=20)

    def loadGrid(self):
        row_count = 0  # Contador de columnas en la fila actual
        row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)  # Fila inicial

        for item in self.items:
            item_w = self.create_item_widget(item)  # Crear widget del elemento

            if row_count < self.cols:
                row_grid.controls.append(item_w)
                row_count += 1
                #print(f"{item['ref']} añadido...")
            else:
                self.grid.controls.append(row_grid)
                row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)
                row_grid.controls.append(item_w)
                row_count = 1

        # Agregar la última fila si tiene elementos
        if row_grid.controls:
            self.grid.controls.append(row_grid)
    
    def loadGridFilter(self,items):
        
        row_count = 0  # Contador de columnas en la fila actual
        row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)  # Fila inicial

        for item in items:
            item_w = self.create_item_widget(item)  # Crear widget del elemento

            if row_count < self.cols:
                row_grid.controls.append(item_w)
                row_count += 1
                #print(f"{item['ref']} añadido...")
            else:
                self.grid.controls.append(row_grid)
                row_grid = Row(alignment=MainAxisAlignment.SPACE_EVENLY, expand=True)
                row_grid.controls.append(item_w)
                row_count = 1

        # Agregar la última fila si tiene elementos
        if row_grid.controls:
            self.grid.controls.append(row_grid)

    def create_item_widget(self, item):
        # Crear un contenedor para cada elemento
        return Container(
            bgcolor=colors.TRANSPARENT,
            content=ItemInventory(item,self.page).build(),
            padding=10,
            border_radius=10,
            on_click=lambda e,item=item: self.select_item(item),
            on_long_press=lambda e,item=item: self.viewData(item),
            ink=True,
            ink_color=Colors.RED_300
        )

    def select_item(self, item):
        """Selecciona un único elemento de la grilla."""
        self.selected_item = item
        print(f"custom grid item selected = {item}")
        # Guardar el índice del elemento seleccionado
        self.highlight_selected_item()
        self.grid.update()# Resaltar visualmente el elemento seleccionado

    def highlight_selected_item(self):
        """Resalta el elemento seleccionado y restaura los demás."""
        for row in self.grid.controls:
            for item in row.controls:
                data = item.content.data['ref']
                print(data)
                if data is not None:
                    if data == self.selected_item['ref']:
                        item.bgcolor = colors.RED_200  # Resaltar seleccionado
                        print("resaltado")
                    else:
                        item.bgcolor = colors.TRANSPARENT  # Restaurar fondo
                        
                item.update()
        self.update()  # Actualizar la vista
        
    def delete_selected_item(self):
        """Elimina el elemento seleccionado y reorganiza la grilla."""
        if self.selected_item is not None:
            # Eliminar el elemento seleccionado de la lista
            self.items=[item for item in self.items if item["ref"] != self.selected_item['ref']]

            # Reiniciar el índice de selección
            self.selected_item = None

            # Reorganizar la grilla
            self.grid.controls.clear()
            self.loadGrid()
            self.grid.update()
    
    def filter(self,filter):
        
        
        filter_items =[]
        for item in self.items:
            if filter.data in item['ref'] or filter.data in item['nombre']:
                filter_items.append(item)
        
        print(filter_items)
        self.grid.controls.clear()
        self.loadGridFilter(filter_items)
        self.grid.update()

    def viewData(self,item):
        self.dlg = ViewItemInventory(item,self.page)
        self.page.open(self.dlg)
    

from flet import *
from app.components.custom_data_table import CustomDataTable
from app.components.inventory.bach_item import BatchForm


class BatchView(Container):
    def __init__(self, data, page=Page):
        super().__init__()
        self.page = page
        self.data = data
        self.form_visible = False
        self.selected_row = None

    def build(self):
        # Tabla personalizada
        self.table = CustomDataTable(
            columns=["ID", "Nombre", "Unidad", "Precio",
                     "Cantidad", "Fecha Vencimiento", "Proveedor"],
            data=self.data,
            on_item_selected=self.on_item_selected,
        )

        # Formulario
        self.form = BatchForm(on_save=self.save_form,
                              on_cancel=self.cancel_form,page=self.page)

        # Contenedor del formulario
        self.form_container = self.form.build()

        # Botones globales
        self.control_buttons = Row(
            [
                IconButton(Icons.ADD_SHARP,tooltip="Añadir", on_click=lambda e: self.show_form()),
                IconButton(Icons.EDIT_SHARP,tooltip="Editar", on_click=self.edit_selected),
                IconButton(Icons.DELETE_SHARP,tooltip="Eliminar", on_click=self.delete_selected),
            ],
            alignment=MainAxisAlignment.END,
        )

        return Container(
            padding=Padding(20,5,5,5),
            content=Stack(
                [
                    Column([self.control_buttons, self.table.build()],
                           expand=True),
                    self.form_container,
                ]
            ))

    # Función para mostrar el formulario
    def show_form(self, row=None):
        self.form_visible = True
        self.selected_row = row
        self.form_container.expand_loose=True
        self.form_container.offset = Offset(.5, -.4)

        if row:  # Editar
            self.form.title.value= "Editar lote"
            self.form.id_field.value = str(row[0])
            self.form.name_field.value = row[1]
            self.form.unit_field.value = str(row[2])
            self.form.price_field.value = str(row[3])
            self.form.quantity_field.value = str(row[4])
            self.form.expiry_date_field.value = row[5]
            self.form.supplier_field.value = row[6]
        else:  # Añadir
            self.form.title.value= "Añadir un lote"
            self.form.id_field.value = str(len(self.data) + 1)
            self.form.name_field.value = ""
            self.form.unit_field.value = ""
            self.form.price_field.value = ""
            self.form.quantity_field.value = ""
            self.form.expiry_date_field.value = ""
            self.form.supplier_field.value = ""

        self.page.update()

    # Función para guardar los datos del formulario
    def save_form(self, e):
        updated_row = [
            int(self.form.id_field.value),
            self.form.name_field.value,
            int(self.form.unit_field.value),
            float(self.form.price_field.value),
            int(self.form.quantity_field.value),
            self.form.expiry_date_field.value,
            self.form.supplier_field.value,
        ]

        if self.selected_row:  # Editar
            self.table.edit_item(self.table.selected_index, updated_row)
        else:  # Añadir
            self.table.add_item(updated_row)

        self.form_visible = False
        self.form_container.offset = Offset(3, 0)
        self.page.update()

    # Función para cancelar la edición
    def cancel_form(self, e):
        self.form_visible = False
        self.form_container.offset = Offset(3, 0)
        self.page.update()
    # Función para eliminar una fila
    def delete_selected(self, e):
        if self.table.selected_index is not None:
            self.table.delete_item(self.table.selected_index)
        self.page.update()

    # Función para editar la fila seleccionada
    def edit_selected(self, e):
        if self.table.selected_index is not None:
            self.show_form(self.table.data[self.table.selected_index])

    # Función llamada cuando se selecciona una fila
    def on_item_selected(self, row):
        print(f"Fila seleccionada: {row}")

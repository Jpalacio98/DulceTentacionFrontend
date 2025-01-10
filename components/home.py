import flet as ft
from datetime import datetime
import threading

# Componente para la vista Home
def home_view():
    # Actualización dinámica del reloj
    clock_text = ft.Text("", size=40, weight="bold", color="blue")
    
    def update_clock():
        while True:
            clock_text.value = datetime.now().strftime("%H:%M:%S")
            clock_text.update()
    
    threading.Thread(target=update_clock, daemon=True).start()

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Home", size=30, weight="bold"),
                ft.Image(
                    src="https://via.placeholder.com/200",  # Enlace a un logo temporal
                    width=200,
                    height=200,
                    fit="contain",
                ),
                ft.Container(
                    content=clock_text,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20),
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
        ),
        alignment=ft.alignment.center,
        padding=20,
    )

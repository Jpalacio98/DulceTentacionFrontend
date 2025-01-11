from components.button_menu import button_menu
import flet as ft


def menu(on_menu_item_click):
    def on_hover(e):
        if e.data == "true":  # Cuando el mouse está sobre el elemento
            container.width = 250  # Expandir el menú
            menu_title_text.opacity = 1  # Mostrar texto "Menu"
            menu_title_text.update()
            for button in menu_buttons:
                button.set_expanded(True)  # Expandir botones
        else:  # Cuando el mouse sale del elemento
            container.width = 70  # Contraer el menú
            menu_title_text.opacity = 0  # Ocultar texto "Menu"
            menu_title_text.update()
            for button in menu_buttons:
                button.set_expanded(False)  # Contraer botones
        container.update()  # Actualizar el contenedor

    # Lista de ítems del menú con íconos
    menu_items = [
        {"icon": "src\static\heladeria.png", "label": "Home",
            "on_click": lambda _: on_menu_item_click("home")},
        {"icon": "src\static\\vendedor.png", "label": "Settings",
            "on_click": lambda _: on_menu_item_click("settings")},
    ]

    # Crear botones del menú
    menu_buttons = [
        button_menu(item["icon"], item["label"],
                    item["on_click"], expanded=False)
        for item in menu_items
    ]

    # Título del menú con ícono y texto animado
    menu_title_text = ft.Text(
        "Menu", opacity=0, animate_opacity=300, size=20, weight="bold")
    menu_title = ft.Row(
        [
            ft.Icon(ft.icons.MENU, size=24),
            menu_title_text,
        ],
        spacing=10,
        alignment="start",
    )

    # Contenedor del menú
    container = ft.Container(
        bgcolor=ft.colors.BLACK45,
        content=ft.Column(
            [
                menu_title,
                *menu_buttons,  # Añadir botones del menú
            ],
            alignment="start",
            spacing=16,
        ),
        width=70,  # Ancho inicial (menú contraído)
        padding=16,
        on_hover=on_hover,  # Vincular el evento on_hover
        # Animación suave al cambiar el tamaño
        animate=ft.animation.Animation(500, "ease"),
    )

    return container

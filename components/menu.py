import flet as ft

def menu(on_menu_item_click):
    def on_hover(e):
        if e.data == "true":  # Cuando el mouse está sobre el elemento
            container.width = 250  # Expandir el menú
            menu_title_text.opacity = 1  # Mostrar texto "Menu"
            menu_title_text.update()
            for item in menu_items:
                item["text"].opacity = 1  # Mostrar texto de los ítems
                item["text"].update()
        else:  # Cuando el mouse sale del elemento
            container.width = 70  # Contraer el menú
            menu_title_text.opacity = 0  # Ocultar texto "Menu"
            menu_title_text.update()
            for item in menu_items:
                item["text"].opacity = 0  # Ocultar texto de los ítems
                item["text"].update()
        container.update()  # Actualizar el contenedor

    # Lista de ítems del menú con íconos
    menu_items = [
        {"icon": ft.icons.HOME, "label": "Home", "on_click": lambda _: on_menu_item_click("home")},
        {"icon": ft.icons.SETTINGS, "label": "Settings", "on_click": lambda _: on_menu_item_click("settings")},
    ]

    # Crear ítems del menú
    menu_widgets = []
    for item in menu_items:
        text_widget = ft.Text(item["label"], opacity=0, animate_opacity=300)  # Texto con animación de opacidad
        menu_widgets.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(item["icon"]),
                        text_widget,  # Añadir texto al lado del ícono
                    ],
                    spacing=10,
                    alignment="start",
                ),
                on_click=item["on_click"],
                padding=ft.padding.all(8),
            )
        )
        item["text"] = text_widget  # Guardar referencia al texto para animarlo

    # Título del menú con ícono y texto animado
    menu_title_text = ft.Text("Menu", opacity=0, animate_opacity=300, size=20, weight="bold")
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
                *menu_widgets,  # Añadir widgets del menú
            ],
            alignment="start",
            spacing=16,
        ),
        width=70,  # Ancho inicial (menú contraído)
        padding=16,
        on_hover=on_hover,  # Vincular el evento on_hover
        animate=ft.animation.Animation(500, "ease"),  # Animación suave al cambiar el tamaño
    )

    return container

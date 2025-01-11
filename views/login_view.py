import flet as ft


def login_view(page: ft.Page, switch_to_main_view):
    page.window.frameless = True  # Elimina el marco del sistema operativo
    # Fondo transparente para mostrar bordes redondeados
    page.window.bgcolor = "transparent"
    page.bgcolor = "transparent"

    def on_login_click(e):
        if username.value and password.value:
            switch_to_main_view()
        else:
            error_message.value = "Please fill in all fields."
            page.update()

    def on_close_click(e):
        page.window.close()
    # Create UI elements
    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True,
                            can_reveal_password=True, width=300)
    login_button = ft.ElevatedButton(text="Login", on_click=on_login_click)
    error_message = ft.Text(value="", color="red")
    social_login_text = ft.Text("Or login with social media:")

    google_button = ft.IconButton(
        content=ft.Image(src="src/image/google.png", width=24, height=24),
        tooltip="Login with Google"
    )
    github_button = ft.IconButton(
        content=ft.Image(src="src/image/github.png", width=24, height=24),
        tooltip="Login with GitHub"
    )
    facebook_button = ft.IconButton(
        content=ft.Image(src="src/static/bill.png", width=24, height=24),
        tooltip="Login with Facebook"
    )

    close_button = ft.IconButton(
        icon_color=ft.Colors.WHITE, icon=ft.icons.CLOSE, on_click=on_close_click)

    # Layout

    return ft.Container(border_radius=30, expand=True, bgcolor='#e3dac9', content=ft.Column(
        [

            ft.Container(
                content=ft.Column(
                        [
                            ft.Row([
                                ft.WindowDragArea(
                                    ft.Container(
                                        bgcolor=ft.Colors.TRANSPARENT,

                                        padding=10
                                    ), expand=True,
                                ), close_button
                            ]
                            ),
                            ft.Text("Login", size=24, weight="bold",
                                    text_align="center"),
                            username,
                            password,
                            login_button,
                            error_message,
                            social_login_text,
                            ft.Row([
                                google_button,
                                github_button,
                                facebook_button
                            ], alignment="center", spacing=10),
                        ],
                        alignment="center",
                        horizontal_alignment="center",
                        ),
                alignment=ft.alignment.center,
                padding=16,
                bgcolor='#e3dac9'
            )
        ]
    )

    )

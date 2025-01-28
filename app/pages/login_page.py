from flet import *
from app.components.text_field import TextFieldCustom


class LoginPage:
    def __init__(self, page=Page):
        self.page = page
        self.close_button = IconButton(
            icon_color=Colors.WHITE, icon=icons.CLOSE, on_click=lambda e: self.on_close_click())

    def on_close_click(self):
        self.page.window.close()

    def build(self):
        user =TextFieldCustom(label="usuario",hint_text="Email o nombre de usuario")
        
        password =TextFieldCustom(label="Contraseña",hint_text="Contraseña",password=True,can_reveal_password=True)
        
        def handle_login(e):
            # Lógica para validar credenciales
            self.page.go(route="/main")

        return View(
            bgcolor=Colors.TRANSPARENT,
            spacing=0,
            route="/login",
            controls=[
                Container(
                    Column(
                        [
                            Container(
                                Row(
                                    [
                                        self.close_button
                                    ],
                                    alignment="end",
                                    expand=True,
                                    height=40,
                                ),
                                
                            ),
                            Image("static/images/logo.png",width=300,height=170,fit=ImageFit.CONTAIN),
                            Container(height=35,width=1),
                            user,
                            Container(height=10,width=1),
                            password,
                            Container(height=50,width=1),
                            ElevatedButton(text="Iniciar Sesion",width=150,height=55,style=ButtonStyle(shape=RoundedRectangleBorder(10)),on_click=handle_login),
                            TextButton("¿Olvido su contraseña?"),
                            Container(height=15,width=1),
                            Image("static/images/LogoInnobyte2024SFN.png",width=100,height=100,fit=ImageFit.CONTAIN),
                        ],
                        alignment=MainAxisAlignment.START,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        expand=True
                    ), bgcolor='#ffdac9', expand=True, border_radius=15,padding=10
                )
            ],
        )

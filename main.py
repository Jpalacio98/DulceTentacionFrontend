import flet as ft
from dotenv import load_dotenv
from app.pages.login_page import LoginPage
from app.pages.main_page import MainPage

load_dotenv()
class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width =  400
        self.page.window.height = 750
        self.page.window.frameless = True
        self.page.window.bgcolor= "transparent"
        self.page.bgcolor = "transparent"
        self.page.window.center()
        self.page.padding = 0
        self.page.route = "/login"
        self.page.views.append(LoginPage(self.page).build())
        self.page.on_route_change = self.route_change

    def route_change(self, e):
        if self.page.route == "/login":
            self.page.views.clear()
            self.page.views.append(LoginPage(self.page).build())
        elif self.page.route == "/main":
            self.page.views.clear()
            self.page.views.append(MainPage(self.page).build())
            pass

    def start(self):
        self.page.go(self.page.route)

def main(page: ft.Page):
    app = App(page)
    app.start()

ft.app(target=main)

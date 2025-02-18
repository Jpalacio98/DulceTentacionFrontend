# import time
# from flet import *

# from app.components.stepper.stepper import Stepper
# from app.components.stepper.steps.clients import BillingDataClientView
# from app.components.stepper.steps.deals import BillingDealView
# from app.components.stepper.steps.products import BillingSelectProductView




# def main(page=Page):
#     page.window.width = 1300
#     page.window.height = 750
#     titles = ["Selección de Productos",
#               "Datos del Cliente", "Opciones de Facturacion"]
#     product = BillingSelectProductView(page=page)

#     client = BillingDataClientView(page=page,)
#     item3 = BillingDealView(
#         page=page,
#     )
#     content = [product.build(), client.build(), item3.build()]

#     page.add(
#         Stepper(page=page, titles=titles, content=content).build()
#     )


# if __name__ == "__main__":
#     app(target=main)


from app.models.inventory import Inventory

inv = Inventory()


print(inv.list())
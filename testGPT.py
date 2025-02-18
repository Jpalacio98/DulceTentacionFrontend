from flet import *

class User:
    def __init__(self, email=None, phone=None):
        self.email = email
        self.phone = phone

def main(page: Page):
    # Usuario de ejemplo (modificar según necesidades)
    user = User(email="usuario@ejemplo.com", phone="+573001234567")
    
    page.title = "Configuración de Facturación"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.padding = 30

    # Componentes para tipo de facturación
    billing_type = RadioGroup(
        content=Column([
            Radio(value="normal", label="Facturación Normal"),
            Radio(value="electronica", label="Facturación Electrónica")
        ]),
        value="normal"
    )

    # Componentes para métodos de pago
    payment_method = RadioGroup(
        content=Column([
            Radio(value="efectivo", label="Efectivo"),
            Radio(value="nequi", label="Nequi"),
            Radio(value="bancolombia", label="Bancolombia"),
            Radio(value="daviplata", label="DaviPlata")
        ])
    )

    # Componentes para notificaciones
    print_checkbox = Checkbox(label="Imprimir", value=False)
    email_checkbox = Checkbox(
        label="Enviar por Email",
        disabled=not bool(user.email),
        value=False
    )
    whatsapp_checkbox = Checkbox(
        label="Enviar por WhatsApp",
        disabled=not bool(user.phone),
        value=False
    )

    notifications = Column([
        Text("Métodos de notificación:"),
        print_checkbox,
        email_checkbox,
        whatsapp_checkbox
    ])

    # Crear diseño principal
    page.add(
        Column(
            [
                Text("Tipo de facturación:", weight=FontWeight.BOLD),
                billing_type,
                Divider(),
                
                Text("Métodos de pago:", weight=FontWeight.BOLD),
                payment_method,
                Divider(),
                
                Text("Notificaciones:", weight=FontWeight.BOLD),
                notifications
            ],
            spacing=20,
            width=600
        )
    )

app(target=main)
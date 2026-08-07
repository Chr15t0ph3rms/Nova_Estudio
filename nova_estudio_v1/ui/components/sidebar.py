import flet as ft

def sidebar(on_change, opciones=None):

    # Menú por defecto (administrador), usado cuando no se especifica "opciones"
    if opciones is None:
        opciones = [
            (ft.Icons.DASHBOARD, "Dashboard"),
            (ft.Icons.PEOPLE, "Clientes"),
            (ft.Icons.MUSIC_NOTE, "DJs"),
            (ft.Icons.BADGE, "Empleados"),
            (ft.Icons.EVENT, "Eventos"),
            (ft.Icons.INVENTORY, "Inventario"),
            (ft.Icons.CELEBRATION, "Paquetes"),
            (ft.Icons.DESCRIPTION, "Contratos"),
            (ft.Icons.PAYMENTS, "Pagos"),
            (ft.Icons.INSERT_CHART, "Reportes"),
            (ft.Icons.BUSINESS, "Agencia"),
        ]

    def enviar_opcion(texto):
        print("Botón presionado:", texto)
        if on_change:
            on_change(texto)

    def boton(icono, texto, color=ft.Colors.WHITE):

        return ft.Container(

            height=38,
            padding=6,
            border_radius=10,
            ink=True,

            on_click=lambda e: enviar_opcion(texto),

            content=ft.Row(
                [
                    ft.Icon(icono, color=color, size=20),
                    ft.Text(texto, color=color, size=14, weight=ft.FontWeight.W_500)
                ],
                spacing=10
            )
        )

    menu = ft.Column(
        [boton(icono, texto) for icono, texto in opciones],
        spacing=2
    )

    return ft.Container(
        width=240,
        bgcolor=ft.Colors.GREY_900,
        padding=12,

        content=ft.Column(
            [
                # LOGO PEQUEÑO
                ft.Container(
                    height=80,
                    content=ft.Image(
                        src="logo_nova.png",
                        width=120,
                        height=70,
                    )
                ),

                ft.Divider(),

                menu,

                # EMPUJA CERRAR SESIÓN ABAJO
                ft.Container(expand=True),

                ft.Divider(),

                boton(ft.Icons.LOGOUT, "Cerrar sesión", ft.Colors.RED)
            ],
            expand=True
        )
    )

import flet as ft


def sidebar(on_change):
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
                    ft.Icon(
                        icono,

                        color=color,

                        size=20
                    ),

                    ft.Text(
                        texto,

                        color=color,

                        size=14,

                        weight=ft.FontWeight.W_500
                    )
                ],

                spacing=10
            )
        )

    menu = ft.Column(
        [
            boton(
                ft.Icons.DASHBOARD,
                "Dashboard"
            ),

            boton(
                ft.Icons.PEOPLE,
                "Clientes"
            ),

            boton(
                ft.Icons.MUSIC_NOTE,
                "DJs"
            ),

            boton(
                ft.Icons.BADGE,
                "Empleados"
            ),

            boton(
                ft.Icons.EVENT,
                "Eventos"
            ),

            boton(
                ft.Icons.INVENTORY,
                "Inventario"
            ),

            boton(
                ft.Icons.CELEBRATION,
                "Paquetes"
            ),

            boton(
                ft.Icons.DESCRIPTION,
                "Contratos"
            ),

            boton(
                ft.Icons.PAYMENTS,
                "Pagos"
            ),

            boton(
                ft.Icons.INSERT_CHART,
                "Reportes"
            ),

            boton(
                ft.Icons.BUSINESS,
                "Agencia"
            )

        ],

        spacing=2
    )

    return ft.Container(
        width=240,

        bgcolor=ft.Colors.GREY_900,

        padding=12,

        content=ft.Column(
            [
                # logo pequeño

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

                # empuja cerrar sesión abajo

                ft.Container(
                    expand=True
                ),

                ft.Divider(),

                boton(
                    ft.Icons.LOGOUT,

                    "Cerrar sesión",

                    ft.Colors.RED
                )

            ],

            expand=True
        )
    )

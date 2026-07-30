import flet as ft



def sidebar(on_change):


    def enviar_opcion(texto):

        print("Botón presionado:", texto)

        if on_change:

            on_change(texto)



    def boton(icono, texto, color=ft.Colors.WHITE):

        return ft.Container(

            padding=10,

            border_radius=10,

            ink=True,


            content=ft.Row(

                [

                    ft.Icon(

                        icono,

                        color=color

                    ),


                    ft.Text(

                        texto,

                        color=color

                    )

                ],

                spacing=15

            ),


            on_click=lambda e: enviar_opcion(texto)

        )



    return ft.Container(

        width=250,

        bgcolor=ft.Colors.GREY_900,

        padding=20,


        content=ft.Column(

            [

                ft.Text(

                    "DJ STAFF NOVA",

                    size=25,

                    color=ft.Colors.WHITE,

                    weight=ft.FontWeight.BOLD

                ),



                ft.Divider(),



                boton(

                    ft.Icons.DASHBOARD,

                    "Dashboard"

                ),



                boton(

                    ft.Icons.PEOPLE,

                    "Clientes"

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

                ),



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
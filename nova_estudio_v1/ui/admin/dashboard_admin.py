import flet as ft


from ui.components.sidebar import sidebar
from ui.components.navbar import navbar
from ui.components.cards import card


from ui.admin.clientes import clientes
from ui.admin.empleados import empleados
from ui.admin.eventos import eventos
from ui.admin.inventario import inventario
from ui.admin.paquetes import paquetes
from ui.admin.contratos import contratos
from ui.admin.agencia import agencia



def dashboard_admin(page: ft.Page, cerrar_sesion):


    contenido = ft.Container(
        expand=True
    )



    # ==========================
    # DASHBOARD
    # ==========================

    def mostrar_dashboard():

        contenido.content = ft.Column(

            [

                navbar("Administrador"),


                ft.Container(height=20),



                ft.Row(

                    [

                        card(
                            "Clientes",
                            0,
                            ft.Icons.PEOPLE
                        ),


                        card(
                            "Eventos",
                            0,
                            ft.Icons.EVENT
                        ),


                        card(
                            "Empleados",
                            0,
                            ft.Icons.BADGE
                        ),


                        card(
                            "Inventario",
                            0,
                            ft.Icons.INVENTORY
                        )

                    ],

                    spacing=20

                ),



                ft.Container(height=25),



                ft.Container(

                    expand=True,

                    bgcolor=ft.Colors.GREY_900,

                    border_radius=15,

                    padding=20,


                    content=ft.Column(

                        [

                            ft.Text(

                                "Bienvenido al Panel de Administración",

                                size=25,

                                weight=ft.FontWeight.BOLD,

                                color=ft.Colors.WHITE

                            ),


                            ft.Divider(),


                            ft.Text(

                                "Desde este panel podrás administrar:",

                                color=ft.Colors.WHITE

                            ),


                            ft.Text("• Clientes", color=ft.Colors.WHITE),
                            ft.Text("• Empleados", color=ft.Colors.WHITE),
                            ft.Text("• DJs", color=ft.Colors.WHITE),
                            ft.Text("• Eventos", color=ft.Colors.WHITE),
                            ft.Text("• Inventario", color=ft.Colors.WHITE),
                            ft.Text("• Paquetes", color=ft.Colors.WHITE),
                            ft.Text("• Contratos", color=ft.Colors.WHITE),
                            ft.Text("• Reportes", color=ft.Colors.WHITE)

                        ]

                    )

                )

            ],

            expand=True

        )


        page.update()




    # ==========================
    # CERRAR SESIÓN
    # ==========================


    def mostrar_confirmacion():


        def aceptar(e):

            cerrar_sesion()



        def cancelar(e):

            mostrar_dashboard()



        contenido.content = ft.Container(

            expand=True,

            bgcolor=ft.Colors.GREY_900,

            border_radius=15,

            padding=30,


            content=ft.Column(

                [

                    ft.Text(

                        "Cerrar sesión",

                        size=30,

                        weight=ft.FontWeight.BOLD,

                        color=ft.Colors.WHITE

                    ),


                    ft.Text(

                        "¿Seguro que deseas salir?",

                        size=18,

                        color=ft.Colors.WHITE

                    ),


                    ft.Row(

                        [

                            ft.ElevatedButton(

                                "Cancelar",

                                on_click=cancelar

                            ),


                            ft.ElevatedButton(

                                "Aceptar",

                                on_click=aceptar

                            )

                        ],

                        alignment=ft.MainAxisAlignment.CENTER

                    )

                ],

                alignment=ft.MainAxisAlignment.CENTER,

                horizontal_alignment=ft.CrossAxisAlignment.CENTER

            )

        )


        page.update()




    # ==========================
    # CAMBIO DE PANTALLAS
    # ==========================


    def cambiar_pantalla(opcion):


        if opcion == "Dashboard":

            mostrar_dashboard()



        elif opcion == "Clientes":

            contenido.content = clientes(page)

            page.update()



        elif opcion == "Empleados":

            contenido.content = empleados(page)

            page.update()



        elif opcion == "Eventos":

            contenido.content = eventos(page)

            page.update()



        elif opcion == "Inventario":

            contenido.content = inventario(page)

            page.update()



        elif opcion == "Paquetes":

            contenido.content = paquetes(page)

            page.update()



        elif opcion == "Contratos":

            contenido.content = contratos(page)

            page.update()



        elif opcion == "Agencia":

            contenido.content = agencia(page)

            page.update()



        elif opcion == "Cerrar sesión":

            mostrar_confirmacion()




    mostrar_dashboard()



    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.BLACK,

        padding=15,


        content=ft.Row(

            [

                sidebar(

                    cambiar_pantalla

                ),



                ft.VerticalDivider(

                    width=1

                ),



                ft.Container(

                    expand=True,

                    content=contenido

                )

            ],

            expand=True

        )

    )
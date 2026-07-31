import flet as ft


from dao.dashboard_dao import DashboardDAO


from ui.components.sidebar import sidebar
from ui.components.navbar import navbar
from ui.components.cards import card


from ui.admin.clientes import clientes
from ui.admin.empleados import empleados
from ui.admin.eventos import eventos
from ui.admin.inventario import inventario
from ui.admin.paquetes import paquetes
from ui.admin.contratos import contratos
from ui.admin.pagos import pagos
from ui.admin.djs import djs
from ui.admin.reportes import reportes
from ui.admin.agencia import agencia



def dashboard_admin(page: ft.Page, cerrar_sesion, usuario):


    contenido = ft.Container(
        expand=True
    )



    # ==========================
    # DASHBOARD
    # ==========================

    def mostrar_dashboard():


        datos = DashboardDAO.obtener_estadisticas()



        contenido.content = ft.Column(

            [


                # NAVBAR DINAMICO

                navbar(
                    page,
                    usuario
                ),



                ft.Container(
                    height=20
                ),



                # CARDS

                ft.Row(

                    [


                        card(
                            "Clientes",
                            datos["clientes"],
                            ft.Icons.PEOPLE
                        ),



                        card(
                            "Eventos",
                            datos["eventos"],
                            ft.Icons.EVENT
                        ),



                        card(
                            "Empleados",
                            datos["empleados"],
                            ft.Icons.BADGE
                        ),



                        card(
                            "Inventario",
                            datos["inventario"],
                            ft.Icons.INVENTORY
                        )


                    ],

                    spacing=20

                ),



                ft.Container(
                    height=25
                ),




                # PANEL PRINCIPAL


                ft.Container(

                    expand=True,

                    bgcolor=ft.Colors.GREY_900,

                    border_radius=15,

                    padding=25,


                    content=ft.Column(

                        [


                            ft.Text(

                                "Bienvenido al Panel de Administración",

                                size=26,

                                weight=ft.FontWeight.BOLD,

                                color=ft.Colors.WHITE

                            ),



                            ft.Divider(),



                            ft.Text(

                                "Desde este panel podrás administrar:",

                                size=17,

                                color=ft.Colors.WHITE

                            ),



                            ft.Text(
                                "• Clientes",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Empleados",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• DJs",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Eventos",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Inventario",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Paquetes",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Contratos",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Pagos",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Reportes",
                                color=ft.Colors.WHITE
                            ),


                            ft.Text(
                                "• Agencia",
                                color=ft.Colors.WHITE
                            )

                        ]

                    )

                )


            ],

            expand=True

        )


        page.update()





    # ==========================
    # CONFIRMAR CIERRE
    # ==========================


    def confirmar_cierre():



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


        pantallas = {


            "Clientes": clientes,

            "Empleados": empleados,

            "DJs": djs,

            "Eventos": eventos,

            "Inventario": inventario,

            "Paquetes": paquetes,

            "Contratos": contratos,

            "Pagos": pagos,

            "Reportes": reportes,

            "Agencia": agencia

        }




        if opcion == "Dashboard":

            mostrar_dashboard()

            return




        if opcion == "Cerrar sesión":

            confirmar_cierre()

            return




        if opcion in pantallas:


            contenido.content = pantallas[opcion](page)

            page.update()





    # CARGAR AL INICIO

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
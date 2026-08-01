import flet as ft


from dao.dashboard_dao import DashboardDAO


from ui.components.sidebar import sidebar
from ui.components.navbar import navbar
from ui.components.graficas import graficas_dashboard


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
    # DASHBOARD PRINCIPAL
    # ==========================

    def mostrar_dashboard():


        datos_bd = DashboardDAO.obtener_estadisticas()



        datos = {

            "clientes": datos_bd.get("clientes", 0),

            "eventos": datos_bd.get("eventos", 0),

            "empleados": datos_bd.get("empleados", 0),

            "inventario": datos_bd.get("inventario", 0),

            "djs": datos_bd.get("djs", 0),

            "contratos": datos_bd.get("contratos", 0),

            "pagos": datos_bd.get("pagos", 0),

            "ingresos": datos_bd.get("ingresos", 0)

        }



        contenido.content = ft.Column(

            [

                # NAVBAR

                navbar(

                    page,

                    usuario

                ),



                ft.Container(

                    height=20

                ),



                # ==========================
                # PANEL PRINCIPAL
                # ==========================

                ft.Container(

                    expand=True,

                    bgcolor=ft.Colors.GREY_900,

                    border_radius=15,

                    padding=25,


                    content=graficas_dashboard(datos)

                )


            ],


            expand=True

        )


        page.update()





    # ==========================
    # CERRAR SESIÓN
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

                        color=ft.Colors.WHITE,

                        size=18

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
    # CAMBIO DE MÓDULOS
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





    # INICIO

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
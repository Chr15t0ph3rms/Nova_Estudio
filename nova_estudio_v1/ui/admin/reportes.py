import flet as ft

from database.conexion import Conexion


def reportes(page: ft.Page):


    # TARJETAS DE INFORMACIÓN

    card_clientes = ft.Card()
    card_empleados = ft.Card()
    card_djs = ft.Card()
    card_eventos = ft.Card()
    card_contratos = ft.Card()
    card_pagos = ft.Card()
    card_ingresos = ft.Card()


    # FUNCIÓN PARA CREAR TARJETAS

    def crear_card(titulo, valor, icono):
        return ft.Container(
            width=200,
            height=120,
            bgcolor=ft.Colors.GREY_900,
            border_radius=15,
            padding=15,
            content=ft.Column(
                [

                    ft.Icon(

                        icono,

                        color=ft.Colors.WHITE,

                        size=35

                    ),


                    ft.Text(

                        titulo,

                        color=ft.Colors.WHITE,

                        size=16

                    ),


                    ft.Text(

                        str(valor),

                        color=ft.Colors.WHITE,

                        size=25,

                        weight=ft.FontWeight.BOLD

                    )

                ]

            )

        ) 

    # OBTENER DATOS DE REPORTES

    def obtener_datos():

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()


        try:

            # Total clientes

            cursor.execute(
                "SELECT COUNT(*) FROM cliente"
            )

            clientes = cursor.fetchone()[0]



            # Total empleados

            cursor.execute(
                "SELECT COUNT(*) FROM empleados"
            )

            empleados = cursor.fetchone()[0]



            # Total DJs

            cursor.execute(
                "SELECT COUNT(*) FROM dj"
            )

            djs = cursor.fetchone()[0]



            # Total eventos

            cursor.execute(
                "SELECT COUNT(*) FROM evento"
            )

            eventos = cursor.fetchone()[0]



            # Total contratos

            cursor.execute(
                "SELECT COUNT(*) FROM contrato"
            )

            contratos = cursor.fetchone()[0]



            # Total pagos

            cursor.execute(
                "SELECT COUNT(*) FROM pago"
            )

            pagos = cursor.fetchone()[0]



            # Total ingresos

            cursor.execute(
                "SELECT COALESCE(SUM(monto),0) FROM pago"
            )

            ingresos = cursor.fetchone()[0]



            return (

                clientes,

                empleados,

                djs,

                eventos,

                contratos,

                pagos,

                ingresos

            )


        except Exception as error:

            print(
                "Error en reportes:",
                error
            )


            return (

                0,

                0,

                0,

                0,

                0,

                0,

                0

            )


        finally:

            cursor.close()

            conexion.close() 

    # CARGAR INFORMACIÓN

    def cargar_reportes():

        datos = obtener_datos()


        clientes = datos[0]

        empleados = datos[1]

        djs = datos[2]

        eventos = datos[3]

        contratos = datos[4]

        pagos = datos[5]

        ingresos = datos[6]



        contenido_reportes.controls = [

            ft.Row(

                [

                    crear_card(
                        "Clientes",
                        clientes,
                        ft.Icons.PEOPLE
                    ),


                    crear_card(
                        "Empleados",
                        empleados,
                        ft.Icons.BADGE
                    ),


                    crear_card(
                        "DJs",
                        djs,
                        ft.Icons.MUSIC_NOTE
                    ),


                    crear_card(
                        "Eventos",
                        eventos,
                        ft.Icons.EVENT
                    )

                ],

                spacing=20

            ),


            ft.Container(

                height=25

            ),


            ft.Row(

                [

                    crear_card(
                        "Contratos",
                        contratos,
                        ft.Icons.DESCRIPTION
                    ),


                    crear_card(
                        "Pagos",
                        pagos,
                        ft.Icons.PAYMENTS
                    ),


                    crear_card(
                        "Ingresos",
                        "$ " + str(ingresos),
                        ft.Icons.ATTACH_MONEY
                    )

                ],

                spacing=20

            )

        ]


        page.update() 

    # CONTENEDOR DE REPORTES

    contenido_reportes = ft.Column(

        expand=True

    )



    # INTERFAZ FINAL

    cargar_reportes()


    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Text(

                    "Reportes del Sistema",

                    size=28,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),


                ft.Divider(),


                contenido_reportes

            ],

            expand=True

        )

    )
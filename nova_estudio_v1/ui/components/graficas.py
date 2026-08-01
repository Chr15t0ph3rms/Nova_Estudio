import flet as ft



def graficas_dashboard(datos):

    return ft.Column(

        [

            ft.Text(

                "Estadísticas Generales",

                size=26,

                weight=ft.FontWeight.BOLD,

                color=ft.Colors.WHITE

            ),



            ft.Container(

                height=15

            ),



            ft.Row(

                [

                    panel_estadisticas(datos),


                    panel_ingresos(datos)


                ],


                spacing=20,


                expand=True

            ),



            ft.Container(

                height=20

            ),



            resumen_sistema(datos)


        ],


        expand=True,


        scroll=ft.ScrollMode.AUTO

    )






# =====================================
# PANEL DE INDICADORES
# =====================================

def panel_estadisticas(datos):


    return ft.Container(

        expand=True,


        height=300,


        bgcolor=ft.Colors.GREY_900,


        border_radius=15,


        padding=25,



        content=ft.Column(

            [

                ft.Text(

                    "Indicadores del sistema",

                    size=22,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),



                ft.Container(

                    height=15

                ),



                indicador(

                    "Contratos",

                    datos.get("contratos",0),

                    ft.Icons.DESCRIPTION

                ),



                indicador(

                    "Pagos",

                    datos.get("pagos",0),

                    ft.Icons.PAYMENT

                ),



                indicador(

                    "DJs",

                    datos.get("djs",0),

                    ft.Icons.MUSIC_NOTE

                ),



                indicador(

                    "Inventario",

                    datos.get("inventario",0),

                    ft.Icons.INVENTORY

                )


            ]

        )

    )







# =====================================
# BARRAS BLANCAS DINÁMICAS
# =====================================

def indicador(nombre, valor, icono):


    porcentaje = valor / 10


    if porcentaje > 1:

        porcentaje = 1



    return ft.Column(

        [

            ft.Row(

                [

                    ft.Row(

                        [

                            ft.Icon(

                                icono,

                                size=20,

                                color=ft.Colors.WHITE

                            ),



                            ft.Text(

                                nombre,

                                color=ft.Colors.WHITE,

                                size=16

                            )


                        ]

                    ),




                    ft.Text(

                        str(valor),

                        color=ft.Colors.WHITE,

                        weight=ft.FontWeight.BOLD

                    )


                ],


                alignment=ft.MainAxisAlignment.SPACE_BETWEEN

            ),




            ft.Container(

                height=12,

                bgcolor=ft.Colors.BLACK,

                border_radius=10,



                content=ft.Container(

                    height=12,

                    width=280 * porcentaje,

                    bgcolor=ft.Colors.WHITE,

                    border_radius=10

                )

            ),




            ft.Container(

                height=8

            )


        ]

    )







# =====================================
# PANEL INGRESOS
# =====================================

def panel_ingresos(datos):


    return ft.Container(

        width=260,


        height=300,



        bgcolor=ft.Colors.GREY_900,



        border_radius=15,



        padding=25,



        content=ft.Column(

            [

                ft.Icon(

                    ft.Icons.ATTACH_MONEY,

                    size=55,

                    color=ft.Colors.WHITE

                ),




                ft.Text(

                    "Ingresos",

                    size=22,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),




                ft.Text(

                    f"${datos.get('ingresos',0)}",

                    size=38,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),




                ft.Divider(),




                ft.Text(

                    f"Pagos registrados: {datos.get('pagos',0)}",

                    color=ft.Colors.WHITE

                ),




                ft.Text(

                    "Total generado",

                    color=ft.Colors.GREY_400

                )


            ],


            horizontal_alignment=ft.CrossAxisAlignment.CENTER,


            alignment=ft.MainAxisAlignment.CENTER


        )

    )








# =====================================
# RESUMEN DEL SISTEMA
# =====================================

def resumen_sistema(datos):


    return ft.Container(

        bgcolor=ft.Colors.GREY_900,


        border_radius=15,


        padding=20,



        content=ft.Column(

            [

                ft.Text(

                    "Resumen del sistema",

                    size=22,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),




                ft.Divider(),




                ft.Row(

                    [

                        tarjeta_resumen(

                            "Contratos",

                            datos.get("contratos",0)

                        ),



                        tarjeta_resumen(

                            "Pagos",

                            datos.get("pagos",0)

                        ),



                        tarjeta_resumen(

                            "DJs",

                            datos.get("djs",0)

                        )


                    ],


                    spacing=20

                )


            ]

        )

    )







def tarjeta_resumen(titulo, valor):


    return ft.Container(

        width=150,


        height=80,



        bgcolor=ft.Colors.BLACK,



        border_radius=10,



        padding=10,



        content=ft.Column(

            [

                ft.Text(

                    titulo,

                    color=ft.Colors.GREY_400

                ),




                ft.Text(

                    str(valor),

                    size=24,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                )


            ]

        )

    )
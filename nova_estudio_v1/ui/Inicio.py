import flet as ft

from Nova_Estudio.nova_estudio_v1.ui.inicio_sesion_admin import inicio_sesion_u
from ui.admin.dashboard_admin import dashboard_admin


def main(page: ft.Page):

    page.title = "DJ Staff Nova Studio"
    page.bgcolor = ft.Colors.BLACK

    page.window_width = 900
    page.window_height = 600

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    contenido = ft.Container(
        expand=True
    )


    # ABRIR DASHBOARD ADMIN


    def abrir_dashboard():

        contenido.content = dashboard_admin(page)

        page.update()



    # LOGIN ADMIN

    def entrar_admin(e):

        contenido.content = inicio_sesion_u(
            page,
            abrir_dashboard
        )

        page.update()



    # LOGIN USUARIO

    def entrar_usuario(e):

        page.snack_bar = ft.SnackBar(
            ft.Text(
                "Módulo usuario próximamente"
            )
        )

        page.snack_bar.open = True

        page.update()



    # PANTALLA PRINCIPAL

    contenido.content = ft.Container(

        expand=True,

        bgcolor=ft.Colors.BLACK,


        content=ft.Column(

            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,


            controls=[


                ft.Text(

                    "DJ Staff Nova Studio",

                    size=40,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),



                ft.Text(

                    "Tu música, tu experiencia inolvidable",

                    size=18,

                    color=ft.Colors.GREY

                ),



                ft.Container(

                    height=30

                ),



                ft.Row(

                    alignment=ft.MainAxisAlignment.CENTER,

                    spacing=40,


                    controls=[


                        
                        # TARJETA USUARIO
                        

                        ft.Container(

                            width=250,

                            height=300,

                            bgcolor=ft.Colors.GREY_900,

                            border_radius=15,

                            padding=20,


                            content=ft.Column(

                                alignment=ft.MainAxisAlignment.CENTER,

                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,


                                controls=[


                                    ft.Icon(

                                        ft.Icons.PERSON,

                                        size=60,

                                        color=ft.Colors.WHITE

                                    ),



                                    ft.Text(

                                        "Usuario",

                                        size=24,

                                        weight=ft.FontWeight.BOLD,

                                        color=ft.Colors.WHITE

                                    ),



                                    ft.Text(

                                        "Accede para solicitar eventos,\nver DJs y gestionar contrataciones",

                                        color=ft.Colors.WHITE70,

                                        text_align=ft.TextAlign.CENTER

                                    ),



                                    ft.ElevatedButton(

                                        "Entrar como usuario",

                                        bgcolor=ft.Colors.GREY_700,

                                        color=ft.Colors.WHITE,

                                        on_click=entrar_usuario

                                    )

                                ]

                            )

                        ),



                        
                        # TARJETA ADMIN
                        

                        ft.Container(

                            width=250,

                            height=300,

                            bgcolor=ft.Colors.GREY_900,

                            border_radius=15,

                            padding=20,


                            content=ft.Column(

                                alignment=ft.MainAxisAlignment.CENTER,

                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,


                                controls=[


                                    ft.Icon(

                                        ft.Icons.ADMIN_PANEL_SETTINGS,

                                        size=60,

                                        color=ft.Colors.WHITE

                                    ),



                                    ft.Text(

                                        "Administrador",

                                        size=24,

                                        weight=ft.FontWeight.BOLD,

                                        color=ft.Colors.WHITE

                                    ),



                                    ft.Text(

                                        "Accede al panel de administrador\npara gestionar la agencia",

                                        color=ft.Colors.WHITE70,

                                        text_align=ft.TextAlign.CENTER

                                    ),



                                    ft.ElevatedButton(

                                        "Entrar como administrador",

                                        bgcolor=ft.Colors.GREY_700,

                                        color=ft.Colors.WHITE,

                                        on_click=entrar_admin

                                    )

                                ]

                            )

                        )

                    ]

                )

            ]

        )

    )


    page.add(contenido)
import flet as ft


from ui.inicio_sesion_admin import inicio_sesion_admin
from ui.inicio_sesion_usuario import inicio_sesion_usuario
from ui.registro_usuario import registro_usuario_view
from ui.admin.dashboard_admin import dashboard_admin



def main(page: ft.Page):


    # ==========================
    # CONFIGURACIÓN
    # ==========================

    page.title = "DJ Staff Nova Studio"

    page.bgcolor = ft.Colors.BLACK

    page.window_width = 1200

    page.window_height = 700


    contenido = ft.Container(
        expand=True
    )



    # ==========================
    # VOLVER AL INICIO
    # ==========================

    def volver_inicio(e=None):

        contenido.content = pantalla_inicio()

        page.update()



    # ==========================
    # ABRIR DASHBOARD ADMIN
    # ==========================

    def abrir_dashboard(usuario):


        contenido.content = dashboard_admin(

            page,

            volver_inicio,

            usuario

        )


        page.update()





    # ==========================
    # LOGIN ADMIN
    # ==========================

    def entrar_admin(e):


        contenido.content = inicio_sesion_admin(

            page,

            abrir_dashboard

        )


        page.update()





    # ==========================
    # LOGIN USUARIO
    # ==========================

    def entrar_usuario(e):


        contenido.content = inicio_sesion_usuario(

            page,

            abrir_registro

        )


        page.update()





    # ==========================
    # REGISTRO
    # ==========================

    def abrir_registro():


        contenido.content = registro_usuario_view(

            page

        )


        page.update()





    # ==========================
    # PANTALLA PRINCIPAL
    # ==========================

    def pantalla_inicio():


        return ft.Container(


            expand=True,


            bgcolor=ft.Colors.BLACK,


            content=ft.Column(


                [



                    ft.Image(

                        src="logo_nova.png",

                        width=160,

                        height=120

                    ),




                    ft.Text(

                        "DJ STAFF NOVA STUDIO",

                        size=40,

                        weight=ft.FontWeight.BOLD,

                        color=ft.Colors.WHITE

                    ),




                    ft.Text(

                        "Tu música, tu experiencia inolvidable",

                        size=18,

                        color=ft.Colors.GREY

                    ),




                    ft.Container(height=30),




                    ft.Row(

                        [



                            # ======================
                            # USUARIO
                            # ======================


                            ft.Container(


                                width=280,

                                height=300,


                                bgcolor=ft.Colors.GREY_900,


                                border_radius=15,


                                padding=20,



                                content=ft.Column(

                                    [



                                        ft.Icon(

                                            ft.Icons.PERSON,

                                            size=60,

                                            color=ft.Colors.WHITE

                                        ),




                                        ft.Text(

                                            "Usuario",

                                            size=25,

                                            color=ft.Colors.WHITE,

                                            weight=ft.FontWeight.BOLD

                                        ),




                                        ft.Text(

                                            "Solicita eventos\n"
                                            "Consulta DJs\n"
                                            "Realiza contrataciones",

                                            color=ft.Colors.WHITE70,

                                            text_align=ft.TextAlign.CENTER

                                        ),




                                        ft.ElevatedButton(

                                            "Entrar como usuario",

                                            on_click=entrar_usuario

                                        )


                                    ],


                                    alignment=ft.MainAxisAlignment.CENTER,


                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER

                                )

                            ),





                            # ======================
                            # ADMINISTRADOR
                            # ======================


                            ft.Container(


                                width=280,


                                height=300,


                                bgcolor=ft.Colors.GREY_900,


                                border_radius=15,


                                padding=20,



                                content=ft.Column(

                                    [



                                        ft.Icon(

                                            ft.Icons.ADMIN_PANEL_SETTINGS,

                                            size=60,

                                            color=ft.Colors.WHITE

                                        ),




                                        ft.Text(

                                            "Administrador",

                                            size=25,

                                            color=ft.Colors.WHITE,

                                            weight=ft.FontWeight.BOLD

                                        ),




                                        ft.Text(

                                            "Gestiona toda la agencia",

                                            color=ft.Colors.WHITE70

                                        ),




                                        ft.ElevatedButton(

                                            "Entrar como administrador",

                                            on_click=entrar_admin

                                        )



                                    ],


                                    alignment=ft.MainAxisAlignment.CENTER,


                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER


                                )


                            )



                        ],



                        alignment=ft.MainAxisAlignment.CENTER,


                        spacing=50


                    )



                ],



                alignment=ft.MainAxisAlignment.CENTER,


                horizontal_alignment=ft.CrossAxisAlignment.CENTER


            )


        )





    # INICIO

    contenido.content = pantalla_inicio()


    page.add(contenido)




# ==========================
# EJECUTAR
# ==========================


if __name__ == "__main__":


    ft.app(

        target=main,

        assets_dir="assets"

    )
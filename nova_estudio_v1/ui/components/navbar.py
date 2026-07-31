import flet as ft
from datetime import datetime


def navbar(page, usuario):

    fecha = datetime.now().strftime("%d/%m/%Y")


    nombre = usuario.get("nombre", "")
    apellido = usuario.get("apellido", "")
    correo = usuario.get("correo", "")
    rol = usuario.get("rol", "")


    inicial = nombre[0].upper() if nombre else "A"



    # ==========================
    # CERRAR DIALOG
    # ==========================

    def cerrar_dialog(e):

        page.pop_dialog()



    # ==========================
    # PERFIL
    # ==========================

    def mostrar_perfil(e):


        dialog = ft.AlertDialog(

            title=ft.Text(
                "Perfil Administrador"
            ),


            content=ft.Column(

                [
                    ft.Text(
                        f"Nombre: {nombre}"
                    ),

                    ft.Text(
                        f"Apellido: {apellido}"
                    ),

                    ft.Text(
                        f"Correo: {correo}"
                    ),

                    ft.Text(
                        f"Rol: {rol}"
                    )
                ],

                tight=True
            ),


            actions=[

                ft.TextButton(
                    "Cerrar",
                    on_click=cerrar_dialog
                )

            ]

        )


        page.show_dialog(dialog)





    # ==========================
    # NOTIFICACIONES
    # ==========================

    def mostrar_notificaciones(e):


        dialog = ft.AlertDialog(


            title=ft.Text(
                "Notificaciones"
            ),


            content=ft.Column(

                [

                    ft.Text(
                        "✓ Sistema iniciado correctamente"
                    ),


                    ft.Text(
                        "✓ No hay notificaciones nuevas"
                    )

                ],

                tight=True
            ),


            actions=[

                ft.TextButton(
                    "Cerrar",
                    on_click=cerrar_dialog
                )

            ]

        )


        page.show_dialog(dialog)




    # ==========================
    # NAVBAR
    # ==========================

    return ft.Container(


        bgcolor=ft.Colors.GREY_900,

        padding=15,

        border_radius=10,


        content=ft.Row(

            [


                ft.Column(

                    [

                        ft.Text(

                            "DJ STAFF NOVA STUDIO",

                            size=24,

                            weight=ft.FontWeight.BOLD,

                            color=ft.Colors.WHITE

                        ),


                        ft.Text(

                            fecha,

                            color=ft.Colors.GREY_400

                        )

                    ]

                ),



                ft.Container(
                    expand=True
                ),




                ft.IconButton(

                    icon=ft.Icons.NOTIFICATIONS,

                    icon_color=ft.Colors.WHITE,

                    tooltip="Notificaciones",

                    on_click=mostrar_notificaciones

                ),





                ft.Container(

                    on_click=mostrar_perfil,


                    content=ft.CircleAvatar(

                        bgcolor=ft.Colors.GREY_700,


                        content=ft.Text(

                            inicial,

                            color=ft.Colors.WHITE

                        )

                    )

                ),





                ft.Container(

                    on_click=mostrar_perfil,


                    content=ft.Column(

                        [

                            ft.Text(

                                f"{nombre} {apellido}",

                                color=ft.Colors.WHITE,

                                weight=ft.FontWeight.BOLD

                            ),


                            ft.Text(

                                rol,

                                color=ft.Colors.GREY_400

                            )

                        ]

                    )

                )


            ]

        )

    )
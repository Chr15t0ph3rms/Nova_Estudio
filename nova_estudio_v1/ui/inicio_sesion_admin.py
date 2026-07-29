import flet as ft


def inicio_sesion_u(regresar):


    email_field = ft.TextField(

        label="Correo electrónico",

        width=300,

        bgcolor=ft.Colors.WHITE,

        color=ft.Colors.BLACK

    )


    password_field = ft.TextField(

        label="Contraseña",

        password=True,

        can_reveal_password=True,

        width=300,

        bgcolor=ft.Colors.WHITE,

        color=ft.Colors.BLACK

    )



    def login(e):

        email = email_field.value

        password = password_field.value



        if email == "chrisp@gmail.com" and password == "Christopher":


            regresar()



        else:


            dialog = ft.AlertDialog(

                title=ft.Text(

                    "Correo o contraseña incorrectos"

                )

            )


            dialog.open = True

            page.update()



    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.BLACK,


        content=ft.Column(

            [

                ft.Text(

                    "INICIO SESIÓN",

                    size=30,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),



                email_field,


                password_field,



                ft.ElevatedButton(

                    "Iniciar sesión",

                    bgcolor=ft.Colors.GREY_700,

                    color=ft.Colors.WHITE,

                    on_click=login

                )

            ],


            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=20

        )

    )
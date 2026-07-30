import flet as ft


def inicio_sesion_usuario(page, ir_registro=None):

    correo = ft.TextField(
        hint_text="Correo electrónico",
        width=380,
        height=55,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK
    )


    contraseña = ft.TextField(
        hint_text="Contraseña",
        width=380,
        height=55,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        password=True,
        can_reveal_password=True
    )


    def ingresar(e):

        if correo.value == "" or contraseña.value == "":

            page.snack_bar = ft.SnackBar(
                ft.Text("Completa todos los campos")
            )

        else:

            page.snack_bar = ft.SnackBar(
                ft.Text("Inicio de sesión correcto")
            )

        page.snack_bar.open = True
        page.update()



    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.BLACK,

        alignment=ft.alignment.center,


        content=ft.Column(

            controls=[


                ft.Text(
                    "INICIO SESIÓN USUARIO",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),


                ft.Text(
                    "Accede a tu cuenta",
                    size=18,
                    color=ft.Colors.GREY
                ),


                correo,


                contraseña,


                ft.ElevatedButton(

                    "Ingresar",

                    width=180,

                    bgcolor=ft.Colors.GREY_700,

                    color=ft.Colors.WHITE,

                    on_click=ingresar

                ),



                ft.TextButton(

                    "¿No tienes cuenta? Regístrate aquí",

                    style=ft.ButtonStyle(
                        color=ft.Colors.BLUE
                    )

                ),



                ft.TextButton(

                    "¿Olvidaste tu contraseña?",

                    style=ft.ButtonStyle(
                        color=ft.Colors.BLUE
                    )

                )


            ],


            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=20

        )

    )
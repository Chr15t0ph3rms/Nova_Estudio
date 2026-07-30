import flet as ft


def inicio_sesion_admin(page, abrir_dashboard):


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



    def login(e):

        if correo.value == "chrisp@gmail.com" and contraseña.value == "Christopher":

            abrir_dashboard()


        else:

            page.dialog = ft.AlertDialog(

                title=ft.Text(
                    "Correo o contraseña incorrectos"
                )

            )

            page.dialog.open = True
            page.update()



    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.BLACK,

        alignment=ft.Alignment(0, 0),


        content=ft.Column(

            [

                ft.Text(

                    "INICIO SESIÓN ADMINISTRADOR",

                    size=32,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),



                ft.Text(

                    "Accede al panel de administración",

                    size=16,

                    color=ft.Colors.GREY

                ),



                correo,


                contraseña,



                ft.ElevatedButton(

                    "Ingresar",

                    width=180,

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
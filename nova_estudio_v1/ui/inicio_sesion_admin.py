import flet as ft

from dao.usuario_dao import UsuarioDAO



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


        usuario = UsuarioDAO.login(

            correo.value,

            contraseña.value

        )



        if usuario:


            datos_usuario = {


                "id": usuario[0],

                "nombre": usuario[1],

                "apellido": usuario[2],

                "correo": usuario[3],

                "rol": usuario[4]


            }



            abrir_dashboard(

                datos_usuario

            )



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

        alignment=ft.Alignment(0,0),


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
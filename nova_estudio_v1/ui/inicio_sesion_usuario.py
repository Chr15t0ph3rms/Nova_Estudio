import flet as ft

from dao.usuario_dao import UsuarioDAO

def inicio_sesion_usuario(page, ir_registro=None, al_iniciar_sesion=None):

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

        usuario = UsuarioDAO.login(correo.value, contraseña.value)

        if usuario is None:
            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Correo o contraseña incorrectos")
                )
            )
            return

        # usuario = (id_usuario, nombre, apellido, correo, rol)
        rol = usuario[4]

        if rol != "cliente":
            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Esta cuenta no es de cliente. Usa el acceso de administrador.")
                )
            )
            return

        datos_usuario = {
            "id": usuario[0],
            "nombre": usuario[1],
            "apellido": usuario[2],
            "correo": usuario[3],
            "rol": usuario[4]
        }

        if al_iniciar_sesion:
            al_iniciar_sesion(datos_usuario)

    return ft.Container(

        expand=True,
        bgcolor=ft.Colors.BLACK,
        alignment=ft.Alignment(0, 0),

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
                    on_click=login
                ),

                ft.TextButton(
                    "¿No tienes cuenta? Regístrate aquí",
                    style=ft.ButtonStyle(color=ft.Colors.BLUE),
                    on_click=lambda e: ir_registro() if ir_registro else None
                ),

                ft.TextButton(
                    "¿Olvidaste tu contraseña?",
                    style=ft.ButtonStyle(color=ft.Colors.BLUE)
                )

            ],

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20

        )

    )

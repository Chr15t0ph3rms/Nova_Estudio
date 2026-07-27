import flet as ft

def inicio_sesion_u(regresar):

    layout = ft.Stack(expand = True)

    # ------------ Campos del formulario ------------------

    # Función de login
    def login(e):
        email = email_field.value
        password = password_field.value
        if email == "chrisp@gmail.com" and password == "Christopher":
            dialog = ft.AlertDialog(title=ft.Text("Inicio de sesión exitoso 🎉"))
        else:
            dialog = ft.AlertDialog(title=ft.Text("Correo o contraseña incorrectos"))
        dialog.open = True
        layout.update()

    # Título
    title = ft.Text("INICIO SESIÓN", size=24, weight="bold", color="white")
    subtitle = ft.Text("Accede a tu cuenta", size=14, color="gray")

    # Campos de entrada
    email_field = ft.TextField(label="Correo electrónico", width=300, bgcolor="white", hint_text = "Jared Alan")
    password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, bgcolor="white", hint_text = "****")

    # Checkbox
    remember_me = ft.Checkbox(label="Recordarme", value=False, fill_color="white")

    # Botón de inicio de sesión
    login_button = ft.ElevatedButton("Iniciar sesión", on_click=login, bgcolor="gray", color="white")

    # Links
    forgot_password = ft.TextButton("¿Olvidaste tu contraseña?", style=ft.ButtonStyle(color="blue"))
    register = ft.TextButton("¿No tienes cuenta? Regístrate aquí", style=ft.ButtonStyle(color="blue"))

    # Layout principal
    layout_principal = ft.Container(
        padding = 10,
        content = ft.Column(

            [
                title,
                subtitle,
                email_field,
                password_field,
                remember_me,
                login_button,
                forgot_password,
                register,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=10,
        )
    )

    layout.controls.append(layout_principal)

    return layout
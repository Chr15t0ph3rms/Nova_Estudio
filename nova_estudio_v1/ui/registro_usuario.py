import flet as ft

def registro_usuario_view(page: ft.Page):
    return ft.Container(
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text("Registro de Administrador", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Nombre completo", width=300),
                ft.TextField(label="Correo electrónico", width=300),
                ft.TextField(label="Teléfono", width=300),
                ft.TextField(label="Contraseña", password=True, width=300),
                ft.TextField(label="Confirmar contraseña", password=True, width=300),
                ft.ElevatedButton(
                    text="Crear cuenta",
                    on_click=lambda e: page.go("/recuperar_admin"),  # después de registrarse, pasa a recuperación
                ),
            ],
        ),
    )

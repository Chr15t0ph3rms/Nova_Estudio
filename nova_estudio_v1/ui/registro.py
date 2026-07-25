import flet as ft

def registro_view(page: ft.Page):
    return ft.Container(
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Registro de Usuario", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Nombre completo", width=300),
                ft.TextField(label="Correo electrónico", width=300),
                ft.TextField(label="Teléfono", width=300),
                ft.TextField(label="Contraseña", password=True, width=300),
                ft.TextField(label="Confirmar contraseña", password=True, width=300),
                ft.ElevatedButton(text="Registrarse", on_click=lambda e: page.go("/dashboard_usuario")),
            ],
        ),
    )

import flet as ft

def recuperar_admin_view(page: ft.Page):
    return ft.Container(
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text("Recuperar Contraseña - Administrador", size=30, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Correo electrónico", width=300),
                ft.ElevatedButton(
                    text="Enviar enlace de recuperación",
                    on_click=lambda e: page.go("/inicio_admin"),  # después de recuperar, va al inicio admin
                ),
                ft.TextButton(
                    text="¿Ya recuerdas tu contraseña? Inicia sesión",
                    on_click=lambda e: page.go("/inicio_admin"),
                ),
            ],
        ),
    )

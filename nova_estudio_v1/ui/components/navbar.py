import flet as ft
from datetime import datetime

def navbar(nombre="Administrador"):

    fecha = datetime.now().strftime("%d/%m/%Y")

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
                            color=ft.Colors.WHITE,
                        ),
                        ft.Text(
                            fecha,
                            color=ft.Colors.GREY_400,
                        ),
                    ],
                    spacing=3,
                ),

                ft.Container(expand=True),

                ft.Icon(ft.Icons.NOTIFICATIONS, color="white"),

                ft.CircleAvatar(
                    bgcolor=ft.Colors.GREY_700,
                    content=ft.Text(nombre[0]),
                ),

                ft.Text(
                    nombre,
                    color="white",
                ),
            ]
        ),
    )
import flet as ft

def card(titulo, valor, icono):

    return ft.Container(
        width=180,
        height=110,
        bgcolor=ft.Colors.GREY_900,
        border_radius=15,
        padding=15,
        content=ft.Column(
            [
                ft.Icon(icono, color="white", size=30),

                ft.Text(
                    str(valor),
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),

                ft.Text(
                    titulo,
                    color=ft.Colors.GREY_400,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
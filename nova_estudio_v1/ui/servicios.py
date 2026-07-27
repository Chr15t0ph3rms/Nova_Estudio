import flet as ft

def servicios_view(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.add(
        ft.Column(
            [
                ft.Text("Servicios", size=20, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.DataTable(
                    bgcolor=ft.colors.GREY_900,
                    columns=[
                        ft.DataColumn(ft.Text("Nombre", color=ft.colors.WHITE)),
                        ft.DataColumn(ft.Text("Descripción", color=ft.colors.WHITE)),
                        ft.DataColumn(ft.Text("Precio", color=ft.colors.WHITE)),
                        ft.DataColumn(ft.Text("Estado", color=ft.colors.WHITE)),
                    ],
                    rows=[
                        ft.DataRow(cells=[ft.DataCell(ft.Text("DJ Premium", color=ft.colors.WHITE)), ft.DataCell(ft.Text("Servicio musical", color=ft.colors.WHITE)), ft.DataCell(ft.Text("$5000", color=ft.colors.WHITE)), ft.DataCell(ft.Text("Activo", color=ft.colors.GREY_300))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("Fotografía", color=ft.colors.WHITE)), ft.DataCell(ft.Text("Cobertura completa", color=ft.colors.WHITE)), ft.DataCell(ft.Text("$3000", color=ft.colors.WHITE)), ft.DataCell(ft.Text("Activo", color=ft.colors.GREY_300))]),
                    ],
                ),
                ft.Text("Agregar servicio", size=18, color=ft.colors.GREY_300),
                ft.TextField(label="Nombre del servicio", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, border_color=ft.colors.GREY_600),
                ft.TextField(label="Descripción del servicio", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, border_color=ft.colors.GREY_600),
                ft.TextField(label="Precio", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE, border_color=ft.colors.GREY_600),
                ft.Dropdown(label="Estado", options=[ft.dropdown.Option("Activo"), ft.dropdown.Option("Inactivo")], bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                ft.ElevatedButton("Guardar", bgcolor=ft.colors.GREY_600, color=ft.colors.BLACK),
            ],
            spacing=15,
        )
    )

import flet as ft

from database.conexion import Conexion


def reportes(page: ft.Page):
    # crear tarjetas

    def crear_card(titulo, valor, icono):
        return ft.Container(
            width=220,

            height=140,

            bgcolor=ft.Colors.GREY_900,

            border_radius=15,

            padding=15,

            content=ft.Column(
                [
                    ft.Icon(
                        icono,

                        color=ft.Colors.WHITE,

                        size=35
                    ),

                    ft.Text(
                        titulo,

                        color=ft.Colors.GREY_300,

                        size=16
                    ),

                    ft.Text(
                        str(valor),

                        color=ft.Colors.WHITE,

                        size=28,

                        weight=ft.FontWeight.BOLD
                    )
                ],

                spacing=5
            )
        )

    # obtener datos

    def obtener_datos():
        conexion = None

        try:
            conexion = Conexion.obtener_conexion()

            cursor = conexion.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM cliente"
            )

            clientes = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM empleados"
            )

            empleados = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM dj"
            )

            djs = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM evento"
            )

            eventos = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM contrato"
            )

            contratos = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM pago"
            )

            pagos = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COALESCE(SUM(monto),0) FROM pago"
            )

            ingresos = cursor.fetchone()[0]

            cursor.close()

            return (
                clientes,

                empleados,

                djs,

                eventos,

                contratos,

                pagos,

                ingresos
            )

        except Exception as error:
            print(
                "Error cargando reportes:",
                error
            )

            return (
                0,

                0,

                0,

                0,

                0,

                0,

                0
            )

        finally:
            if conexion:
                conexion.close()

    # cargar reportes

    def cargar_reportes():
        datos = obtener_datos()

        clientes = datos[0]

        empleados = datos[1]

        djs = datos[2]

        eventos = datos[3]

        contratos = datos[4]

        pagos = datos[5]

        ingresos = datos[6]

        contenido_reportes.controls = [
            ft.Row(
                [
                    crear_card(
                        "Clientes",
                        clientes,
                        ft.Icons.PEOPLE
                    ),

                    crear_card(
                        "Empleados",
                        empleados,
                        ft.Icons.BADGE
                    ),

                    crear_card(
                        "DJs",
                        djs,
                        ft.Icons.MUSIC_NOTE
                    ),

                    crear_card(
                        "Eventos",
                        eventos,
                        ft.Icons.EVENT
                    )
                ],

                spacing=20,

                alignment=ft.MainAxisAlignment.START
            ),

            ft.Container(
                height=25
            ),

            ft.Row(
                [
                    crear_card(
                        "Contratos",
                        contratos,
                        ft.Icons.DESCRIPTION
                    ),

                    crear_card(
                        "Pagos",
                        pagos,
                        ft.Icons.PAYMENTS
                    ),

                    crear_card(
                        "Ingresos",

                        f"$ {float(ingresos):.2f}",

                        ft.Icons.ATTACH_MONEY
                    )

                ],

                spacing=20,

                alignment=ft.MainAxisAlignment.START
            )

        ]

        page.update()

    # contenedor

    contenido_reportes = ft.Column(
        expand=True
    )

    cargar_reportes()

    return ft.Container(
        expand=True,

        padding=20,

        content=ft.Column(
            [
                ft.Text(
                    "Reportes del Sistema",

                    size=28,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE
                ),

                ft.Divider(),

                contenido_reportes

            ],

            expand=True
        )
    )

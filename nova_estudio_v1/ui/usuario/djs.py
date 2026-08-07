import flet as ft
import datetime

from dao.dj_dao import DjDAO
from dao.cliente_dao import ClienteDAO
from dao.eventos_dao import EventosDAO
from dao.pago_dao import PagoDAO
from modelos.eventos import Eventos
from modelos.pago import Pago

def djs(page: ft.Page, usuario=None):

    dao = DjDAO()
    contenedor = ft.Container(expand=True)

    color = ft.Colors.PURPLE_200  # color de acento para toda la sección de DJs

    # Pantalla 1: lista de djs

    def mostrar_lista():

        lista_djs = dao.obtener_todo()

        if not lista_djs:
            tarjetas = [ft.Text("Aún no hay DJs disponibles.", color=ft.Colors.WHITE70)]
        else:
            tarjetas = [tarjeta_dj(dj) for dj in lista_djs]

        contenedor.content = ft.Container(
            expand=True,
            padding=25,
            content=ft.Column(
                [
                    ft.Text("DJs Disponibles", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text("Elige el DJ ideal para tu evento", size=15, color=ft.Colors.WHITE70),
                    ft.Container(height=10),
                    ft.Divider(),
                    ft.Container(height=10),
                    ft.Row(tarjetas, wrap=True, spacing=20, run_spacing=20),
                ],
                expand=True,
                scroll=ft.ScrollMode.ALWAYS,
            ),
        )

        page.update()

    def mostrar_detalles(dj):

        page.show_dialog(
            ft.AlertDialog(
                title=ft.Text(f"{dj.nombre} {dj.app} {dj.apm}", color=color, weight=ft.FontWeight.BOLD),
                content=ft.Column(
                    [
                        ft.Text(f"Especialidad: {dj.especialidad}"),
                        ft.Text(f"Teléfono: {dj.telefono}"),
                        ft.Text(f"Disponibilidad: {'Disponible' if dj.disponibilidad else 'No disponible'}"),
                        ft.Text(f"Tarifa por hora: ${dj.tarifa_hora}"),
                    ],
                    tight=True,
                    spacing=8,
                ),
            )
        )

    def tarjeta_dj(dj):

        return ft.Container(
            width=250,
            bgcolor=ft.Colors.GREY_900,
            border=ft.Border.all(1.5, color),
            border_radius=15,
            padding=20,

            content=ft.Column(
                [
                    ft.CircleAvatar(
                        content=ft.Icon(ft.Icons.HEADPHONES, size=30),
                        radius=35,
                        bgcolor=ft.Colors.GREY_800,
                    ),

                    ft.Container(height=8),

                    ft.Text(f"{dj.nombre} {dj.app} {dj.apm}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(dj.especialidad, size=13, color=ft.Colors.WHITE70),

                    ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.CIRCLE,
                                size=10,
                                color=ft.Colors.GREEN if dj.disponibilidad else ft.Colors.RED,
                            ),
                            ft.Text(
                                "Disponible" if dj.disponibilidad else "No disponible",
                                size=12,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        spacing=6,
                    ),

                    ft.Container(height=10),

                    ft.OutlinedButton(
                        "Ver más",
                        style=ft.ButtonStyle(color=color, side=ft.BorderSide(1, color)),
                        width=200,
                        on_click=lambda e, d=dj: mostrar_detalles(d),
                    ),

                    ft.Container(height=8),

                    ft.ElevatedButton(
                        "Cotiza",
                        bgcolor=color,
                        color=ft.Colors.BLACK,
                        width=200,
                        on_click=lambda e, d=dj: intentar_cotizar(d),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
        )

    # Pantalla 2: cotización (elegir horas -> ver precio)

    def intentar_cotizar(dj):

        if not dj.disponibilidad:
            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("DJ no disponible", color=ft.Colors.RED),
                    content=ft.Text(f"{dj.nombre} {dj.app} {dj.apm} no está disponible en este momento."),
                )
            )
            return

        mostrar_cotizacion(dj)

    def mostrar_cotizacion(dj):

        horas = ft.Dropdown(
            label="¿Cuántas horas necesitas?",
            options=[ft.dropdown.Option(str(h)) for h in range(1, 9)],
            value="4",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            width=250,
        )

        def actualizar_total(e=None):
            h = int(horas.value)
            texto_total.value = f"${dj.tarifa_hora * h}"
            page.update()

        texto_total = ft.Text(
            f"${dj.tarifa_hora * 4}",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=color,
        )

        horas.on_change = actualizar_total

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),

            content=ft.Container(
                width=420,
                bgcolor=ft.Colors.GREY_900,
                border=ft.Border.all(1.5, color),
                border_radius=15,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text("Cotización", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Divider(),

                        ft.Text(f"DJ: {dj.nombre} {dj.app} {dj.apm}", size=16, color=ft.Colors.WHITE),
                        ft.Text(f"Especialidad: {dj.especialidad}", color=ft.Colors.WHITE70),
                        ft.Text(f"Tarifa por hora: ${dj.tarifa_hora}", color=ft.Colors.WHITE70),

                        ft.Container(height=10),
                        horas,
                        ft.Container(height=10),

                        ft.Text("Total estimado:", color=ft.Colors.WHITE70),
                        texto_total,

                        ft.Container(height=15),

                        ft.Row(
                            [
                                ft.OutlinedButton("Cancelar", on_click=lambda e: mostrar_lista()),
                                ft.ElevatedButton(
                                    "Pagar",
                                    bgcolor=color,
                                    color=ft.Colors.BLACK,
                                    on_click=lambda e: mostrar_pago(dj, int(horas.value)),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
            ),
        )

        page.update()

    # Pantalla 3: formulario de pago

    def mostrar_pago(dj, horas):

        total = dj.tarifa_hora * horas

        nombre_titular = ft.TextField(label="Nombre del titular de la tarjeta", bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
        numero_tarjeta = ft.TextField(label="Número de la tarjeta", bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK, max_length=19)

        mes_vencimiento = ft.Dropdown(
            label="Mes de vencimiento",
            options=[ft.dropdown.Option(f"{m:02d}") for m in range(1, 13)],
            width=150,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        anio_actual = datetime.date.today().year
        anio_vencimiento = ft.Dropdown(
            label="Año de vencimiento",
            options=[ft.dropdown.Option(str(anio_actual + i)) for i in range(0, 11)],
            width=150,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        cvv = ft.TextField(
            label="CVV", bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK,
            password=True, can_reveal_password=True, max_length=4, width=150,
        )

        def procesar_pago(e):

            if not nombre_titular.value.strip():
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta el nombre del titular")))
                return

            numero_limpio = numero_tarjeta.value.replace(" ", "")
            if not numero_limpio.isdigit() or len(numero_limpio) < 13:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Número de tarjeta inválido")))
                return

            if not mes_vencimiento.value or not anio_vencimiento.value:
                page.show_dialog(ft.AlertDialog(title=ft.Text("Falta la fecha de vencimiento")))
                return

            if not cvv.value or not cvv.value.isdigit() or len(cvv.value) < 3:
                page.show_dialog(ft.AlertDialog(title=ft.Text("CVV inválido")))
                return

            # TODO: cuando exista el enlace cliente-evento en la BD, aquí se
            # insertaría el registro real en "contrato"/"pago".

            perfil_cliente = ClienteDAO.obtener_por_usuario(usuario["id"]) if usuario else None

            if perfil_cliente is None:
                page.show_dialog(
                    ft.AlertDialog(
                        title=ft.Text("No se pudo registrar la contratación"),
                        content=ft.Text("Tu cuenta no tiene un perfil de cliente vinculado todavía."),
                    )
                )
                return

            id_cliente, telefono, calle, numero_exterior, colonia = perfil_cliente

            eventos_dao = EventosDAO()
            nuevo_id_evento = eventos_dao.obtener_ultimo_id() + 1

            nuevo_evento = Eventos(
                id_evento=nuevo_id_evento,
                nombre=f"Evento - DJ {dj.nombre} {dj.app}",
                fecha=datetime.date.today(),
                hora=datetime.datetime.now().time(),
                calle=calle,
                colonia=colonia,
                numero_exterior=numero_exterior,
                costo=total,
                id_cliente=id_cliente,
                estado="En proceso",
            )

            eventos_dao.insertar(nuevo_evento)

            pago_dao = PagoDAO()
            nuevo_id_pago = pago_dao.obtener_ultimo_id() + 1

            nuevo_pago = Pago(
                id_pago=nuevo_id_pago,
                id_contrato=None,
                fecha_pago=datetime.date.today(),
                monto=total,
                estado="Pagado",
                id_cliente=id_cliente,
                id_evento=nuevo_id_evento,
            )

            pago_dao.insertar(nuevo_pago)

            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("¡Pago confirmado!"),
                    content=ft.Text(f"Contrataste a {dj.nombre} por {horas} hora(s) — Total: ${total}. Ya puedes verlo en 'Mis Eventos' y 'Mis Pagos'."),
                )
            )

            mostrar_lista()

        contenedor.content = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),

            content=ft.Container(
                width=480,
                bgcolor=ft.Colors.GREY_900,
                border=ft.Border.all(1.5, color),
                border_radius=15,
                padding=30,

                content=ft.Column(
                    [
                        ft.Text(
                            "Agregar una tarjeta de crédito o débito",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER,
                        ),

                        ft.Divider(),
                        ft.Text(f"Total a pagar: ${total}", size=18, weight=ft.FontWeight.BOLD, color=color),
                        ft.Text("Todos los campos son obligatorios", size=12, color=ft.Colors.WHITE70),

                        ft.Row(
                            [
                                ft.Icon(ft.Icons.CREDIT_CARD, color=ft.Colors.WHITE70),
                                ft.Text("Se aceptan Visa, Mastercard y Amex", size=12, color=ft.Colors.WHITE70),
                            ],
                            spacing=8,
                        ),

                        ft.Container(height=10),

                        nombre_titular,
                        numero_tarjeta,
                        ft.Row([mes_vencimiento, anio_vencimiento, cvv], spacing=10),

                        ft.Row(
                            [
                                ft.Icon(ft.Icons.HELP_OUTLINE, size=16, color=ft.Colors.WHITE70),
                                ft.Text(
                                    "¿Dónde encuentro el CVV? Últimos 3 dígitos de la parte trasera.",
                                    size=12,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            spacing=6,
                        ),

                        ft.Container(height=15),

                        ft.Row(
                            [
                                ft.OutlinedButton("Atrás", on_click=lambda e: mostrar_cotizacion(dj)),
                                ft.ElevatedButton("Siguiente", bgcolor=color, color=ft.Colors.BLACK, on_click=procesar_pago),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15,
                        ),
                    ],
                    spacing=8,
                ),
            ),
        )

        page.update()

    mostrar_lista()

    return contenedor

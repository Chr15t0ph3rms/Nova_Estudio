import flet as ft

from dao.eventos_dao import EventosDAO
from modelos.eventos import Eventos


def eventos(page: ft.Page):

    evento_dao = EventosDAO()

    evento_seleccionado = None


    # =============================
    # CAMPOS DEL FORMULARIO
    # =============================

    txt_nombre = ft.TextField(
        label="Nombre del evento",
        width=250
    )


    txt_fecha = ft.TextField(
        label="Fecha",
        width=250
    )


    txt_hora = ft.TextField(
        label="Hora",
        width=250
    )


    txt_calle = ft.TextField(
        label="Calle",
        width=250
    )


    txt_colonia = ft.TextField(
        label="Colonia",
        width=250
    )


    txt_numero_exterior = ft.TextField(
        label="Número Exterior",
        width=250
    )


    txt_costo = ft.TextField(
        label="Costo",
        width=250
    )


    txt_buscar = ft.TextField(
        label="Buscar evento",
        prefix_icon=ft.Icons.SEARCH,
        expand=True
    )



    # =============================
    # TABLA EVENTOS
    # =============================

    tabla_eventos = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text("ID")
            ),

            ft.DataColumn(
                ft.Text("Nombre")
            ),

            ft.DataColumn(
                ft.Text("Fecha")
            ),

            ft.DataColumn(
                ft.Text("Hora")
            ),

            ft.DataColumn(
                ft.Text("Costo")
            ),

            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]

    )

    # =============================
    # DIALOGO EVENTO
    # =============================

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nuevo Evento"
        ),

        content=ft.Column(

            [

                txt_nombre,

                txt_fecha,

                txt_hora,

                txt_calle,

                txt_colonia,

                txt_numero_exterior,

                txt_costo

            ],

            tight=True

        )

    )


    # =============================
    # CARGAR EVENTOS
    # =============================

    def cargar_eventos():

        tabla_eventos.rows.clear()

        try:

            lista_eventos = evento_dao.obtener_todo()


            for evento in lista_eventos:

                tabla_eventos.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(
                                    str(evento.id_evento)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    evento.nombre
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(evento.fecha)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(evento.hora)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(evento.costo)
                                )
                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, ev=evento:
                                                editar_evento(ev)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, ev=evento:
                                                eliminar_evento(ev)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


            page.update()


        except Exception as error:

            mostrar_mensaje(
                f"Error al cargar eventos: {error}"
            )



    # =============================
    # LIMPIAR CAMPOS
    # =============================

    def limpiar_campos():

        txt_nombre.value = ""

        txt_fecha.value = ""

        txt_hora.value = ""

        txt_calle.value = ""

        txt_colonia.value = ""

        txt_numero_exterior.value = ""

        txt_costo.value = ""

    # =============================
    # GUARDAR EVENTO
    # =============================

    def guardar_evento(e):

        try:

            nuevo_id = evento_dao.obtener_ultimo_id() + 1


            evento = Eventos(

                nuevo_id,

                txt_nombre.value,

                txt_fecha.value,

                txt_hora.value,

                txt_calle.value,

                txt_colonia.value,

                txt_numero_exterior.value,

                txt_costo.value

            )


            evento_dao.insertar(
                evento
            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_eventos()


            mostrar_mensaje(
                "Evento registrado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al guardar evento: {error}"
            )



    # =============================
    # EDITAR EVENTO
    # =============================

    def editar_evento(evento):

        nonlocal evento_seleccionado


        evento_seleccionado = evento


        txt_nombre.value = evento.nombre

        txt_fecha.value = evento.fecha

        txt_hora.value = evento.hora

        txt_calle.value = evento.calle

        txt_colonia.value = evento.colonia

        txt_numero_exterior.value = evento.numero_exterior

        txt_costo.value = evento.costo


        dialogo.title = ft.Text(
            "Editar Evento"
        )


        dialogo.actions = [

            ft.ElevatedButton(

                "Actualizar",

                icon=ft.Icons.SAVE,

                on_click=actualizar_evento

            ),


            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            )

        ]


        dialogo.open = True

        page.update()



    # =============================
    # ACTUALIZAR EVENTO
    # =============================

    def actualizar_evento(e):

        try:

            evento_actualizado = Eventos(

                evento_seleccionado.id_evento,

                txt_nombre.value,

                txt_fecha.value,

                txt_hora.value,

                txt_calle.value,

                txt_colonia.value,

                txt_numero_exterior.value,

                txt_costo.value

            )


            evento_dao.actualizar(

                evento_actualizado

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_eventos()


            mostrar_mensaje(
                "Evento actualizado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al actualizar evento: {error}"
            )

    # =============================
    # ELIMINAR EVENTO
    # =============================

    def eliminar_evento(evento):

        try:

            evento_dao.eliminar(
                evento.id_evento
            )


            cargar_eventos()


            mostrar_mensaje(
                "Evento eliminado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al eliminar evento: {error}"
            )



    # =============================
    # BUSCAR EVENTOS
    # =============================

    def buscar_eventos(e):

        texto = txt_buscar.value.lower()

        tabla_eventos.rows.clear()


        for evento in evento_dao.obtener_todo():

            nombre_evento = evento.nombre.lower()


            if texto in nombre_evento:

                tabla_eventos.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(
                                    str(evento.id_evento)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    evento.nombre
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(evento.fecha)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(evento.hora)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(evento.costo)
                                )
                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, ev=evento:
                                                editar_evento(ev)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, ev=evento:
                                                eliminar_evento(ev)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


        page.update()



    # =============================
    # NUEVO EVENTO
    # =============================

    def nuevo_evento(e):

        limpiar_campos()


        dialogo.title = ft.Text(
            "Nuevo Evento"
        )


        dialogo.actions = [

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            ),


            ft.ElevatedButton(

                "Guardar",

                icon=ft.Icons.SAVE,

                on_click=guardar_evento

            )

        ]


        page.dialog = dialogo

        dialogo.open = True

        page.update()



    # =============================
    # CERRAR DIALOGO
    # =============================

    def cerrar_dialogo():

        dialogo.open = False

        page.update()



    # =============================
    # MENSAJES
    # =============================

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )

        page.snack_bar.open = True

        page.update()



    txt_buscar.on_change = buscar_eventos


    cargar_eventos()



    # =============================
    # INTERFAZ FINAL
    # =============================

    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de Eventos",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),


                        ft.Container(

                            expand=True

                        ),


                        ft.ElevatedButton(

                            "Nuevo Evento",

                            icon=ft.Icons.ADD,

                            on_click=nuevo_evento

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_eventos

                )

            ],

            expand=True

        )

    )
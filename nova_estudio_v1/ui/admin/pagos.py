import flet as ft

from dao.pago_dao import PagoDAO
from modelos.pago import Pago


def pagos(page: ft.Page):

    pago_dao = PagoDAO()

    pago_seleccionado = None


    # CAMPOS DEL FORMULARIO

    txt_id_contrato = ft.TextField(

        label="ID Contrato",

        width=250

    )


    txt_fecha_pago = ft.TextField(

        label="Fecha de pago",

        width=250

    )


    txt_monto = ft.TextField(

        label="Monto",

        width=250

    )


    txt_estado = ft.Dropdown(

        label="Estado del pago",

        width=250,

        options=[

            ft.dropdown.Option("Pendiente"),

            ft.dropdown.Option("Pagado"),

            ft.dropdown.Option("Cancelado")

        ]

    )


    txt_buscar = ft.TextField(

        label="Buscar pago",

        prefix_icon=ft.Icons.SEARCH,

        expand=True

    )



    # TABLA PAGOS

    tabla_pagos = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text("ID")
            ),

            ft.DataColumn(
                ft.Text("Contrato")
            ),

            ft.DataColumn(
                ft.Text("Fecha")
            ),

            ft.DataColumn(
                ft.Text("Monto")
            ),

            ft.DataColumn(
                ft.Text("Estado")
            ),

            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]

    ) 


    # DIALOGO PAGO

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nuevo Pago"
        ),

        content=ft.Column(

            [

                txt_id_contrato,

                txt_fecha_pago,

                txt_monto,

                txt_estado

            ],

            tight=True

        )

    )



    # CARGAR PAGOS

    def cargar_pagos():

        tabla_pagos.rows.clear()


        try:

            lista_pagos = pago_dao.obtener_todo()


            for pago in lista_pagos:


                tabla_pagos.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(pago.id_pago)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    str(pago.id_contrato)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    str(pago.fecha_pago)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    "$ " + str(pago.monto)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    pago.estado
                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, p=pago:
                                                editar_pago(p)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, p=pago:
                                                eliminar_pago(p)

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

                f"Error al cargar pagos: {error}"

            )



    # LIMPIAR CAMPOS

    def limpiar_campos():

        txt_id_contrato.value = ""

        txt_fecha_pago.value = ""

        txt_monto.value = ""

        txt_estado.value = None 


    # GUARDAR PAGO

    def guardar_pago(e):

        try:

            nuevo_id = pago_dao.obtener_ultimo_id() + 1


            nuevo_pago = Pago(

                nuevo_id,

                int(txt_id_contrato.value),

                txt_fecha_pago.value,

                float(txt_monto.value),

                txt_estado.value

            )


            pago_dao.insertar(

                nuevo_pago

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_pagos()


            mostrar_mensaje(

                "Pago registrado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al guardar pago: {error}"

            )



    # EDITAR PAGO

    def editar_pago(pago):

        nonlocal pago_seleccionado


        pago_seleccionado = pago


        txt_id_contrato.value = str(pago.id_contrato)

        txt_fecha_pago.value = str(pago.fecha_pago)

        txt_monto.value = str(pago.monto)

        txt_estado.value = pago.estado



        dialogo.title = ft.Text(

            "Editar Pago"

        )


        dialogo.actions = [

            ft.ElevatedButton(

                "Actualizar",

                icon=ft.Icons.SAVE,

                on_click=actualizar_pago

            ),


            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            )

        ]


        dialogo.open = True

        page.update()



    # ACTUALIZAR PAGO

    def actualizar_pago(e):

        try:

            pago_actualizado = Pago(

                pago_seleccionado.id_pago,

                int(txt_id_contrato.value),

                txt_fecha_pago.value,

                float(txt_monto.value),

                txt_estado.value

            )


            pago_dao.actualizar(

                pago_actualizado

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_pagos()


            mostrar_mensaje(

                "Pago actualizado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al actualizar pago: {error}"

            ) 

    # ELIMINAR PAGO

    def eliminar_pago(pago):

        try:

            pago_dao.eliminar(

                pago.id_pago

            )


            cargar_pagos()


            mostrar_mensaje(

                "Pago eliminado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al eliminar pago: {error}"

            )



    # BUSCAR PAGO

    def buscar_pagos(e):

        texto = txt_buscar.value.lower()


        tabla_pagos.rows.clear()


        for pago in pago_dao.obtener_todo():


            if (
                texto in str(pago.id_pago).lower()
                or texto in str(pago.id_contrato).lower()
                or texto in pago.estado.lower()
            ):


                tabla_pagos.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(
                                    str(pago.id_pago)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(pago.id_contrato)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    str(pago.fecha_pago)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    "$ " + str(pago.monto)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    pago.estado
                                )
                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, p=pago:
                                                editar_pago(p)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, p=pago:
                                                eliminar_pago(p)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


        page.update()



    # NUEVO PAGO

    def nuevo_pago(e):

        limpiar_campos()


        dialogo.title = ft.Text(

            "Nuevo Pago"

        )


        dialogo.actions = [

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            ),


            ft.ElevatedButton(

                "Guardar",

                icon=ft.Icons.SAVE,

                on_click=guardar_pago

            )

        ]


        page.dialog = dialogo


        dialogo.open = True


        page.update()



    # CERRAR DIALOGO

    def cerrar_dialogo():

        dialogo.open = False

        page.update()



    # MENSAJES

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )

        page.snack_bar.open = True

        page.update()



    txt_buscar.on_change = buscar_pagos


    cargar_pagos()



    # INTERFAZ FINAL

    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de Pagos",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),


                        ft.Container(

                            expand=True

                        ),


                        ft.ElevatedButton(

                            "Nuevo Pago",

                            icon=ft.Icons.ADD,

                            on_click=nuevo_pago

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_pagos

                )

            ],

            expand=True

        )

    )
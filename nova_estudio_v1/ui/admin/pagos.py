import flet as ft

from dao.pago_dao import PagoDAO
from modelos.pago import Pago



def pagos(page: ft.Page):

    dao = PagoDAO()

    pago_actual = None


    # ==========================
    # CAMPOS DEL FORMULARIO
    # ==========================

    id_contrato = ft.TextField(
        label="ID Contrato",
        width=250
    )


    fecha_pago = ft.TextField(
        label="Fecha de Pago",
        width=250
    )


    monto = ft.TextField(
        label="Monto",
        width=250
    )


    estado = ft.TextField(
        label="Estado",
        width=250
    )



    # ==========================
    # FORMULARIO
    # ==========================

    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15,

        content=ft.Column([])

    )



    # ==========================
    # TABLA PAGOS
    # ==========================

    tabla = ft.DataTable(

        expand=True,

        column_spacing=45,

        horizontal_margin=30,


        columns=[


            ft.DataColumn(
                ft.Text("ID Pago")
            ),


            ft.DataColumn(
                ft.Text("ID Contrato")
            ),


            ft.DataColumn(
                ft.Text("Fecha Pago")
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



    # ==========================
    # LIMPIAR CAMPOS
    # ==========================

    def limpiar():

        id_contrato.value = ""

        fecha_pago.value = ""

        monto.value = ""

        estado.value = ""



    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():

        tabla.rows.clear()


        lista_pagos = dao.obtener_todo()



        for pago in lista_pagos:


            tabla.rows.append(

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
                                str(pago.monto)
                            )
                        ),


                        ft.DataCell(
                            ft.Text(
                                pago.estado
                            )
                        ),


                        ft.DataCell(

                            ft.Container(

                                width=130,

                                content=ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            icon_color=ft.Colors.BLUE_400,

                                            tooltip="Editar pago",

                                            on_click=lambda e, p=pago: editar(p)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar pago",

                                            on_click=lambda e, p=pago: eliminar(p)

                                        )

                                    ],

                                    spacing=8

                                )

                            )

                        )

                    ]

                )

            )


        page.update() 

    # ==========================
    # MOSTRAR FORMULARIO
    # ==========================

    def mostrar_formulario(titulo):

        formulario.content = ft.Column(

            [

                ft.Text(

                    titulo,

                    size=25,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE

                ),


                ft.Row(

                    [

                        id_contrato,

                        fecha_pago

                    ]

                ),


                ft.Row(

                    [

                        monto,

                        estado

                    ]

                ),


                ft.Row(

                    [

                        ft.ElevatedButton(

                            "Guardar",

                            icon=ft.Icons.SAVE,

                            on_click=guardar

                        ),


                        ft.TextButton(

                            "Cancelar",

                            on_click=cerrar_formulario

                        )

                    ]

                )

            ]

        )


        formulario.visible = True

        page.update()




    # ==========================
    # CERRAR FORMULARIO
    # ==========================

    def cerrar_formulario(e=None):

        formulario.visible = False

        limpiar()

        page.update()




    # ==========================
    # NUEVO PAGO
    # ==========================

    def nuevo_pago(e):

        nonlocal pago_actual


        pago_actual = None


        limpiar()


        mostrar_formulario(

            "Nuevo Pago"

        )




    # ==========================
    # GUARDAR PAGO
    # ==========================

    def guardar(e):

        try:


            nuevo = Pago(

                id_pago=dao.obtener_ultimo_id()+1,


                id_contrato=int(

                    id_contrato.value

                    if id_contrato.value

                    else 0

                ),


                fecha_pago=fecha_pago.value,


                monto=float(

                    monto.value

                    if monto.value

                    else 0

                ),


                estado=estado.value

            )



            dao.insertar(nuevo)



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Pago agregado correctamente"

            )



        except Exception as error:


            print("ERROR GUARDAR PAGO:", error)


            mostrar_mensaje(

                f"Error: {error}"

            )




    # ==========================
    # EDITAR PAGO
    # ==========================

    def editar(pago):

        nonlocal pago_actual


        pago_actual = pago



        id_contrato.value = str(

            pago.id_contrato

        )


        fecha_pago.value = str(

            pago.fecha_pago

        )


        monto.value = str(

            pago.monto

        )


        estado.value = pago.estado



        mostrar_formulario(

            "Editar Pago"

        )



        formulario.content.controls[-1].controls[0].text = "Actualizar"


        formulario.content.controls[-1].controls[0].on_click = actualizar


        page.update()




    # ==========================
    # ACTUALIZAR PAGO
    # ==========================

    def actualizar(e):

        try:


            pago_actual.id_contrato = int(

                id_contrato.value

                if id_contrato.value

                else 0

            )


            pago_actual.fecha_pago = fecha_pago.value


            pago_actual.monto = float(

                monto.value

                if monto.value

                else 0

            )


            pago_actual.estado = estado.value



            dao.actualizar(

                pago_actual

            )



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Pago actualizado correctamente"

            )



        except Exception as error:


            print("ERROR ACTUALIZAR PAGO:", error)


            mostrar_mensaje(

                f"Error al actualizar: {error}"

            ) 

    # ==========================
    # MENSAJES
    # ==========================

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )


        page.snack_bar.open = True

        page.update()




    # ==========================
    # ELIMINAR PAGO
    # ==========================

    def eliminar(pago):


        def aceptar(e):

            dao.eliminar(

                pago.id_pago

            )


            dialogo_eliminar.open = False


            page.update()


            cargar()


            mostrar_mensaje(

                "Pago eliminado correctamente"

            )



        def cancelar(e):

            dialogo_eliminar.open = False

            page.update()



        dialogo_eliminar = ft.AlertDialog(

            modal=True,


            title=ft.Text(

                "Eliminar pago"

            ),


            content=ft.Text(

                "¿Seguro que deseas eliminar este pago?"

            ),


            actions=[


                ft.TextButton(

                    "Cancelar",

                    on_click=cancelar

                ),



                ft.ElevatedButton(

                    "Aceptar",

                    icon=ft.Icons.DELETE,

                    on_click=aceptar

                )

            ]

        )


        page.dialog = dialogo_eliminar

        dialogo_eliminar.open = True

        page.update()




    # ==========================
    # BOTÓN NUEVO PAGO
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nuevo Pago",

        icon=ft.Icons.ADD,

        on_click=nuevo_pago

    )




    # ==========================
    # CARGAR DATOS INICIALES
    # ==========================

    cargar()




    # ==========================
    # INTERFAZ FINAL
    # ==========================

    return ft.Container(

        expand=True,

        padding=20,


        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de Pagos",

                            size=30,

                            weight=ft.FontWeight.BOLD,

                            color=ft.Colors.WHITE

                        ),



                        ft.Container(

                            expand=True

                        ),



                        boton_nuevo

                    ]

                ),



                ft.Divider(),



                formulario,



                ft.Container(

                    height=0

                ),



                ft.Container(

                    padding=0,

                    content=ft.Column(

                        [

                            tabla

                        ],

                        spacing=0

                    )

                )

            ],


            expand=True,

            spacing=0

        )

    )
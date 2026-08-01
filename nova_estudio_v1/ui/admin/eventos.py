import flet as ft

from dao.eventos_dao import EventosDAO
from modelos.eventos import Eventos



def eventos(page: ft.Page):

    dao = EventosDAO()

    evento_actual = None



    # ==========================
    # CAMPOS DEL FORMULARIO
    # ==========================

    nombre = ft.TextField(
        label="Nombre del Evento",
        width=250
    )


    fecha = ft.TextField(
        label="Fecha",
        width=250
    )


    hora = ft.TextField(
        label="Hora",
        width=250
    )


    calle = ft.TextField(
        label="Calle",
        width=250
    )


    colonia = ft.TextField(
        label="Colonia",
        width=250
    )


    numero_exterior = ft.TextField(
        label="Número Exterior",
        width=250
    )


    costo = ft.TextField(
        label="Costo",
        width=250
    )



    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15

    )



    # ==========================
    # TABLA EVENTOS
    # ==========================

    tabla = ft.DataTable(

        expand=True,

        column_spacing=45,

        horizontal_margin=30,


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
                ft.Text("Calle")
            ),


            ft.DataColumn(
                ft.Text("Colonia")
            ),


            ft.DataColumn(
                ft.Text("Número")
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




    # ==========================
    # LIMPIAR
    # ==========================

    def limpiar():

        nombre.value = ""

        fecha.value = ""

        hora.value = ""

        calle.value = ""

        colonia.value = ""

        numero_exterior.value = ""

        costo.value = ""




    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():

        tabla.rows.clear()


        eventos_lista = dao.obtener_todo()



        for evento in eventos_lista:


            tabla.rows.append(

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

                                evento.calle

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                evento.colonia

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                str(evento.numero_exterior)

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                str(evento.costo)

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

                                            tooltip="Editar evento",

                                            on_click=lambda e, ev=evento: editar(ev)

                                        ),



                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar evento",

                                            on_click=lambda e, ev=evento: eliminar(ev)

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

                        nombre,

                        fecha

                    ]

                ),



                ft.Row(

                    [

                        hora,

                        calle

                    ]

                ),



                ft.Row(

                    [

                        colonia,

                        numero_exterior

                    ]

                ),



                ft.Row(

                    [

                        costo

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
    # NUEVO EVENTO
    # ==========================

    def nuevo_evento(e):

        nonlocal evento_actual


        evento_actual = None


        limpiar()


        mostrar_formulario(

            "Nuevo Evento"

        )




    # ==========================
    # GUARDAR EVENTO
    # ==========================

    def guardar(e):

        try:


            nuevo = Eventos(

                id_evento=dao.obtener_ultimo_id()+1,


                nombre=nombre.value,


                fecha=fecha.value,


                hora=hora.value,


                calle=calle.value,


                colonia=colonia.value,


                numero_exterior=int(

                    numero_exterior.value

                    if numero_exterior.value

                    else 0

                ),


                costo=float(

                    costo.value

                    if costo.value

                    else 0

                )

            )



            dao.insertar(nuevo)



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Evento agregado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error: {error}"

            )





    # ==========================
    # EDITAR EVENTO
    # ==========================

    def editar(evento):

        nonlocal evento_actual


        evento_actual = evento



        nombre.value = evento.nombre


        fecha.value = str(evento.fecha)


        hora.value = str(evento.hora)


        calle.value = evento.calle


        colonia.value = evento.colonia


        numero_exterior.value = str(

            evento.numero_exterior

        )


        costo.value = str(

            evento.costo

        )



        mostrar_formulario(

            "Editar Evento"

        )



        formulario.content.controls[-1].controls[0].text = "Actualizar"


        formulario.content.controls[-1].controls[0].on_click = actualizar



        page.update()




    # ==========================
    # ACTUALIZAR EVENTO
    # ==========================

    def actualizar(e):

        try:


            evento_actual.nombre = nombre.value


            evento_actual.fecha = fecha.value


            evento_actual.hora = hora.value


            evento_actual.calle = calle.value


            evento_actual.colonia = colonia.value



            evento_actual.numero_exterior = int(

                numero_exterior.value

                if numero_exterior.value

                else 0

            )



            evento_actual.costo = float(

                costo.value

                if costo.value

                else 0

            )



            dao.actualizar(

                evento_actual

            )



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Evento actualizado correctamente"

            )



        except Exception as error:


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
    # ELIMINAR EVENTO
    # ==========================

    def eliminar(evento):

        print(
            "BOTON ELIMINAR EVENTO:",
            evento.id_evento
        )


        def aceptar(e):

            try:

                print(
                    "ELIMINANDO EVENTO:",
                    evento.id_evento
                )


                dao.eliminar(

                    evento.id_evento

                )


                dialogo_eliminar.open = False

                page.update()


                cargar()


                mostrar_mensaje(

                    "Evento eliminado correctamente"

                )


            except Exception as error:


                print(

                    "ERROR AL ELIMINAR EVENTO:",
                    error

                )


                mostrar_mensaje(

                    f"Error al eliminar: {error}"

                )



        def cancelar(e):

            dialogo_eliminar.open = False

            page.update()



        dialogo_eliminar = ft.AlertDialog(

            modal=True,


            title=ft.Text(

                "Eliminar evento"

            ),


            content=ft.Text(

                f"¿Seguro que deseas eliminar el evento {evento.nombre}?"

            ),


            actions=[


                ft.TextButton(

                    "Cancelar",

                    on_click=cancelar

                ),



                ft.TextButton(

                    "Eliminar",

                    icon=ft.Icons.DELETE,

                    on_click=aceptar

                )

            ]

        )


        page.overlay.append(dialogo_eliminar)


        dialogo_eliminar.open = True


        page.update()




    # ==========================
    # BOTÓN NUEVO EVENTO
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nuevo Evento",

        icon=ft.Icons.ADD,

        on_click=nuevo_evento

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

                            "Gestión de Eventos",

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
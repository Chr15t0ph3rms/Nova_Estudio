from database.conexion import Conexion
from modelos.paquetes import Paquetes


class PaquetesDAO:


    # SELECT

    def obtener_todo(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        cursor.execute(
            "SELECT * FROM paquete"
        )


        registros = cursor.fetchall()


        paquetes = []


        for registro in registros:

            paquete = Paquetes(

                id_paquetes=registro[0],

                nombre=registro[1],

                tipo_paquete=registro[2],

                costo=registro[3],

                descripcion=registro[4]

            )


            paquetes.append(paquete)



        cursor.close()
        conexion.close()


        return paquetes



    # INSERT

    def insertar(self, paquete):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        sql = """

        INSERT INTO paquete(

            id_paquetes,

            nombre,

            tipo_paquete,

            costo,

            descripcion

        )

        VALUES(%s,%s,%s,%s,%s)

        """


        cursor.execute(sql, (

            paquete.id_paquetes,

            paquete.nombre,

            paquete.tipo_paquete,

            paquete.costo,

            paquete.descripcion

        ))


        conexion.commit()


        cursor.close()
        conexion.close()


    # UPDATE

    def actualizar(self, paquete):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        sql = """

        UPDATE paquete

        SET

            nombre=%s,

            tipo_paquete=%s,

            costo=%s,

            descripcion=%s


        WHERE id_paquetes=%s

        """


        cursor.execute(sql, (

            paquete.nombre,

            paquete.tipo_paquete,

            paquete.costo,

            paquete.descripcion,

            paquete.id_paquetes

        ))


        conexion.commit()


        cursor.close()
        conexion.close()




        # DELETE

    def eliminar(self, id_paquetes):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                DELETE FROM paquete
                WHERE id_paquetes = %s
                """,
                (id_paquetes,)
            )


            conexion.commit()


        except Exception as error:


            conexion.rollback()


            mensaje = str(error)


            if "fk_paquetes" in mensaje:

                raise Exception(
                    "No se puede eliminar el paquete porque está siendo usado en un contrato."
                )


            else:

                raise Exception(
                    f"Error al eliminar paquete: {error}"
                )


        finally:

            cursor.close()

            conexion.close()




    # ULTIMO ID

    def obtener_ultimo_id(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        cursor.execute(

            "SELECT MAX(id_paquetes) FROM paquete"

        )


        resultado = cursor.fetchone()


        cursor.close()
        conexion.close()



        if resultado[0] is None:

            return 0



        return resultado[0]
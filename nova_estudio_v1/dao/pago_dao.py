from database.conexion import Conexion
from modelos.pago import Pago


class PagoDAO:


    # SELECT

    def obtener_todo(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pago")
        registros = cursor.fetchall()
        pagos = []


        for registro in registros:

            pago = Pago(

                id_pago = registro[0],
                id_contrato = registro[1],
                fecha_pago = registro[2],
                monto = registro[3],
                estado = registro[4]

            )


            pagos.append(pago)


        cursor.close()
        conexion.close()


        return pagos



    # INSERT

    def insertar(self, pago):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        sql = """
        INSERT INTO pago(
            id_pago,
            id_contrato,
            fecha_pago,
            monto,
            estado
        )
        VALUES(%s,%s,%s,%s,%s)
        """


        cursor.execute(sql, (

            pago.id_pago,
            pago.id_contrato,
            pago.fecha_pago,
            pago.monto,
            pago.estado

        ))


        conexion.commit()

        cursor.close()
        conexion.close()



    # UPDATE

    def actualizar(self, pago):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        sql = """
        UPDATE pago
        SET id_contrato = %s,
            fecha_pago = %s,
            monto = %s,
            estado = %s
        WHERE id_pago = %s
        """


        cursor.execute(sql, (

            pago.id_contrato,
            pago.fecha_pago,
            pago.monto,
            pago.estado,
            pago.id_pago

        ))


        conexion.commit()

        cursor.close()
        conexion.close()

    # DELETE

    def eliminar(self, id_pago):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        cursor.execute(
            "DELETE FROM pago WHERE id_pago = %s",
            (id_pago,)
        )


        conexion.commit()

        cursor.close()
        conexion.close()



    # ULTIMO ID

    def obtener_ultimo_id(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()


        cursor.execute(
            "SELECT MAX(id_pago) FROM pago"
        )


        resultado = cursor.fetchone()


        cursor.close()
        conexion.close()


        if resultado[0] is None:

            return 0


        return resultado[0]
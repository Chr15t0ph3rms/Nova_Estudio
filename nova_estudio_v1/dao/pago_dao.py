from database.conexion import Conexion
from modelos.pago import Pago

class PagoDAO:

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
                estado = registro[4],
                id_cliente = registro[5] if len(registro) > 5 else None,
                id_evento = registro[6] if len(registro) > 6 else None

            )

            pagos.append(pago)

        cursor.close()
        conexion.close()

        return pagos

    # SELECT solo los pagos de un cliente en específico

    def obtener_por_cliente(self, id_cliente):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM pago WHERE id_cliente = %s ORDER BY id_pago DESC",
            (id_cliente,)
        )

        registros = cursor.fetchall()
        pagos = []

        for registro in registros:
            pago = Pago(
                id_pago = registro[0],
                id_contrato = registro[1],
                fecha_pago = registro[2],
                monto = registro[3],
                estado = registro[4],
                id_cliente = registro[5] if len(registro) > 5 else None,
                id_evento = registro[6] if len(registro) > 6 else None
            )
            pagos.append(pago)

        cursor.close()
        conexion.close()

        return pagos

    def insertar(self, pago):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO pago(
            id_pago,
            id_contrato,
            fecha_pago,
            monto,
            estado,
            id_cliente,
            id_evento
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (

            pago.id_pago,
            pago.id_contrato,
            pago.fecha_pago,
            pago.monto,
            pago.estado,
            pago.id_cliente,
            pago.id_evento

        ))

        conexion.commit()

        cursor.close()
        conexion.close()

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

    # Cambiar el estado del pago asociado a un evento (ej. al cancelar el evento)

    def actualizar_estado_por_evento(self, id_evento, nuevo_estado):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "UPDATE pago SET estado = %s WHERE id_evento = %s",
            (nuevo_estado, id_evento)
        )

        conexion.commit()

        cursor.close()
        conexion.close()

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

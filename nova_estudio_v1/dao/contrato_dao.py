from database.conexion import Conexion
from modelos.contrato import Contrato

class ContratoDAO:

    #SELECT * FROM contrato
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM contrato")
        registros = cursor.fetchall()

        contratos = []
        for registro in registros : 
            contrato = Contrato(
                id_contrato = registro[0],
                fecha_firma = registro[1],
                costo = registro[2],
                paquetes = registro[3]
            )
            contratos.append(contrato)
        cursor.close()
        conexion.close()
        return contratos

    # INSERT
    def insertar(self, contrato):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO contrato(id_contrato, fecha_firma, costo, paquetes)
        VALUES(%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            contrato.id_contrato,
            contrato.fecha_firma,
            contrato.costo,
            contrato.paquetes
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, contrato):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE contrato
        SET fecha_firma = %s, costo = %s, paquetes = %s
        WHERE id_contrato = %s
        """

        cursor.execute(sql, (
            contrato.fecha_firma,
            contrato.costo,
            contrato.paquetes,
            contrato.id_contrato
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM contrato WHERE id_contrato = %s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()


    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id_contrato) FROM contrato")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0
        return resultado[0]
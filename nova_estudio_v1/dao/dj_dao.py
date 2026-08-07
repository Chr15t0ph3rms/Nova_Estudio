from database.conexion import Conexion
from modelos.dj import Dj

class DjDAO:

    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM dj")
        registros = cursor.fetchall()

        djs = []

        for registro in registros:
            dj = Dj(
                id_dj = registro[0],
                nombre = registro[1],
                app = registro[2],
                apm = registro[3],
                telefono = registro[4],
                especialidad = registro[5],
                disponibilidad = registro[6],
                tarifa_hora = registro[7] if len(registro) > 7 and registro[7] is not None else 500
            )

            djs.append(dj)

        cursor.close()
        conexion.close()

        return djs

    def insertar(self, dj):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO dj(
            id_dj,
            nombre,
            app,
            apm,
            telefono,
            especialidad,
            disponibilidad
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (

            dj.id_dj,
            dj.nombre,
            dj.app,
            dj.apm,
            dj.telefono,
            dj.especialidad,
            dj.disponibilidad

        ))

        conexion.commit()

        cursor.close()
        conexion.close()

    def actualizar(self, dj):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE dj
        SET nombre = %s,
            app = %s,
            apm = %s,
            telefono = %s,
            especialidad = %s,
            disponibilidad = %s
        WHERE id_dj = %s
        """

        cursor.execute(sql, (

            dj.nombre,
            dj.app,
            dj.apm,
            dj.telefono,
            dj.especialidad,
            dj.disponibilidad,
            dj.id_dj

        ))

        conexion.commit()

        cursor.close()
        conexion.close()

    def eliminar(self, id):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM dj WHERE id_dj = %s",
            (id,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT MAX(id_dj) FROM dj"
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:

            return 0

        return resultado[0]

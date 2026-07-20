from database.conexion import Conexion
from modelos.agencia import Agencia

class AgenciaDAO:

    #SELECT * FROM agencia
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM agencia")
        registros = cursor.fetchall()

        agencias = []
        for registro in registros : 
            agencia = Agencia(
                id_agencia = registro[0],
                agencia_nombre = registro[1],
                nombre = registro[2],
                app = registro[3],
                apm = registro[4],
                telefono = registro[5],
                correo = registro[6],
                empleados = registro[7]
            )
            agencias.append(agencia)
        cursor.close()
        conexion.close()
        return agencias

    # INSERT
    def insertar(self, agencia):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO agencia(id_agencia, agencia_nombre, nombre, app, apm, telefono, correo, empleados)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            agencia.id_agencia,
            agencia.agencia_nombre,
            agencia.nombre,
            agencia.app,
            agencia.apm,
            agencia.telefono,
            agencia.correo,
            agencia.empleados
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, agencia):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE agencia
        SET agencia_nombre = %s, nombre = %s, app = %s, apm = %s, telefono = %s, correo = %s, empleados = %s
        WHERE id_agencia = %s
        """

        cursor.execute(sql, (
            agencia.agencia_nombre,
            agencia.nombre,
            agencia.app,
            agencia.apm,
            agencia.telefono,
            agencia.correo,
            agencia.empleados,
            agencia.id_agencia
                        ) )
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM agencia WHERE id_agencia = %s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()


    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id_agencia) FROM agencia")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0
        return resultado[0]
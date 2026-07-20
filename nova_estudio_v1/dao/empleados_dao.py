from database.conexion import Conexion
from modelos.empleados import Empleados

class EmpleadosDAO:

    #SELECT * FROM empleado
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM empleados")
        registros = cursor.fetchall()

        empleados = []
        for registro in registros : 
            empleado = Empleados(
                id_empleado = registro[0],
                nombre = registro[1],
                app = registro[2],
                apm = registro[3],
                puesto = registro[4],
                telefono = registro[5]
            )
            empleados.append(empleado)
        cursor.close()
        conexion.close()
        return empleados

    # INSERT
    def insertar(self, empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO empleados(id_empleado, nombre, app, apm, puesto, telefono)
        VALUES(%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            empleado.id_empleado,
            empleado.nombre,
            empleado.app,
            empleado.apm,
            empleado.puesto,
            empleado.telefono
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE empleados
        SET nombre = %s, app = %s, apm = %s, puesto = %s, telefono = %s
        WHERE id_empleado = %s
        """

        cursor.execute(sql, (
                        empleado.nombre,
                        empleado.app,
                        empleado.apm,
                        empleado.puesto,
                        empleado.telefono,
                        empleado.id_empleado
                        ) )
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self,id):
       conexion = Conexion.obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute("DELETE FROM empleados WHERE id_empleado = %s",(id,))

       conexion.commit()
       cursor.close()
       conexion.close()


    def obtener_ultimo_id(self):
       conexion = Conexion.obtener_conexion()
       cursor = conexion.cursor()

       cursor.execute("SELECT MAX(id_empleado) FROM empleados")
       resultado = cursor.fetchone()

       cursor.close()
       conexion.close()

       if resultado[0] is None:
           return 0
       return resultado[0] 



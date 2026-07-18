class Empleado    :
    
    #Constructor
    def __init__(self, id_empleados, nombre, app, apm, puesto, telefono):
        self.id_empleados = id_empleados
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.puesto = puesto
        self.telefono = telefono

    def mostrar_info(self):
        return f"ID: {self.id_empleados}, Nombre: {self.nombre}, Apellido Paterno: {self.app}, Apellido Materno: {self.apm}, Puesto: {self.puesto}, Teléfono: {self.telefono}"
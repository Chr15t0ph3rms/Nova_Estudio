class Agencia:
    
    #Constructor
    def __init__(self, id_agencia, agencia_nombre, nombre, app, apm, telefono, correo, empleados):
        self.id_agencia = id_agencia
        self.agencia_nombre = agencia_nombre
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.telefono = telefono
        self.correo = correo
        self.empleados = empleados

    def mostrar_info(self):
        return f"ID: {self.id_agencia}, Agencia_nombre: {self.agencia_nombre}, Nombre: {self.nombre}, Apellido Paterno: {self.app}, Apellido Materno: {self.apm}, Teléfono: {self.telefono}, Correo: {self.correo}, Empleados: {self.empleados}"
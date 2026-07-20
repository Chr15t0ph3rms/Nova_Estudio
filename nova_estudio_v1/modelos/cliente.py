class Cliente:
    
    #Constructor
    def __init__(self, id_cliente, nombre, app, apm, telefono, correo, calle, colonia, numero_exterior):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.telefono = telefono
        self.correo = correo
        self.calle = calle
        self.colonia = colonia
        self.numero_exterior = numero_exterior

    def mostrar_info(self):
        return f"ID: {self.id_cliente}, Nombre: {self.nombre}, Apellido Paterno: {self.app}, Apellido Materno: {self.apm}, Teléfono: {self.telefono}, Correo: {self.correo}, Calle: {self.calle}, Colonia: {self.colonia}, Número Exterior: {self.numero_exterior}"
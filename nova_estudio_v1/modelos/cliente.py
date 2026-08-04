class Cliente:
    def __init__(self, id_cliente, nombre, app, apm, telefono, correo, calle, numero_exterior, colonia):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.telefono = telefono
        self.correo = correo
        self.calle = calle
        self.numero_exterior = numero_exterior
        self.colonia = colonia

    def mostrar_info(self):
        return (
            f"ID: {self.id_cliente}, "
            f"Nombre: {self.nombre}, "
            f"Apellido Paterno: {self.app}, "
            f"Apellido Materno: {self.apm}, "
            f"Teléfono: {self.telefono}, "
            f"Correo: {self.correo}, "
            f"Calle: {self.calle}, "
            f"Número Exterior: {self.numero_exterior}, "
            f"Colonia: {self.colonia}"
        )

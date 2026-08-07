class Eventos:

    def __init__(self, id_evento, nombre, fecha, hora, calle, colonia, numero_exterior, costo, id_cliente=None, estado="En proceso"):
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.calle = calle
        self.colonia = colonia
        self.numero_exterior = numero_exterior
        self.costo = costo
        self.id_cliente = id_cliente
        self.estado = estado

    def mostrar_info(self):
        return f"ID: {self.id_evento}, Nombre: {self.nombre}, Fecha: {self.fecha}, Hora: {self.hora}, Calle: {self.calle}, Colonia: {self.colonia}, Número Exterior: {self.numero_exterior}, Costo: {self.costo}, Estado: {self.estado}"

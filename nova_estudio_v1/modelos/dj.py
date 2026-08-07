class Dj:

    def __init__(
        self,
        id_dj,
        nombre,
        app,
        apm,
        telefono,
        especialidad,
        disponibilidad,
        tarifa_hora=500
    ):

        self.id_dj = id_dj
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.telefono = telefono
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
        self.tarifa_hora = tarifa_hora

    def mostrar_info(self):

        disponibilidad = (
            "Disponible"
            if self.disponibilidad
            else "No disponible"
        )

        return (
            f"ID: {self.id_dj}, "
            f"Nombre: {self.nombre}, "
            f"Apellido Paterno: {self.app}, "
            f"Apellido Materno: {self.apm}, "
            f"Teléfono: {self.telefono}, "
            f"Especialidad: {self.especialidad}, "
            f"Disponibilidad: {disponibilidad}"
        )

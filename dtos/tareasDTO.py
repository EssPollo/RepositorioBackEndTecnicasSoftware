class TareasDTO:
    id:int
    titulo:str
    descripcion:str
    fecha_entrega:str
    prioridad:str
    tiempo:str


class TareasDTO:
    def __init__(self, id=None, titulo=None, descripcion=None, fecha_entrega=None, prioridad=None, tiempo=None):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad
        self.tiempo = tiempo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def fecha_entrega(self):
        return self._fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, value):
        self._fecha_entrega = value

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, value):
        self._prioridad = value

    @property
    def tiempo(self):
        return self._tiempo

    @tiempo.setter
    def tiempo(self, value):
        self._tiempo = value

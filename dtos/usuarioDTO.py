class UsuarioDTO():
    id:int
    nombre:str 
    apellidoP:str
    apellidoM:str
    correo:str
    contrasena:str

    def __init__(self, nombre:str, apellidoP:str, apellidoM:str, correo:str, contrasena:str):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.correo = correo
        self.contrasena = contrasena

    # Getters (@property) and Setters(<nombre>.setter)

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def apellidoP(self):
        return self._apellidoP
    @apellidoP.setter
    def apellidoP(self, apellidoP):
        self._apellidoP = apellidoP
    @property
    def apellidoM(self):
        return self._apellidoM
    @apellidoM.setter
    def apellidoM(self, apellidoM):
        self._apellidoM = apellidoM
    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, correo):
        self._correo = correo
    @property
    def contrasena(self):
        return self._contrasena
    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena
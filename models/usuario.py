from models.configDataBase import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64))
    apellidoP=db.Column(db.String(64))
    apellidoM=db.Column(db.String(64))
    correo=db.Column(db.String(64))
    contrasena=db.Column(db.String(64))
    
    def __repr__(self):
        return '<Usuario %r>' %self.nombre
    
    def obtenerTodos(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def obtenerPorId(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
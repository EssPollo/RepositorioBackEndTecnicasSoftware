from configDataBase import db

class Tarea(db.Model):
    __tablename__ = 'tarea'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    fecha_entrega = db.Column(db.Date)
    prioridad = db.Column(db.String(50))
    tiempo = db.Column(db.Integer)  # Supongo que el tiempo está en minutos

    def __repr__(self):
        return f'<Tarea {self.titulo}>'

    def obtenerTodos(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def obtenerPorId(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Saludo(db.Model):
    __tablename__ = 'saludos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mensaje = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'mensaje': self.mensaje
        }

from flask import Flask, request, jsonify, abort
from models import db, Saludo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@db:5432/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear las tablas cuando la aplicación arranque
with app.app_context():
    db.create_all()

@app.route('/saludos', methods=['GET'])
def get_saludos():
    saludos = Saludo.query.all()
    return jsonify([saludo.serialize() for saludo in saludos])

@app.route('/saludos', methods=['POST'])
def add_saludo():
    if not request.is_json:
        abort(415, description="Content-Type must be application/json")
    data = request.get_json()
    if 'mensaje' not in data:
        abort(400, description="Debe proporcionar el campo 'mensaje'")
    mensaje = data['mensaje']
    nuevo_saludo = Saludo(mensaje=mensaje)
    db.session.add(nuevo_saludo)
    db.session.commit()
    return jsonify(nuevo_saludo.serialize()), 201

@app.route('/saludos/<int:id>', methods=['GET'])
def get_saludo(id):
    saludo = Saludo.query.get(id)
    if saludo is None:
        abort(404, description="Saludo no encontrado")
    return jsonify(saludo.serialize())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

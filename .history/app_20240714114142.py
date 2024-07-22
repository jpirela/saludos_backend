from flask import Flask, request, jsonify, abort
from models import db, Saludo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@db/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Flag to ensure tables are created only once
tables_created = False

@app.before_request
def create_tables():
    global tables_created
    if not tables_created:
        db.create_all()
        tables_created = True

@app.route('/saludos', methods=['GET'])
def get_saludos():
    saludos = Saludo.query.all()
    return jsonify([saludo.serialize() for saludo in saludos])

@app.route('/saludos', methods=['POST'])
def add_saludo():
    if not request.json or 'mensaje' not in request.json:
        abort(400, description="Debe proporcionar el campo 'mensaje'")
    mensaje = request.json['mensaje']
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
    app.run(host="0.0.0.0", port=5000, debug=True)

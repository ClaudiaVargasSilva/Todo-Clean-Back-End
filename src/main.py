"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Trabajador
#from trabajador import db, Trabajador
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/proyecto_final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/signup', methods=['POST'])
def create_user():
    
    email = request.json.get('email')
    rut = request.json.get('rut')
    name = request.json.get('name')
    last_name = request.json.get('last_name')
    address = request.json.get('address')
    phone = request.json.get('phone')
    birth_date = request.json.get('birth_date')
    gender = request.json.get('gender')
    password = request.json.get('password')
    is_active = request.json.get('is_active')
    
    user = User()

    user.email = email
    user.rut = rut
    user.name = name
    user.last_name = last_name
    user.address = address
    user.birth_date = birth_date
    user.gender = gender
    user.password = password
    user.is_active = is_active
    user.phone = phone

    user.save()


    return jsonify({"msg":"usuario creado"}), 200


@app.route('/new/trabajaconnosotros', methods=['POST'])
def create_trabajador():
    
    email = request.json.get('email')
    rut = request.json.get('rut')
    name = request.json.get('name')
    last_name = request.json.get('last_name')
    address = request.json.get('address')
    birth_date = request.json.get('birth_date')
    gender = request.json.get('gender')
    password = request.json.get('password')
    is_active = request.json.get('is_active')
    phone = request.json.get('phone')

    trabajador = Trabajador()
    
    trabajador.email = email
    trabajador.rut = rut
    trabajador.name = name
    trabajador.last_name = last_name
    trabajador.address = address
    trabajador.birth_date = birth_date
    trabajador.gender = gender
    trabajador.password = password
    trabajador.is_active = is_active
    trabajador.phone = phone

    trabajador.save()

    return jsonify({"msg":"trabajador creado, bienvenido/a"}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
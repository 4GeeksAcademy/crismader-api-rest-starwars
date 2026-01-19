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
from models import db, User, Character, Planet, Film, Vehicle, Specie
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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

#Conseguir la lista de los elementos que estamos queriendo ver
@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    results_users = list(map(lambda user: user.serialize(), all_users))

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "users": results_users
    }

    return jsonify(response_body), 200

@app.route('/character', methods=['GET'])
def get_characters():
    all_characters = Character.query.all()
    results_characters = list(map(lambda char: char.serialize(), all_characters))

    response_body = {
        "msg": "Hello, this is your GET /character response ",
        "characters": results_characters
    }

    return jsonify(response_body), 200

@app.route('/planet', methods=['GET'])
def get_planets():
    all_planets = Planet.query.all()
    results_planets = list(map(lambda planet: planet.serialize(), all_planets))

    response_body = {
        "msg": "Hello, this is your GET /planet response ",
        "planets": results_planets
    }

    return jsonify(response_body), 200

@app.route('/film', methods=['GET'])
def get_films():
    all_films = Film.query.all()
    results_films = list(map(lambda film: film.serialize(), all_films))

    response_body = {
        "msg": "Hello, this is your GET /film response ",
        "films": results_films
    }

    return jsonify(response_body), 200

@app.route('/vehicle', methods=['GET'])
def get_vehicles():
    all_vehicles = Vehicle.query.all()
    results_vehicles = list(map(lambda vehicle: vehicle.serialize(), all_vehicles))

    response_body = {
        "msg": "Hello, this is your GET /film response ",
        "vehicles": results_vehicles
    }

    return jsonify(response_body), 200

@app.route('/specie', methods=['GET'])
def get_species():
    all_species = Specie.query.all()
    results_species = list(map(lambda specie: specie.serialize(), all_species))

    response_body = {
        "msg": "Hello, this is your GET /film response ",
        "species": results_species
    }

    return jsonify(response_body), 200

#Conseguir un elemento en especifico de la lista para poder modificarla o borrarla.

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({"msg": "User not found"}), 404

    response_body = {
        "msg": "Hello, this is your GET /user/<id> response",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get(character_id)

    if character is None:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({
        "msg": "Hello, this is your GET /character/<id> response",
        "character": character.serialize()
    }), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({
        "msg": "Hello, this is your GET /planet/<id> response",
        "planet": planet.serialize()
    }), 200

@app.route('/film/<int:film_id>', methods=['GET'])
def get_film(film_id):
    film = Film.query.get(film_id)

    if film is None:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({
        "msg": "Hello, this is your GET /film/<id> response",
        "film": film.serialize()
    }), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)

    if vehicle is None:
        return jsonify({"msg": "Vehicle not found"}), 404

    return jsonify({
        "msg": "Hello, this is your GET /vehicle/<id> response",
        "vehicle": vehicle.serialize()
    }), 200

@app.route('/specie/<int:specie_id>', methods=['GET'])
def get_specie(specie_id):
    specie = Specie.query.get(specie_id)

    if specie is None:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({
        "msg": "Hello, this is your GET /specie/<id> response",
        "specie": specie.serialize()
    }), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

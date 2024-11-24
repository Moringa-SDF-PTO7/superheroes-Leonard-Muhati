# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# # from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate

# # Initialize app
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize extensions
# db = SQLAlchemy()
# db.init_app(app)
# # ma = Marshmallow(app)
# migrate = Migrate(app, db)


# @app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the Superheroes !"}), 200


# @app.route('/heroes', methods=['GET'])
# def get_heroes():
#     from models import Hero  # Import inside the route to avoid circular import
#     heroes = Hero.query.all()
#     return jsonify([hero.to_dict() for hero in heroes]), 200


# @app.route('/heroes/<int:id>', methods=['GET'])
# def get_hero(id):
#     from models import Hero  # Import inside the route to avoid circular import
#     hero = Hero.query.get(id)
#     if not hero:
#         return jsonify({"error": "Hero not found"}), 404
#     return jsonify(hero.to_dict()), 200


# @app.route('/powers', methods=['GET'])
# def get_powers():
#     from models import Power  # Import inside the route to avoid circular import
#     powers = Power.query.all()
#     return jsonify([power.to_dict() for power in powers]), 200


# @app.route('/powers/<int:id>', methods=['GET'])
# def get_power(id):
#     from models import Power  # Import inside the route to avoid circular import
#     power = Power.query.get(id)
#     if not power:
#         return jsonify({"error": "Power not found"}), 404
#     return jsonify(power.to_dict()), 200


# @app.route('/powers/<int:id>', methods=['PATCH'])
# def update_power(id):
#     from models import Power  # Import inside the route to avoid circular import
#     power = Power.query.get(id)
#     if not power:
#         return jsonify({"error": "Power not found"}), 404

#     data = request.json
#     description = data.get('description')

#     if description and len(description) >= 20:
#         power.description = description
#         db.session.commit()
#         return jsonify(power.to_dict()), 200
#     else:
#         return jsonify({"errors": ["Validation error: description must be at least 20 characters"]}), 400


# @app.route('/hero_powers', methods=['POST'])
# def create_hero_power():
#     from models import Hero, Power, HeroPower  # Import inside the route to avoid circular import
#     data = request.json
#     strength = data.get('strength')
#     hero_id = data.get('hero_id')
#     power_id = data.get('power_id')

#     if not all([strength, hero_id, power_id]):
#         return jsonify({"errors": ["Missing required fields"]}), 400

#     if strength not in ['Strong', 'Weak', 'Average']:
#         return jsonify({"errors": ["Validation error: invalid strength value"]}), 400

#     hero = Hero.query.get(hero_id)
#     power = Power.query.get(power_id)

#     if not hero or not power:
#         return jsonify({"errors": ["Validation error: Hero or Power not found"]}), 400

#     hero_power = HeroPower(strength=strength, hero=hero, power=power)
#     db.session.add(hero_power)
#     db.session.commit()

#     return jsonify(hero_power.to_dict()), 201


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


from flask import Flask, jsonify, request
from flask_migrate import Migrate
from database import db  # Import from the new file

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Import models after initializing `db` to avoid circular imports
from models import Hero, Power, HeroPower

# Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Superheroes !"}), 200


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        } for hero in heroes
    ]), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name
    }), 200



@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([
        {
            "id": power.id,
            "name": power.name,
            "description": power.description
        } for power in powers
    ]), 200


@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    }), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.json
    description = data.get('description')

    if description and len(description) >= 20:
        power.description = description
        db.session.commit()
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200
    else:
        return jsonify({"errors": ["Validation error: description must be at least 20 characters"]}), 400


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    if not all([strength, hero_id, power_id]):
        return jsonify({"errors": ["Missing required fields"]}), 400

    if strength not in ['Strong', 'Weak', 'Average']:
        return jsonify({"errors": ["Validation error: invalid strength value"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["Validation error: Hero or Power not found"]}), 400

    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        "id": hero_power.id,
        "strength": hero_power.strength,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id
    }), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)

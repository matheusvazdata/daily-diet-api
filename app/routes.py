from flask import Blueprint, request, jsonify
from .models import Meal
from .database import db
from werkzeug.exceptions import NotFound, BadRequest

bp = Blueprint('main', __name__)

@bp.route('/meals', methods=['POST'])
def create_meal():
    data = request.json

    if not data.get('name'):
        return jsonify({'error': 'Field "name" is required!'}), 400

    meal = Meal(**data)
    db.session.add(meal)
    db.session.commit()
    return jsonify({'id': meal.id}), 201

@bp.route('/meals/<int:id>', methods=['PUT'])
def update_meal(id):
    meal = Meal.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(meal, key, value)
    db.session.commit()
    return jsonify({'message': 'Item updated successfully!'})

@bp.route('/meals/<int:id>', methods=['DELETE'])
def delete_meal(id):
    meal = Meal.query.get_or_404(id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'message': 'Item removed successfully!'})

@bp.route('/meals', methods=['GET'])
def list_meals():
    meals = Meal.query.all()
    return jsonify([{
        'id': m.id,
        'name': m.name,
        'description': m.description,
        'date_time': m.date_time.isoformat(),
        'within_diet': m.within_diet
    } for m in meals])

@bp.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    meal = Meal.query.get_or_404(id)
    return jsonify({
        'id': meal.id,
        'name': meal.name,
        'description': meal.description,
        'date_time': meal.date_time.isoformat(),
        'within_diet': meal.within_diet
    })

@bp.errorhandler(NotFound)
def handle_404(e):
    return jsonify({
        'error': 'Not Found',
        'message': 'Meal not found with the given ID!'
    }), 404

@bp.errorhandler(BadRequest)
def handle_400(e):
    return jsonify({
        'error': 'Bad Request',
        'message': 'Request error. Check the data sent!'
    }), 400
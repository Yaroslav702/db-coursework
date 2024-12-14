from flask_src.app import app
from flask import request, jsonify
from marshmallow import ValidationError

from flask_src.models import (
    session,
    User
)

from flask_src.schemas import (
    user_read_schema,
    users_read_schema,
    user_create_schema,
    user_update_schema
)


@app.route('/users', methods=['GET'])
def get_users():
    users_list = session.query(User).all()
    result = users_read_schema.dump(users_list)

    response = {
        "count": len(result),
        "data": result
    }

    return jsonify(response), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({"message": f"User with ID {user_id} does not exist"}), 404

    result = user_read_schema.dump(user)

    return jsonify(result), 200


@app.route('/users/', methods=['POST'])
def create_user():
    try:
        validated_data = user_create_schema.load(request.form)

        user = User(first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])

        session.add(user)
        session.commit()

        return jsonify({
            "message": "User was successfully created.",
            "data": user_read_schema.dump(user)
        }), 201
    except ValidationError as err:
        return jsonify({
            "error": "Validation failed",
            "messages": err.messages
        }), 400


@app.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        return jsonify({"message": f"User with ID {user_id} does not exist"}), 404

    session.delete(user)
    session.commit()

    return jsonify({"message": "User was successfully deleted."}), 200


@app.route('/users/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    print('we are here')
    try:
        validated_data = user_update_schema.load(request.form)
        user = session.query(User).filter_by(id=user_id).first()

        if not user:
            return jsonify({"message": f"User with ID {user_id} does not exist"}), 404

        for key, value in validated_data.items():
            if key == 'password':
                user.set_password(value)
            else:
                setattr(user, key, value)

        session.commit()

        return jsonify({
            "message": "User was successfully updated.",
            "data": user_read_schema.dump(user)
        }), 200
    except ValidationError as err:
        return jsonify({
            "error": "Validation failed",
            "messages": err.messages
        }), 400

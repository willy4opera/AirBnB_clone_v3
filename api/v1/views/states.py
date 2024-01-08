#!/usr/bin/python3

"""Here, we defined the objects that handle all
default RestFul API actions for States """

from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_state.yml', methods=['GET'])
def get_states():
    """
    Here, we Retrieves the list of all State objects
    """
    dev_state_all = storage.all(State).values()
    StateList = []
    for state in dev_state_all:
        StateList.append(state.to_dict())
    return jsonify(StateList)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_id_state.yml', methods=['get'])
def get_state(state_id):
    """ Retrieves a specific State """
    dev_state = storage.get(State, state_id)
    if not dev_state:
        abort(404)

    renderdata = jsonify(dev_state.to_dict())
    return renderdata


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/state/delete_state.yml', methods=['DELETE'])
def delete_state(state_id):
    """
    Here, we deletes a State Object
    """

    dev_state = storage.get(State, state_id)

    if not dev_state:
        abort(404)

    storage.delete(dev_state)
    storage.save()
    renderdata = make_response(jsonify({}), 200)
    return renderdata


@app_views.route('/states', methods=['POST'], strict_slashes=False)
@swag_from('documentation/state/post_state.yml', methods=['POST'])
def post_state():
    """
    Here, we created the State
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = State(**data)
    instance.save()
    renderdata = make_response(jsonify(instance.to_dict()), 201)
    return renderdata


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/state/put_state.yml', methods=['PUT'])
def put_state(state_id):
    """
    Here, we updated the State
    """
    dev_state = storage.get(State, state_id)

    if not dev_state:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    esc = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in esc:
            setattr(state, key, value)
    storage.save()
    renderdata = make_response(jsonify(state.to_dict()), 200)
    return renderdata

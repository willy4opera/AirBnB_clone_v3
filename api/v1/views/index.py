#!/usr/bin/python3

"""Here, we write our Index file """

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Here, we retrieved the number of each objects by type """
    dev_class = [Amenity, City, Place, Review, State, User]
    dev_name = ["amenities", "cities", "places", "reviews", "states", "users"]

    object_n = {}
    for val in range(len(dev_class)):
        object_n[dev_name[val]] = storage.count(dev_class[val])

    return jsonify(object_n)

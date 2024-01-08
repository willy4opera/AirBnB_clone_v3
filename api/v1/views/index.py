#!/usr/bin/python3

""" Import modules """
from api.v1.views import app_views
from flask import jsonify

""" create route """


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Return status"""
    return jsonify({ "status": "OK" })

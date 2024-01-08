#!/usr/bin/python3

""" Import flask modules """
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

""" Import all """
from api.v1.views.index import *

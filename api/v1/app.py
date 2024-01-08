#!/usr/bin/python3
""" Import modules """
from api.v1.views import app_views
from flask import Flask
from models import storage
import os

app = Flask(__name__)

""" register blueprint """
app.register_blueprint(app_views)

""" Teardown appcontext """
@app.teardown_appcontext
def tear_down(error):
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
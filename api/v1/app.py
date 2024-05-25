#!/usr/bin/python3
"""Root of the project app file"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """handles teardown appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', "0.0.0.0")
    port = int(getenv('HBNB_API_PORT', "5000"))
    app.run(host=host, port=port, threaded=True)

#!/usr/bin/python3
"""defin view apis"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


types = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """retrive response status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def numberOfObjects():
    """retrieves the number of each objects by type"""
    res = {}
    for key, value in types.items():
        res[key] = storage.count(value)
    return jsonify(res)

# -*- coding: utf-8 -*-
"""User points on the state border to generate a polygon."""

import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from flask import Flask, request


app = Flask(__name__)

states_json = {}
with open('states_json.json') as f:
    states_json = json.load(f)


@app.route('/', methods=['POST'])
def check_point():
    longitude = float(request.form.get('longitude'))
    latitude = float(request.form.get('latitude'))
    tar_point = Point(longitude, latitude)
    for k, v in states_json.items():
        # convert point to tuple
        polygon = Polygon([(point[0], point[1]) for point in v])
        if polygon.contains(tar_point):
            return k
    return 'Cannot find in the data'


if __name__ == '__main__':
    app.run(port=8080)

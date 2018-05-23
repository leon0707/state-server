# -*- coding: utf-8 -*-
import json
from flask import Flask, request

app = Flask(__name__)

states_json = {}
with open('states_json.json') as f:
    states_json = json.load(f)


def orientation(p1, p2, p3):
    """0: colinear 1: Clockwise 2: Counterclockwise."""
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])

    if (val == 0):
        return 0
    if (val > 0):
        return 1
    else:
        return 2


def is_inside(state_border, point):
    """Check if the point is in the state."""
    # extreme longitude
    point_ext = [180, point[1]]
    count = 0
    i = 0
    points_num = len(state_border)
    for i in range(points_num):
        next = (i + 1) % points_num
        if (is_intersected(state_border[i],
                           state_border[next],
                           point, point_ext)):
            if orientation(state_border[i], point, state_border[next]) == 0:
                # if point is on the edge
                return on_segment(state_border[i], point, state_border[next])
            count += 1
    return count % 2 == 1


def is_intersected(p1, p2, p3, p4):
    """Check if (p1, p2) and (p3, p4) are interested."""
    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    if (o1 != o2 and o3 != o4):
        return True

    if (o1 == 0 and on_segment(p1, p3, p2)):
        return True

    if (o2 == 0 and on_segment(p1, p4, p2)):
        return True

    if (o3 == 0 and on_segment(p3, p1, p4)):
        return True

    if (o4 == 0 and on_segment(p3, p2, p4)):
        return True

    return False


def on_segment(p1, p2, p3):
    """Check if p2 one the segment of p1 and p3."""
    if (p2[0] <= max(p1[0], p3[0]) and p2[0] >= min(p1[0], p3[0]) and
            p2[1] <= max(p1[1], p3[1]) and p2[1] >= min(p1[1], p3[1])):
        return True
    return False


@app.route('/', methods=['POST'])
def check_point():
    longitude = float(request.form.get('longitude'))
    latitude = float(request.form.get('latitude'))
    tar_point = [longitude, latitude]
    for k, v in states_json.items():
        # convert point to tuple
        if is_inside(v, tar_point):
            return k
    return 'Cannot find in the data'


if __name__ == '__main__':
    app.run(port=8080)

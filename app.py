# -*- coding: utf-8 -*-
import json

states_json = {}
with open('states_json.json') as f:
    states_json = json.load(f)


def check_point(states_json, point_1):
    pass


def is_inside(state_border, point):
    point_ext = [180, point[1]]
    count = 0
    i = 0
    points_num = len(state_border)
    for i in range(points_num):
        next = (i + 1) % points_num
        if (is_intersected(state_border[i], state_border[next], point, point_ext)):
            pass


def is_intersected(p1, p2, p3, p4):
    pass


def on_segment(p1, p2, p3):
    pass


if __name__ == '__main__':
    pa = [
        [-77.475793, 39.719623],
        [-80.524269, 39.721209],
        [-80.520592, 41.986872],
        [-74.705273, 41.375059],
        [-75.142901, 39.881602],
        [-77.475793, 39.719623]
    ]
    point_1 = [-77.036133, 40.513799]
    is_inside(pa, point_1)

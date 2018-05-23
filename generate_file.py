# -*- coding: utf-8 -*-
"""Convert state file to json."""
import json


if __name__ == '__main__':
    state = {}
    with open('states.json') as f:
        content = f.readlines()
        for line in content:
            state_json = json.loads(line)
            state[state_json['state']] = []
            state[state_json['state']] = [
                (point[0], point[1]) for point in state_json['border']]

    with open('states_json.json', 'w') as outfile:
        json.dump(state, outfile)

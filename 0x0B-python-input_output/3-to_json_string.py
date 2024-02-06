#!/usr/bin/python3
"""module of json file function"""

import json


def to_json_string(my_obj):
    """Return JSON representation of a string object"""

    return json.dumps(my_obj)

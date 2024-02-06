#!/usr/bin/python3
"""module of json file function"""

import json


def from_json_string(my_str):
    """Return Python object representation of a JSON string"""

    return json.loads(my_str)

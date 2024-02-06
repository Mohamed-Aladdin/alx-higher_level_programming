#!/usr/bin/python3
"""module of json file function"""

import json


def load_from_json_file(filename):
    """
    creates Object from “JSON file”
    """

    with open(filename, encoding="utf-8") as file:
        return json.load(file)

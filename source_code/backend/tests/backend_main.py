from json import JSONDecodeError
import requests
import random
import json
from collections import Counter
from flask import jsonify, Flask


def get_random_activity_for_zone(zoneColour):
    response = requests.get(
        "http://127.0.0.1:5001/random/{}".format(zoneColour),
        headers={'content-type': 'application/json'}
    )
    try:
        print(response.json())
        return response.json()
    except JSONDecodeError as E:
        print("Failed to decode JSON")
        raise E

def record_add_count(zoneColour):
    add_count_response = requests.get("http://127.0.0.1:5001/addcount/{}".format(zoneColour), headers={'content-type': 'application/json'})
    try:
        print(add_count_response.json())
        return add_count_response.json()
    except JSONDecodeError as E:
        print("Failed to decode JSON")
        raise E

def ask_user_to_repeat():
    while input('Would you like to try another activity? y/n') == 'y':
        do_full_run()
    else:
        print('Hope you are feeling better!')

def get_colour_from_user():
    zoneColour = input('What is your zone?').upper()
    return zoneColour

def do_full_run():
    zoneColour = get_colour_from_user()
    get_random_activity_for_zone(zoneColour)
    add_count = record_add_count(zoneColour)
    print("Zone colour {} now has counter:{}".format(zoneColour,add_count))

def run():
    do_full_run()
    ask_user_to_repeat()

if __name__ == '__main__':
    run()


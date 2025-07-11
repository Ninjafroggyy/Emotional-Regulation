from flask import Flask, jsonify, make_response
from collections import Counter
import itertools
import random

from datalayer.datalayer_mysql import DataLayerRegulationBreak

app = Flask(__name__)
counter = {"BLUE": 0, "YELLOW": 0, "RED": 0, "GREEN": 0}

class RegulationBreak:
    def __init__(self, zoneString):
        self.zoneString = zoneString

class SuggestedActivity(RegulationBreak):
    def __init__(self,zoneString):
        self.zoneString = zoneString

    @app.route('/random/<zoneString>')
    def suggested_activity(zoneString):
        data_layer = DataLayerRegulationBreak(5)
        result = data_layer.all_activities_for_zone_colour(zoneString)
        if result == False:
            print("ERROR: No activities found for colour {}".format(zoneString))
            return make_response("Zone not found", 404)
        suggestion = random.choice(result)
        jsonifysuggestion = jsonify(suggestion)
        print(jsonifysuggestion)
        return jsonifysuggestion

class CountActivity(SuggestedActivity):
    def __init__(self, zoneString):
        self.zoneString = zoneString

    @app.route('/addcount/<zoneString>')
    def record_add_count(zoneString):
        if zoneString not in counter:
            print("ERROR: No activities found for colour {}".format(zoneString))
            return make_response("Zone not found", 404)
        count_answer = counter[zoneString]
        count_answer += 1
        counter[zoneString] = count_answer
        jsonify_count_answer = jsonify(count_answer)
        print(jsonify_count_answer)
        return jsonify_count_answer #todo store the counter in database layer


    def resume_process(zoneString):
        data_layer = DataLayerRegulationBreak(5)
        answer = input('What is your zone?')
        data_layer.all_activities_for_zone_colour(zoneString)
        CountActivity.record_add_count(zoneString)
        CountActivity.repeat_count(zoneString)
        new_total = itertools.chain(CountActivity.repeat_count, CountActivity.record_add_count)
        new_total_jsonify = jsonify(new_total)
        return new_total_jsonify

if __name__ == '__main__':
    app.run(debug=True, port = 5001)


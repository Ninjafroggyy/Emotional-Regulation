from flask import Flask, jsonify, request
from collections import Counter
import itertools
from dbutils import get_all_activities
import random

app = Flask(__name__)

class RegulationBreak:
    def __init__(self, answer):
        self.answer = answer

class SuggestedActivity(RegulationBreak):
    def __init__(self,answer):
        self.answer = answer

    @app.route('/random/<answer>')
    def suggested_activity(answer):
        result = get_all_activities(answer)
        suggestion = random.choice(result)
        jsonifysuggestion = jsonify(suggestion)
        print(jsonifysuggestion)
        return jsonifysuggestion

record = []
class CountActivity(SuggestedActivity):
    def __init__(self, answer):
        self.answer = answer

    @app.route('/addcount/<answer>')
    def record_add_count(answer):
        record.append(answer)
        count_answer = Counter(record)
        add_count = count_answer.items()
        for item in count_answer:
            print(item)
        return count_answer

    @app.route('/addcount/<answer>')
    def repeat_count(answer):
        while input('Would you like to try another activity? y/n') == 'y':
            answer = input('What is your zone?')
            print(suggested_activity(answer))
            repeat_count = record_add_count.json()
            print(repeat_count)
        else:
            print('Hope you are feeling better!')
        return repeat_count

    def resume_process(answer):
        answer = input('What is your zone?')
        suggested_activity(answer)
        record_add_count(answer)
        repeat_count(answer)
        new_total = itertools.chain(repeat_count, record_add_count)
        new_total_jsonify = jsonify(new_total)
        return new_total_jsonify

if __name__ == '__main__':
    app.run(debug=True, port = 5001)
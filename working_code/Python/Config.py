from app import app
import random
import mysql.connector
from python.config import USER, HOST, PASSWORD
from collections import Counter
import itertools
class ZoneNotFoundError(Exception):
    pass

def connect_to_db(regulationtoolbox):
    connection = mysql.connector.connect(
    host = HOST,
    user = USER,
    password = PASSWORD,
    auth_plugin = 'mysql_native_password',
    database = regulationtoolbox)
    return connection


answer = input('What is your zone?')
record = []


@app.route('/regulation_toolbox/<zones_ID>')
def get_suggested_activity(answer):
    connection = None
    try:
        db_name = 'regulationtoolbox'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        query = "SELECT * FROM regulationtoolbox.activity_type WHERE act_type_ID = {}".format(answer)
        cur.execute(query)
        result = cur.fetchall()
        suggestion = random.choice(result)
        print(suggestion)
        cur.close()
    except Exception:
        raise ZoneNotFoundError
    finally:
        if db_connection:
            db_connection.close()

def record_add_count(answer):
    record.append(answer)
    count_answer = Counter(record)
    items = count_answer.items()
    for item in items:
        print(item)
    return items

def repeat_count(answer):
    total = []
    while input('Would you like to try another activity? y/n') == 'y':
        answer = input('What is your zone?')
        get_suggested_activity(answer)
        record_add_count(answer)
    else:
        print('Hope you are feeling better!')
    return total

def restart_process(answer):
    answer = input('What is your zone?')
    get_suggested_activity(answer)
    record_add_count(answer)
    repeat_count(answer)
    new_total = itertools.chain(repeat_count, record_add_count)
    return new_total


get_suggested_activity(answer)
record_add_count(answer)
repeat_count(answer)
restart_process(answer)

if __name__ == '__main__':
    app.run(debug=True)

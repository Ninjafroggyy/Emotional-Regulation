from dbconnection import make_db_query
import DBqueries


def ask_user():
    while True:
        try:
            zone = input("Choose a zone: blue, green, yellow, red:  ").upper()
        except:
            print("Entry not recognised, try again")
            continue
        if zone == "BLUE" or zone.startswith("B"):
            return make_db_query(DBqueries.queryblue)
        elif zone == "GREEN" or zone.startswith("G"):
            return
        elif zone == "YELLOW" or zone.startswith("Y"):
            return "Yellow"
        elif zone == "RED" or zone.startswith("R"):
            redactivites = make_db_query(DBqueries.queryred)
            return redactivites
        else:
            print("Entry not recognised, try again ......")
            continue

def find_activities(zone):
    if zone == 1:
        make_db_query(DBqueries.queryblue)
    elif zone == 2:
        make_db_query(DBqueries.querygreen)
    elif zone == 3:
        make_db_query(DBqueries.queryyellow)
    elif zone == 4:
        make_db_query(DBqueries.queryred)

# ask_user()
find_activities(1)
    #
    # if time: could check if input is correct


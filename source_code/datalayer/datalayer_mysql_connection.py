import mysql.connector
import datalayer.config as cfg

class DbConnectionError(Exception):
    pass
# the underscore indicates that this is a private function only
# to be used in this file.

def _connect_to_db(db_name):
    connection = mysql.connector.connect(
    host = cfg.HOST,
    user = cfg.USER,
    password = cfg.PASSWORD,
    auth_plugin = 'mysql_native_password',
    database = db_name)
    return connection

def make_db_query(query):
    try:
        db_name = 'regulationtoolbox'
        # Database engine - connects to DB
        db_connection = _connect_to_db(db_name)
        # Cursor does the querying
        cur = db_connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception:
        raise Exception("Something is wrong, try again")
    finally:
        if db_connection:
            db_connection.close()



#
# query = "SELECT regulation_toolbox.activityName, activity_zone.zone_ID FROM activity_zone INNER JOIN activity_type ON activity_zone.act_type_ID=activity_type.act_type_ID INNER JOIN regulation_toolbox ON regulation_toolbox.act_type_ID=activity_type.act_type_ID WHERE zone_ID = 1"
# make_db_query(query)


# #testing
# make_db_query("SELECT * FROM zones;")
# # make_db_query("SELECT COUNT(activityName) FROM regulationtoolbox.regulation_toolbox")

import datalayer.datalayer_mysql_queries as query
import random
from datalayer.datalayer_mysql_connection import make_db_query


class DataLayerRegulationBreak:

    def __init__(self, numrand):
        self.numrand = numrand # how many random activities are to be generated
        self.zone = 0 # number value for the zones
        self.allzoneactivities = [] # list of all the activities needed
        self.howmanyact = 0 # how many activities are available
        self.randomnumbers = 0 # random numbers generated
        self.randomacts = [] # the random activities generated

    def is_zone_colour_valid(self, zoneColour):
        return zoneColour in ["BLUE", "GREEN", "YELLOW", "RED"]


    def all_activities_for_zone_colour(self, zoneColour):
        if self.is_zone_colour_valid(zoneColour):
            if zoneColour == "BLUE" or zoneColour.startswith("B"):
                self.zone = 1
            elif zoneColour == "GREEN" or zoneColour.startswith("G"):
                self.zone = 2
            elif zoneColour == "YELLOW" or zoneColour.startswith("Y"):
                self.zone = 3
            elif zoneColour == "RED" or zoneColour.startswith("R"):
                self.zone = 4
            return self.find_activities()
        else:
            return False


    def find_activities(self):
        if self.zone == 1:
            self.allzoneactivities = (make_db_query(query.queryblue))
        elif self.zone == 2:
            self.allzoneactivities = make_db_query(query.querygreen)
        elif self.zone == 3:
            self.allzoneactivities = make_db_query(query.queryyellow)
        elif self.zone == 4:
            self.allzoneactivities = make_db_query(query.queryred)
        return DataLayerRegulationBreak.how_many(self)

    def how_many(self):
        self.howmanyact = len(self.allzoneactivities)
        return DataLayerRegulationBreak.random_numgenerator(self)

    def random_numgenerator(self):
        rangeupper = self.howmanyact
        self.randomnumbers = random.sample(range(0, rangeupper), self.numrand)
        return DataLayerRegulationBreak.random_actgenerator(self)

    def random_actgenerator(self):
        for x in self.randomnumbers:
            activity = self.allzoneactivities[x]
            self.randomacts.append(activity[0])
        return self.randomacts

    def remove_from_tuple(self, item):
        removed = list(item[0]).pop
        return removed



from python.EmmaPython.dbconnection import make_db_query
import random
import DBqueries

class RegulationBreak:
    def __init__(self, zone, howmany):
        self.zone = zone  # which zone have been selected
        self.howmany = howmany  # how many random activities are to be generated
        self.numactivitieschoice = 0 # the number of activities available in the DB Query
        self.numlist = 0 # the randomly generated tuple from random_generator

    def acttypeforzone(self):
        redactivites = make_db_query(DBqueries.queryred)
        return redactivites

# find out how many to choose from in chosen zone
#     def how_many_activities(self):
#         query = "SELECT (activityName) FROM regulationtoolbox.regulation_toolbox"
#         numberstring = make_db_query(query)
#
#
#         return numberstring
#         # self.numactivitieschoice = list(numberstring)
#         #
#         # print(self.numactivitieschoice)
#         # return self.numactivitieschoice
#
# # randomly generate numbers and assign outcome to self.numlist
#     def random_generator(self):
#         rangeupper = int(self.numactivitieschoice)
#         numlist = random.sample(range(0, rangeupper), self.howmany)
#         self.numlist = tuple(numlist)
#         return self.numlist
#
# # query Db that correspond to the random_generator numbers above
#     def suggest_activities(self):
#         query = "SELECT activityName FROM regulation_toolbox WHERE activityID in {};".format(self.numlist)
#         outcome = make_db_query(query)
#         return outcome
#
#
# def main():
#     pass
#
# if __name__== '__main__':
#     main()


user_1 = RegulationBreak("red", 2)
print(RegulationBreak.acttypeforzone(user_1))
# print(RegulationBreak.how_many_activities(user_1))
# print(RegulationBreak.random_generator(user_1))
# print(RegulationBreak.suggest_activities(user_1))
import unittest
from json import JSONDecodeError

import requests
import json
from collections import Counter

#Integration/Regression tests

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.example_blue_activities = ['blow out candle', 'square breathing', 'brain break breathing choice', 'starjumps',
                               'movement break activities', 'Movement break choices', 'How would you feel if?',
                               'What if scenarios?', 'Should I say it or not?']
        self.example_yellow_activities = ['blow out candle', 'square breathing', 'brain break breathing choice', 'nature colouring', 'make a worry box', 'Make a worry doll', 'Make a bag of worries', 'Make some flash cards', 'Mindfulness colouring', 'Bullet Journal Page', 'Emotions board game', 'Play uno', 'Self care bingo', 'starjumps', 'movement break activities', 'Movement break choices', 'downward dog pose', 'tree pose', 'follow the yoga cards', 'downward dog pose', 'tree pose', 'follow the yoga cards']
        self.example_red_activities = ['nature colouring', 'make a worry box', 'Make a worry doll', 'Make a bag of worries', 'Make some flash cards', 'Mindfulness colouring', 'Bullet Journal Page', 'Emotions board game', 'Play uno', 'Self care bingo', 'starjumps', 'movement break activities', 'Movement break choices', 'downward dog pose', 'tree pose', 'follow the yoga cards']
        self.example_green_activities = ['blow out candle', 'square breathing', 'brain break breathing choice', 'starjumps', 'movement break activities', 'Movement break choices', 'downward dog pose', 'tree pose', 'follow the yoga cards', 'downward dog pose', 'tree pose', 'follow the yoga cards']
        self.all_activities = {"BLUE": self.example_blue_activities, "YELLOW": self.example_yellow_activities}
    def GetSuggestedActivity(self, zoneColour):
        response = requests.get(
            "http://127.0.0.1:5001/random/{}".format(zoneColour),
            headers={'content-type': 'application/json'}
        )
        print(response)
        try:
            print(response.json())
            return response.json()
        except JSONDecodeError as E:
            print("Failed to decode JSON")
            raise E

    def GetRepeatCount(self, zoneColour):
        response = requests.get(
            "http://127.0.0.1:5001/repeat_count/{}".format(zoneColour),
            headers={'content-type': 'application/json'}
        )
        print(response)
        try:
            print(response.json())
        except JSONDecodeError as E:
            print("Failed to decode JSON")
            raise E

    def testRandomActivity(self):
        for zoneColour in ["BLUE", "RED", "GREEN", "YELLOW"]:
            random_activity = self.GetSuggestedActivity(zoneColour)
            all_activities_for_zone = self.all_activities[zoneColour]
            self.assertGreater(len(all_activities_for_zone), 0)
            self.assertTrue(random_activity in all_activities_for_zone)
            break

    def testTestZoneNotFound(self):
        zoneColour = "DOG"
        response = requests.get(
            "http://127.0.0.1:5001/random/{}".format(zoneColour),
            headers={'content-type': 'application/json'}
        )
        print(response)
        self.assertEqual(response.status_code, 404)

    # def testRepeatCount(self):
    #     for zoneColour in ["RED", "GREEN", "YELLOW", "BLUE"]:
    #         self.GetRepeatCount(zoneColour)


    # def testRecordAddCount(self):
    #     pass





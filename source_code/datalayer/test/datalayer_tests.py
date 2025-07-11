import unittest
from datalayer.datalayer_mysql import DataLayerRegulationBreak

#unit tests for data layer
class TestsUserZoneInput(unittest.TestCase):

    def testAskUserInvalidInput(self):
        testUser = DataLayerRegulationBreak(5)
        testZone = "PURPLE"
        self.assertFalse(testUser.all_activities_for_zone_colour(testZone))

    def testAskUserValidInput(self):
        testUser1 = DataLayerRegulationBreak(5)
        testZone1 = "GREEN"
        self.assertTrue(testUser1.all_activities_for_zone_colour(testZone1))

    def testIsZoneColourValidValidInput(self):
        testUser = DataLayerRegulationBreak(5)
        testZone = "BLUE"
        self.assertTrue(testUser.is_zone_colour_valid(testZone))

    def testIsZoneColourValidInvalidInput(self):
        testUser = DataLayerRegulationBreak(5)
        testZone = "PINK"
        self.assertFalse(testUser.is_zone_colour_valid(testZone))



import unittest
import requests

#drafts of API testing (WIP)

class TestAPI(unittest.TestCase):
    URL = "xyz"

    def test_make_connection(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 4)


class TestAuthoristation(unittest.TestCase):

    def testSignUp(self):
        pass
    def testLogin(self):
        pass
    def testLogOut(self):
        pass

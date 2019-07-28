import unittest
from nabettobot.models import Bet

class TestBet(unittest.TestCase):
    def BetTestCase(self):
        John_RED_300 = Bet("John", "red", 300)
        print(John_RED_300) # Printing the class output for now, will use an assert method after I get it working


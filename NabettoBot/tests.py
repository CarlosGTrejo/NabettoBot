import unittest
from .models import Bet


class TestBet(unittest.TestCase):

    def setUp(self):
        # Populate Bet
        Bet('John', 'blue', '300')

    def test_data(self):
        # Check if bet was updated
        assert Bet.__static_data__ == {'blue':300, 'red':0}

    def test_betWithMajority(self):
        self.assertEqual(Bet.betWithMajority(100), "!blue 10")

    def test_resetData(self):
        # Reset Bet data
        Bet.resetData()
        assert Bet.__static_data__ == {'blue': 0, 'red':0}

    # TODO:def extractBet_TestCase(self):
        # Bet.extractBet()

    def tearDown(self):
        # Reset Bet data
        Bet.resetData()

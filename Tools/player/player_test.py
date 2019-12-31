# UNIT TESTS FOR PLAYER MODULE

import unittest
from player import level, solorank, solowr, champ_wr, champ_mastery



class TestPlayer(unittest.TestCase):
    def test_level(self):
        self.assertEqual(level("pliuwu", "NA"), 267)
        self.assertEqual(level("jinlongr", "NA"), 249)
        self.assertEqual(level("minhissohandsome", "LAN"), -1)
        self.assertEqual(level("pliuwu", "EUW"), -1)
        self.assertEqual(level("", ""), -1)

    def test_solorank(self):
        self.assertEqual(solorank("pliuwu", "NA"), "PlatinumIV")
        self.assertEqual(solorank("jinlongr", "NA"), "DiamondIV")
        self.assertEqual(solorank("minhissohandsome", "LAN"), "Unranked")
        self.assertEqual(solorank("pliuwu", "EUW"), "Unranked")
        self.assertEqual(solorank("", ""), "Unranked")
    
    def test_solowr(self):
        self.assertTrue(solowr("pliuwu", "NA"))
        self.assertTrue(solowr("jinlongr", "NA"))
        self.assertTrue(solowr("smellcookies", "NA"))
        self.assertTrue(solowr("nastyafcookies", "NA"))

    def test_currentchamp_wr(self):
        self.assertTrue(champ_wr("pliuwu", "NA", 44))
        self.assertTrue(champ_wr("jinlongr", "NA", 44))
        self.assertTrue(champ_wr("smellcookies", "NA", 44))
        self.assertTrue(champ_wr("nastyafcookies", "NA", 44))

    def test_currentchamp_mastery(self):
        self.assertTrue(champ_mastery("pliuwu", "NA", "Nami"))
        self.assertTrue(champ_mastery("jinlongr", "NA", "Akali"))
        self.assertEqual(champ_mastery("smellcookies", "NA", "Senna"), 0)
        self.assertEqual(champ_mastery("nastyafcookies", "NA", "Senna"), -1)
        
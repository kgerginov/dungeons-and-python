import unittest

from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.map = [['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' '], ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#', ' ', ' ', ' ', ' '], ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', ' ', ' ', ' ', ' '], ['#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', ' ', ' '], [' ', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', ' ', ' '], [' ', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', ' ', ' '], [' ', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', ' ', ' '], [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ']]

    def test_place_points_of_interest(self):
        for a in Dungeon._place_points_of_interest(self.map):
            print(''.join(a))


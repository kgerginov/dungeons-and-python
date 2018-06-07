import unittest

from dungeon2 import Dungeon
from src.dungeon import DungeonMap


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.map = [['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' '], ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#', ' ', ' ', ' ', ' '], ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', ' ', ' ', ' ', ' '], ['#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', ' ', ' '], [' ', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', ' ', ' '], [' ', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', ' ', ' '], [' ', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', ' ', ' '], [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ']]





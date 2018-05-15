import unittest

from hero import Hero
from spell import Spell

from src.enemy import Enemy
from src.fight import Fight
from src.weapon import Weapon


class TestFight(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(name='Ivan', title='Dr', health=150, mana=80, mana_regeneration_rate=2)
        self.enemy = Enemy(health=150, mana=50, damage=20)

    def test_start_fight(self):
        h = self.hero
        e = self.enemy
        h.learn_spell(Spell())
        h.equip_weapon(Weapon())
        ft = Fight(h, e)
        ft.start_fight()
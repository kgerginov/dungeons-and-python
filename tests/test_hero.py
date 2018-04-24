import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell


class TestHero(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero(name='Ivan', title='Dr', health=100, mana=50, mana_regeneration_rate=2)
        self.test_weapon = Weapon()
        self.test_spell = Spell(mana_cost=20)

    def test_attack_by_weapon(self):
        self.setUp()
        h = self.test_hero
        h.equip_weapon(self.test_weapon)
        result = h.attack(by='weapon')
        exp_data = 20
        self.assertEqual(result, exp_data)

    def test_attack_by_spell(self):
        self.setUp()
        h = self.test_hero
        h.learn_spell(self.test_spell)
        result = h.attack(by='spell')
        exp_data = 30
        self.assertEqual(result, exp_data)
        self.assertEqual(h.mana, 30)

    def test_attack_by_spell_no_mana(self):
        self.setUp()
        h = self.test_hero
        h.learn_spell(self.test_spell)
        h.attack(by='spell')
        h.attack(by='spell')
        with self.assertRaises(Exception):
            h.attack(by='spell')

    def test_attack_no_weapon(self):
        self.setUp()
        with self.assertRaises(Exception):
            h = self.test_hero
            h.attack(by='weapon')


if __name__ == '__main__':
    unittest.main()

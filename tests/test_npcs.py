import unittest
from python101.dungeons_and_python.players import Player, Hero


class TestSoldiers(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero(name='Ivan', title='Dr.', health=250, mana=100, mana_regeneration_rate=2)
        self.test_soldier = Player(health=200, mana=100)

    def test_create_instance_invalid_input_should_raise_value_error(self):
        with self.assertRaises(ValueError):
            Player(health='asd', mana=100)

    def test_take_damage_int(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_damage(20)
        self.assertEqual(npc.health, 180)

    def test_take_damage_float(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_damage(10.5)
        self.assertEqual(npc.health, 189.5)

    def test_take_damage_should_raise_valuerroer_invalid_input(self):
        self.setUp()
        with self.assertRaises(ValueError):
            npc = self.test_soldier
            npc.take_damage('asd')


if __name__ == '__main__':
    unittest.main()
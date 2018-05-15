import unittest

from spell import Spell
from weapon import Weapon

from src.unit import Unit


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.test_soldier = Unit(health=200, mana=100)
        self.default_weapon = Weapon()
        self.default_spell = Spell()

    def test_create_instance_invalid_input_should_type_error_error(self):
        with self.assertRaises(TypeError):
            Unit(health='asd', mana=100)

    def test_create_instance_negative_health_should_raise_value_error(self):
        with self.assertRaises(ValueError):
            Unit(health=-20, mana=20)

    def test_create_instance_negative_mana_should_raise_value_error(self):
        with self.assertRaises(ValueError):
            Unit(health=20, mana=-20)

    def test_can_cast(self):
        self.setUp()
        n = self.test_soldier
        self.assertFalse(n.can_cast())

    def test_can_cast_not_enough_mana(self):
        self.setUp()
        n = self.test_soldier
        n.learn_spell(Spell('Fireball', damage=50, mana_cost=120, cast_range=3))
        self.assertFalse(n.can_cast())

    def test_can_cast_all_okay(self):
        self.setUp()
        self.test_soldier.learn_spell(self.default_spell)
        self.assertTrue(self.test_soldier.can_cast())

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

    def test_take_damage_more_damage_than_hp_should_return_0(self):
        npc = Unit(health=20, mana=50)
        npc.take_damage(30)
        self.assertEqual(npc.get_health(), 0)

    def test_take_damage_should_raise_type_error_invalid_input(self):
        self.setUp()
        with self.assertRaises(TypeError):
            npc = self.test_soldier
            npc.take_damage('asd')

    def test_take_damage_raises_value_error_negative_value(self):
        self.setUp()
        with self.assertRaises(ValueError):
            npc = self.test_soldier
            npc.take_damage(-20)

    def test_take_healing_should_not_get_over_max_hp(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_damage(20)
        npc.take_healing(30)
        self.assertEqual(npc.get_health(), 200)

    def test_healing_msg_if_instance_is_dead(self):
        self.setUp()
        npc = self.test_soldier
        npc.health = 0
        self.assertEqual(npc.take_healing(20), 'Cannot heal a corpse!')

    def test_healing_heals(self):
        self.setUp()
        n = self.test_soldier
        n.take_damage(50)
        n.take_healing(20)
        self.assertEqual(n.health, 170)

    def test_equip_weapon(self):
        self.setUp()
        npc = self.test_soldier
        npc.equip_weapon(self.default_weapon)
        self.assertEqual(npc.weapon, self.default_weapon)

    def test_learn_spell(self):
        self.setUp()
        npc = self.test_soldier
        npc.learn_spell(self.default_spell)
        self.assertEqual(npc.spell, self.default_spell)

    def test_equip_weapon_invalid_instance_raises_type_error(self):
        self.setUp()
        with self.assertRaises(TypeError):
            self.test_soldier.equip_weapon('asd')

    def test_learn_spell_invalid_instance_raises_type_error(self):
        self.setUp()
        with self.assertRaises(TypeError):
            self.test_soldier.learn_spell('asd')

    def test_take_mana_should_not_get_over_max_mana(self):
        self.setUp()
        npc = self.test_soldier
        npc.take_mana(20)
        npc.take_mana(30)
        self.assertEqual(npc.get_mana(), 100)

    def test_take_mana_should_raise_type_error_invalid_input(self):
        self.setUp()
        npc = self.test_soldier
        with self.assertRaises(TypeError):
            npc.take_mana('as')

    def test_take_mana_should_raise_value_error_negative_value(self):
        self.setUp()
        n = self.test_soldier
        with self.assertRaises(ValueError):
            n.take_mana(-20)

    def test_get_damage_source_weapon_and_spell(self):
        self.setUp()
        n = self.test_soldier
        n.equip_weapon(self.default_weapon)
        n.learn_spell(Spell(name='asd', damage=20, mana_cost=30, cast_range=2))
        self.assertEqual(n.get_damage_source(), 'spell')

    def test_get_damage_source_weapon_and_spell_wepaon_higher_damage(self):
        self.setUp()
        n = self.test_soldier
        n.equip_weapon(Weapon(name='asd', damage=50))
        n.learn_spell(self.default_spell)
        self.assertEqual(n.get_damage_source(), 'weapon')

    def test_get_damage_source_weapon_only(self):
        self.setUp()
        n = self.test_soldier
        n.equip_weapon(self.default_weapon)
        self.assertEqual(n.get_damage_source(), 'weapon')

    def test_get_damage_source_spell_only(self):
        self.setUp()
        n = self.test_soldier
        n.learn_spell(self.default_spell)
        self.assertEqual(n.get_damage_source(), 'spell')

    def test_get_damage_source_no_weapon_spell(self):
        self.setUp()
        n = self.test_soldier
        self.assertEqual(n.get_damage_source(), None)


if __name__ == '__main__':
    unittest.main()

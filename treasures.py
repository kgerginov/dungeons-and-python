from random import choice
from weapon import Weapon
from spell import Spell


class Treasures:
    def __init__(self):
        self.treasures = {
            'health_potion': [10, 20, 30, 50, 100],
            'mana_potion': [10, 20, 30, 50, 100],
            'weapon': [
                Weapon(name='Sword', damage=20),
                Weapon(name='Bradve', damage=50),
                Weapon(name='Dagger', damage=15)
            ],
            'spell': [
                Spell(name='Fireball', damage=20, mana_cost=40, cast_range=2),
                Spell(name='Ice', damage=30, mana_cost=50, cast_range=2),
                Spell(name='Lightning', damage=50, mana_cost=70, cast_range=1)
            ]
        }

    def pick_treasure(self):
        loot = choice(list(self.treasures.keys()))
        return {loot: choice(self.treasures.get(loot))}

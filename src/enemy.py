from src.unit import Unit


class Enemy(Unit):
    def __init__(self, *, health, mana, damage):
        if not isinstance(damage, (int, float)):
            raise TypeError('Damage should be a Number!')
        super().__init__(health, mana)
        self.damage = damage

    def __str__(self):
        return f'enemy with {self.health} hp, {self.mana} mana'


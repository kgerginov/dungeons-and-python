from python101.dungeons_and_python.unit import Unit


class Enemy(Unit):
    def __init__(self, health, mana, damage):
        if not isinstance(damage, (int, float)):
            raise TypeError('Damage should be a Number!')
        super().__init__(health, mana)
        self.damage = damage

    def attack(self):
        return self.damage

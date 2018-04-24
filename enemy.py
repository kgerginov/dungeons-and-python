from python101.dungeons_and_python.unit import Unit


class Enemy(Unit):
    def __init__(self, health, mana):
        super().__init__(health, mana)
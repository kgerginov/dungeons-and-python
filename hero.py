from python101.dungeons_and_python.unit import Unit


class Hero(Unit):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

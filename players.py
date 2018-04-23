class Player:
    def __init__(self, health, mana):
        self.validate_value(health, mana)
        self.health = health
        self.mana = mana

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.alive

    def can_cast(self):
        pass

    @staticmethod
    def validate_value(*args):
        for val in args:
            if val < 0:
                raise ValueError('Value must be greater than 0!')
            if not isinstance(val, (int, float)):
                raise ValueError('Value must be a number!')

    def take_damage(self, damage):
        self.validate_value(damage)
        self.health -= damage

    def take_healing(self, healing_points):
        self.validate_value(healing_points)
        self.health += healing_points

    def take_mana(self, mana_points):
        self.validate_value(mana_points)
        self.mana += mana_points


class Hero(Player):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate



asd = Hero(name='asd', title='asdasd', health=200, mana=100, mana_regeneration_rate=2)

print(asd.get_health())



class Weapon:
    def __init__(self, name="The Axe of Destiny", damage=20):
        self.name = name
        self.damage = damage

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.damage == other.damage
        )

    @property
    def get_weapon(self):
        weapon_prop = {}
        weapon_prop['name'] = self.name
        weapon_prop['damage'] = self.damage
        return weapon_prop

class Spell:
    def __init__(self, name="Fireball", damage=30, mana_cost=50, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.damage == other.damage
            and self.mana_cost == other.mana_cost
            and self.cast_range == other.cast_range
        )


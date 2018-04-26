from unit import Unit


class Hero(Unit):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def __str__(self):
        return self.known_as()

    def known_as(self):
        return f'{self.name} the {self.title}'

    def attack(self, by):
        if by not in ('weapon', 'spell'):
            raise Exception('Enter valid attack type')
        if by == 'weapon':
            if self.weapon is None:
                raise Exception('No Weapon!')
            return self.weapon.damage
        if by == 'spell':
            if self.spell is None:
                raise Exception('No Spell Learned!')
            if self.can_cast():
                self.mana -= self.spell.mana_cost
                return self.spell.damage
            else:
                raise Exception('Not Enough Mana!')


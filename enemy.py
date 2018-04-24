from unit import Unit


class Enemy(Unit):
    def __init__(self, health, mana, damage):
        if not isinstance(damage, (int, float)):
            raise TypeError('Damage should be a Number!')
        super().__init__(health, mana)
        self.damage = damage

    def attack(self, by=''):
        if by not in ('weapon', 'spell', ''):
            raise Exception('Enter valid attack type!')
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
        else:
            return self.damage

from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        if not isinstance(hero, Hero):
            raise TypeError('Hero must be instance of hero!')
        if not isinstance(enemy, Enemy):
            raise TypeError('Enemy must be instance of Enemy!')
        self._hero = hero
        self._enemy = enemy

    @property
    def hero(self):
        return self._hero

    @hero.setter
    def hero(self, hero):
        if not isinstance(hero, Hero):
            raise TypeError('Hero must be instance of Hero!')
        self._hero = hero

    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, enemy):
        if isinstance(enemy, Enemy):
            raise TypeError('Enemy must be instance of enemy!')
        self._enemy = enemy

    def start_fight(self):
        print(f'A fight is starter between our hero '
              f'{self.hero.known_as()} and {str(self.enemy)}!')
        while True:
            if self.hero.get_damage_source() == 'spell':
                self.enemy.take_damage(self.hero.attack(by='spell'))
                print(f'Hero casts a {self.hero.spell.name},'
                      f' hits enemy for {self.hero.spell.damage}. '
                      f'Enemy health is {self.enemy.health}.')

            if self.hero.get_damage_source() == 'weapon':
                self.enemy.take_damage(self.hero.attack(by='weapon'))
                print(f'Hero hits with {self.hero.weapon.name}'
                      f' for {self.hero.weapon.damage} damage. '
                      f'Enemy health is {self.enemy.health}.')

            if self.hero.get_damage_source() is None:
                self.hero.health = 0
                print('Our hero stands no chance without weapons or spells. Dead.')
                break

            if not self.enemy.is_alive():
                print('The Enemy is dead!')
                break

            if self.enemy.get_damage_source() == 'spell':
                self.hero.take_damage(self.enemy.attack(by='spell'))
                print(f'Enemy casts a {self.enemy.spell.name},'
                      f' hits enemy for {self.enemy.spell.damage}. '
                      f'Hero health is {self.hero.health}.')

            if self.enemy.get_damage_source() == 'weapon':
                self.hero.take_damage(self.enemy.attack(by='weapon'))
                print(f'Enemy hits with {self.enemy.weapon.name}'
                      f' for {self.enemy.weapon.damage} damage. '
                      f'Hero health is {self.hero.health}.')

            if self.enemy.get_damage_source() is None:
                self.hero.take_damage(self.enemy.damage)
                print(f'Enemy hits hero'
                      f' for {self.enemy.damage} damage. '
                      f'Hero health is {self.hero.health}.')

            if not self.hero.is_alive():
                print('Our hero is dead!')
                break

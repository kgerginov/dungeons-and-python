class Unit:
    def __init__(self, health, mana):
        if self.validate_value(health):
            raise TypeError('Value must be a number!')
        if self.validate_value(mana):
            raise TypeError('Value must be a number!')
        self.health = health
        self.mana = mana
        self.__max_hp = health
        self.__max_mana = mana

    @staticmethod
    def validate_value(val):
        if val < 0:
            raise ValueError('Value cannot be negative!')
        if not isinstance(val, (int, float)):
            return True
        return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def can_cast(self):
        pass

    def take_damage(self, damage):
        if self.validate_value(damage):
            raise TypeError('Enter valid damage!')

        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

    def take_healing(self, healing_points):
        if self.validate_value(healing_points):
            raise TypeError('Enter valid healing points!')

        if not self.is_alive():
            return False

        if self.health + healing_points > self.__max_hp:
            self.health = self.__max_hp
        else:
            self.health += healing_points

    def take_mana(self, mana_points):
        if self.validate_value(mana_points):
            raise TypeError('Enter valid mana points!')

        if self.mana + mana_points > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana_points








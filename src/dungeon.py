from map_generator.dungeon_map_generator import Generator
from src.hero import Hero
from src.enemy import Enemy
from src.fight import Fight
from src.treasures import Treasure
from random import choice

SPAWNING_POINT = 'S'
EXIT = 'G'
WALL = '#'
WALKABLE_PATH = '.'
TREASURE = 'T'
ENEMY = 'E'
HERO = 'H'
map_sizes = ('large', 'small')


class DungeonMap:
    def __init__(self, map_size='small'):
        self.spawn_point = None
        self.layout = self.create_map(map_size)

    def create_map(self, map_size):
        if map_size not in map_sizes:
            raise ValueError('Choose small or large map!')

        if map_size == 'large':
            m = Generator(width=64, height=32)
            m.gen_level()
            layout = self._place_points_of_interest(
                    base_layout=m.gen_tiles_level(),
                    num_of_chests=5,
                    num_of_enemies=4
                    )

        if map_size == 'small':
            m = Generator(
                width=32, height=16, max_rooms=7,
                min_room_xy=4, max_room_xy=8
                )
            m.gen_level()
            layout = self._place_points_of_interest(
                        base_layout=m.gen_tiles_level(),
                        num_of_chests=3,
                        num_of_enemies=3
                    )

        return layout

    def _place_points_of_interest(self, base_layout, num_of_chests, num_of_enemies):
        layout_exit = self.__place_exit_point(base_layout)
        layout_spawn = self.__place_spawn_point(layout_exit)
        layout_treasure = self.__place_treasure(layout_spawn, num_of_chests)
        final_layout = self.__place_enemies(layout_treasure, num_of_enemies)
        return final_layout

    @staticmethod
    def __place_exit_point(layout):
        for row, elem in reversed(list(enumerate(layout))):
            col = choice(range(len(elem)))
            if layout[row][col] == WALL:
                layout[row][col] = EXIT

                return layout

    def __place_spawn_point(self, layout):
        for row, elem in enumerate(layout):
            for col, tile in enumerate(elem):
                if layout[row][col] == WALKABLE_PATH:
                    layout[row][col] = SPAWNING_POINT
                    self.spawn_point = row, col
                    return layout

    @staticmethod
    def __place_enemies(layout, num_of_enemies):
        n = 0
        while n != num_of_enemies:
            row = choice(range(len(layout)))
            col = choice(range(len(layout[row])))
            if layout[row][col] == WALKABLE_PATH:
                layout[row][col] = ENEMY
                n += 1
        return layout

    @staticmethod
    def __place_treasure(layout, num_of_chests):
        n = 0
        while n != num_of_chests:
            row = choice(range(len(layout)))
            col = choice(range(len(layout[row])))
            if layout[row][col] == WALKABLE_PATH:
                layout[row][col] = TREASURE
                n += 1
        return layout

    def print_map(self):
        return print('\n'.join([''.join(line) for line in self.layout]))


class Dungeon(DungeonMap):
    __directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'right': (0, 1),
        'left': (0, -1)
    }

    def __init__(self, layout='small'):
        super(Dungeon, self).__init__(layout)
        self.hero = None
        self.hero_pos = None
        self.treasure = Treasure()

    def set_hero_position(self, x, y):
        self.hero_pos = x, y

    def spawn(self, hero):
        if not isinstance(hero, Hero):
            return TypeError('Hero must be instance of Hero!')
        self.hero = hero
        row, col = self.spawn_point
        self.layout[row][col] = HERO
        self.hero_pos = row, col

    def get_treasure(self, treasure):
        # todo: Add prints for the treasures!!
        loot_name = treasure[0]
        item = treasure[1]
        if loot_name == 'health_potion':
            print(f'Found a health potion! With {item} healing points!')
            self.hero.take_healing(item)
        elif loot_name == 'weapon':
            print('..........')
            self.hero.equip_weapon(item)
        elif loot_name == 'spell':
            print('......')
            self.hero.learn_spell(item)

    def check_next_map_tile(self, x, y):
        # todo: Fix Prints!!
        map_tile = self.layout[x][y]
        if map_tile == WALL:
            return False
        if map_tile == WALKABLE_PATH:
            self.set_hero_position(x, y)
            self.layout[x][y] = HERO
            return True
        if map_tile == ENEMY:
            self.set_hero_position(x, y)
            e = Enemy(health=70, mana=50, damage=15)
            f = Fight(enemy=e, hero=self.hero)
            f.start_fight()
            return True
        if map_tile == TREASURE:
            self.set_hero_position(x, y)
            self.get_treasure(self.treasure.pick_treasure())
            return True
        if map_tile == EXIT:
            print('found exit gj')
            self.set_hero_position(x, y)
            return True

    def move_hero(self, direction):
        if not self.hero.is_alive():
            raise Exception('Hero is dead! You need a new Hero!')
        if direction in self.__directions:
            x, y = self.__directions[direction]
            cur_x, cur_y = self.hero_pos
            new_x = cur_x + x
            new_y = cur_y + y
            if self.check_next_map_tile(new_x, new_y):
                self.layout[cur_x][cur_y] = WALKABLE_PATH
            else:
                return False
        self.hero.take_mana(self.hero.mana_regeneration_rate)
        return True


m = Dungeon('small')
if __name__ == '__main__':
    m.print_map()
    print(m.spawn_point)
    m.spawn(Hero(name='Ivan', title='dr', health=150, mana=200, mana_regeneration_rate=2))
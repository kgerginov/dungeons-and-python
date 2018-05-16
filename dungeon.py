from src.hero import Hero
from map_generator.dungeon_map_generator import Generator
from random import choice


class Dungeon:


    def __init__(self, map_size='small'):
        self.dungeon_map = self.create_map
        self.hero_position = None
        self.enemy_position = None
        self.spawning_positions = self.find_spawning_points



    @property
    def read_map(self):
        row = self.dungeon_map.read()

        self.array_map = []

        for index in row.split():
            self.array_map.append(list(index))
        return self.array_map

    def print_map(self):
        return self.__str__()

    def close_file(self):
        if self.dungeon_map:
            self.dungeon_map.close()
            self.dungeon_map = None

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.array_map])

    def spawn(self, hero):
        if type(hero) is not Hero:
            raise ThisIsNotAHero
        if len(self.spawning_positions) == 0:
            raise NoMoreSpawnPoints
        self.hero = hero
        self.hero_position = self.spawning_positions.pop(0)
        self.array_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.HERO

    @property
    def find_spawning_points(self):
        spawn_points = []
        for cuurent_row, row in enumerate(self.array_map):
            for current_col, col in enumerate(row):
                if col == Dungeon.SPAWNING_POINT:
                    spawn_points.append((cuurent_row, current_col))
        return spawn_points


class ThisIsNotAHero:
    'Object is not a Hero instance'


class NoMoreSpawnPoints:
    'Ther is no more spawning positions'



# m = ['               ####      ', '  ##############..#######', '  #.....................#', '  #.###...........#####.#', '  #.# #...######..#####.#', '  ### #...............###', '      ######.....###..#  ', '           #....####..#  ', '           #####......#  ', '               ########  ', '                         ', '                         ', '               ####      ', '  ##############..#######', '  #.....................#', '  #.###...........#####.#', '  #.# #...######..#####.#', '  ### #...............###', '      ######.....###..#  ', '           #....####..#  ', '           #####......#  ', '               ########  ', '                         ', '                         ']
#
# _place_points_of_interest(m)


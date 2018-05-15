from src.hero import Hero


class Dungeon:
    SPAWNING_POINT = 'S'
    EXIT = 'G'
    WALL = '#'
    WALKABLE_PATH = '.'
    TRESURE = 'T'
    ENEMY = 'E'
    HERO = "H"

    def __init__(self, dungeon_map):
        self.dungeon_map = open(dungeon_map)
        self.array_map = self.read_map
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


map = Dungeon("level1.txt")
print(map.print_map())
print()
some_hero_instance = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
map.spawn(some_hero_instance)
print(map.print_map())

map.close_file()

from map_generator.dungeon_map_generator import Generator
from random import choice


class DungeonMap:

    SPAWNING_POINT = 'S'
    EXIT = 'G'
    WALL = '#'
    WALKABLE_PATH = '.'
    TREASURE = 'T'
    ENEMY = 'E'
    map_sizes = ('large', 'small')

    def __init__(self, map_size='small'):
        self.layout = self.create_map(map_size)

    def create_map(self, map_size):
        if map_size not in self.map_sizes:
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
                        num_of_chests=2,
                        num_of_enemies=2
                    )

        return layout

    def _place_points_of_interest(self, base_layout, num_of_chests, num_of_enemies):
        while True:
            layout_exit = self.__place_exit_point(base_layout)
            layout_spawn = self.__place_spawn_point(layout_exit)
            layout_treasure = self.__place_treasure(layout_spawn, num_of_chests)
            final_layout = self.__place_enemies(layout_treasure, num_of_enemies)
            return final_layout

    def __place_exit_point(self, layout):
        for row, elem in reversed(list(enumerate(layout))):
            col = choice(range(len(elem)))
            if layout[row][col] == self.WALL:
                layout[row][col] = self.EXIT
                return layout

    def __place_spawn_point(self, layout):
        for row, elem in enumerate(layout):
            for col, tile in enumerate(elem):
                if layout[row][col] == self.WALKABLE_PATH:
                    layout[row][col] = self.SPAWNING_POINT
                    return layout

    def __place_enemies(self, layout, num_of_enemies):
        n = 0
        while n != num_of_enemies:
            row = choice(range(len(layout)))
            col = choice(range(len(layout[row])))
            if layout[row][col] == self.WALKABLE_PATH:
                layout[row][col] = self.ENEMY
                n += 1
        return layout

    def __place_treasure(self, layout, num_of_chests):
        n = 0
        while n != num_of_chests:
            row = choice(range(len(layout)))
            col = choice(range(len(layout[row])))
            if layout[row][col] == self.WALKABLE_PATH:
                layout[row][col] = self.TREASURE
                n += 1
        return layout

    def print_map(self):
        return '\n'.join([''.join(line) for line in self.layout])


if __name__ == '__main__':
    m = DungeonMap(map_size='small')
    print(m.print_map())

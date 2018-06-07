from src.hero import Hero
from src.dungeon import Dungeon
import curses


def main():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    m = Dungeon()
    m.spawn(Hero(name='Ivan', title='Dr', health=100, mana=80, mana_regeneration_rate=2))
    while True:
        key = screen.getch()
        if key == ord('w'):
            m.move_hero(direction='up')
        elif key == ord('s'):
            m.move_hero(direction='down')
        elif key == ord('d'):
            m.move_hero(direction='right')
        elif key == ord('a'):
            m.move_hero(direction='left')
        m.print_map()


curses.wrapper(main())

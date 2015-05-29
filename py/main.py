# coding: utf-8

from game import Game

def main():
    g = Game()
    g.start()
    while (g.is_finished() == False):
        g.have_a_day()
    g.notify()

if __name__ == '__main__':
    main()


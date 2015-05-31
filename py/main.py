# coding: utf-8

import sys
sys.path.append("./Days")
from Days import Days
sys.path.append("./Player")
from Player import Jinrou, Villager, FortuneTeller, Psychic, Mad

def main():
    days = Days()
    days.main()

if __name__ == '__main__':
    main()


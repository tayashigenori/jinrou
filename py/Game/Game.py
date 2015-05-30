# coding: utf-8

import sys, os
root_dir = os.path.dirname( os.path.dirname(__file__) )
sys.path.append(root_dir + "./Day")
from Day import Day

class Game:
    def __init__(self,):
        return
    def start(self,):
        return
    def is_finished(self,):
        return
    def notify(self,):
        return
    def main(self,):
        self.start()
        day_num = 0
        while self.is_finished() == False:
            self.have_a_day(day_num)
            day_num += 1
        self.notify()
        return
    def have_a_day(self, day_num)
        d = Day(day_num)
        while d.is_finished() == False:
            d.main()
        return

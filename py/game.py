# coding: utf-8

from day import Day

class Game:
    def __init__(self,):
        self._day_num = 0 # 何日目か
        return
    def start(self,):
        return
    def have_a_day(self,):
        today = Day(self._day_num)
        today.process()
        self._day_num += 1
        return
    def is_finished(self,):
        return
    def notify(self,):
        return

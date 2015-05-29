# coding: utf-8

SPECIES_HUMAN = 1
SPECIES_JINROU = 2

GROUP_HUMAN = 1
GROUP_JINROU = 2

# すべての生き物
class Creature:
    def __init__(self,):
        self._target = False
        return
    def select(self, target):
        self._target = target
        return
    def talk(self,):
        return

class Human(Creature):
    def getSpecy(self,):
        return SPECIES_HUMAN
    def getGroup(self,):
        return GROUP_HUMAN
class Jinrou(Creature):
    def getSpecy(self,):
        return SPECIES_JINROU
    def getGroup(self,):
        return GROUP_JINROU
    def whisper(self,):
        return

# Humans
class Villager(Human): # 村人
    pass
class FortuneTeller(Human): # 占い師
    def execute(self, target):
        return
class Psychic(Human): # 霊能者
    def execute(self, target):
        return
class Hunter(Human): # 狩人
    pass
class Mad(Human): # 狂人
    def getGroup(self,):
        return GROUP_JINROU

import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
    def generate_damage(self):
        spelllow = self.dmg - 15
        spellhigh = self.dmg + 15
        return random.randrange(spelllow,spellhigh)
    def generate_healing(self):
        heallow = self.dmg - 10
        healhigh = self.dmg + 10
        return random.randrange(heallow,healhigh)
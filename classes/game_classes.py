import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[93m'
    WARNING = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_attack_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_healing(self, heal):
        self.hp += heal
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def spend_mp(self, cost):
        self.mp -= cost
    
    def select_action(self):
        i = 1
        print(bcolors.BOLD + bcolors.OKBLUE + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
    
    def select_spell(self):
        i = 1
        print(bcolors.BOLD + bcolors.OKGREEN + "Spells" + bcolors.ENDC)
        for Spell in self.magic:
            print(str(i) + ":", Spell.name, "(cost:", str(Spell.cost) + ")")
            i += 1

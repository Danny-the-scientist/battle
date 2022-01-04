import random
from .game_classes import bcolors
from .magic import spells

class characterTypes:
    def __init__(self, name, hp, mp, atk, phsdf, mgdef, magic, char, desc):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.phsdf = phsdf
        self.mgdef = mgdef
        self.magic = magic
        self.char = char
        self.desc = desc
        self.actions = ["Attack","Magic"]
        self.classtype = ["Barbarian", "Knight", "Black Mage", "Red Mage", "White Mage", "Fighter"]
        self.classdesc = ["High HP and damage, low defence and Spell abilities","Well rounded HP, attack, and defenses, limited healing abilities","Low HP, physical defense, and damage. Highest offensive Spell abilities and good Spell defense.","Lower HP and physical abilities. Good MP and Spell abilities. Able to use attack and healing spells","Low HP, defense, and damage. Excellent Spell abilities for healing and defense.","Very high HP and defense, but limited damage output. Able to heal minor wounds"]

    def generate_attack_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def physical_defense(self):
        return random.randrange(self.phsdf-30 , self.phsdf)

    def magic_defense(self):
        return random.randrange(self.mgdef-30, self.mgdef)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_healing(self, heal):
        self.hp += heal
        if self.hp < 0:
            self.hp = 0
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
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
            print(str(i) + ":", Spell.name, "(cost:", str(Spell.cost) + "):", Spell.desc)
            i += 1

    def select_character(self):
        i = 1
        print(bcolors.BOLD + bcolors.OKBLUE + "Character Types:\n" + bcolors.ENDC)
        for num in self.classtype:
            print(str(i) + " -" , num, ":", self.classdesc[i-1])
            i += 1
    
    def build_character(self,selection):
        barbarian = characterTypes("Barbarian", random.randrange(950, 1000), random.randrange(0,2), random.randrange(120,140), random.randrange(30,45), random.randrange(5, 15),[], "Barbarian", "High HP and damage, low defence and Spell abilities")
        knight = characterTypes("Knight", random.randrange(650, 700), random.randrange(30, 50), random.randrange(90, 110), random.randrange(60, 65), random.randrange(60, 65),[spells.heal], "Knight", "Well rounded HP, attack, and defenses, limited healing abilities")
        black_mage = characterTypes("Black Mage", random.randrange(300, 350), random.randrange(300, 350), random.randrange(30, 40), random.randrange(25, 30), random.randrange(90, 100),[spells.fire, spells.thunder, spells.blizzard, spells.meteor, spells.quake, spells.nova], "Black Mage", "Low HP, physical defense, and damage. Highest offensive Spell abilities and good Spell defense.")
        red_mage = characterTypes("Red Mage", random.randrange(450, 500), random.randrange(250, 300), random.randrange(60, 80), random.randrange(40, 50), random.randrange(80, 90),[spells.fire, spells.thunder, spells.blizzard, spells.heal, spells.heala], "Red Mage", "Lower HP and physical abilities. Good MP and Spell abilities. Able to use attack and healing spells")
        white_mage = characterTypes("White Mage", random.randrange(300, 350), random.randrange(350, 400), random.randrange(30, 40), random.randrange(25, 30), random.randrange(150, 160),[spells.heal, spells.heala, spells.healaga], "White Mage", "Low HP, defense, and damage. Excellent Spell abilities for healing and defense.")
        fighter = characterTypes("Fighter", random.randrange(1200,1300), random.randrange(15, 25), random.randrange(50, 70), random.randrange(100, 120), random.randrange(80, 100),[spells.heal], "Fighter", "Very high HP and defense, but limited damage output. Able to heal minor wounds")
        
        charlist = [barbarian, knight, black_mage, red_mage, white_mage, fighter]

        if int(selection) < len(charlist) and int(selection) >= 0:
            playpick = charlist[int(selection)]
            return(playpick)
        else:
            print("Please select an integer from the list above")
            newpick = (int(input())-1)
            if int(newpick) < len(charlist) and int(newpick) >= 0:
                playpick = charlist[int(newpick)]
                return(playpick)
            else:
                print("Seriously, please pick a valid number.")
                newpick1 = (int(input())-1)
                if int(newpick1) < len(charlist) and int(newpick1) >= 0:
                    playpick = charlist[int(newpick1)]
                    return(playpick)
                else:
                    print("One more chance. I mean it!")
                    newpick2 = (int(input())-1)
                    if int(newpick2) < (len(charlist)) and int(newpick2) >= 0:
                        playpick = charlist[int(newpick2)]
                        return(playpick)
                    else:
                        print(bcolors.UNDERLINE + bcolors.WARNING + bcolors.BOLD + "Fine! Have it your way!\n\n" + bcolors.ENDC)
                        playpick = characterTypes("Didn't listen",10,0,1,1,1,[],"Oaf","I didn't listen!")
                        return(playpick)
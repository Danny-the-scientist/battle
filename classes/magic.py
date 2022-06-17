import random

class Spell:
    def __init__(self, name, cost, dmg, desc, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.desc = desc
        self.type = type

    def generate_damage(self):
        spelllow = self.dmg - 15
        spellhigh = self.dmg + 15
        return random.randrange(spelllow,spellhigh)

    def generate_healing(self):
        heallow = self.dmg - 10
        healhigh = self.dmg + 10
        return random.randrange(heallow,healhigh)

class spells:
    fire = Spell("Fire", 10, 100, "A small flame billows forth, doing ~100 damage", "black")
    thunder = Spell("Thunder", 12, 115, "A massive thunderclap overwhelms the target's hearing, doing ~115 damage","black")
    blizzard = Spell("Blizzard", 15, 140,"Summons a massive storm of ice and snow, doing ~140 damage", "black")
    meteor = Spell("Meteor", 22, 225,"Calls down a stone from the atmosphere onto the enemy, doing ~225 damage", "black")
    quake = Spell("Quake", 17, 190,"Shakes the ground under the enemy, sending them falling off balance, doing ~190 damage", "black")
    nova = Spell("Nova", 30, 310,"Creates a massive explosion engulfing the enemy, doing ~310 damage", "black")

    heal = Spell("Heal", 8, 80,"Heals relatively small wounds, restoring ~80 HP", "white")
    heala = Spell("Heala", 18, 170,"Heals moderate wounds, restoring ~170 HP", "white")
    healaga = Spell("Healaga", 22, 210,"Heals severe wounds, restoring ~210 HP", "white")
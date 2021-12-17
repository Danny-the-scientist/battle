from classes.game_classes import Person, bcolors
from classes.magic import Spell

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 115, "black")
blizzard = Spell("Blizzard", 13, 130, "black")
meteor = Spell("Meteor", 20, 215, "black")
quake = Spell("Quake", 17, 190, "black")

heal = Spell("Heal", 15, 120, "white")
heala = Spell("Heala", 18, 150, "white")


player = Person(480, 700, 12, 25, [fire,thunder,blizzard,meteor,heal,heala]) 
enemy1 = Person(1300, 20, 40, 30, [])

running = True
i = 0

print (bcolors.FAIL + bcolors.BOLD + "AN ENEMY APPROCHES WITH MALICE!" + bcolors.ENDC)

while running:
    print("========================")
    player.select_action()
    selection = input("Choose action:")
    index = int(selection) - 1

    if index == 0:
        dmg = player.generate_attack_damage()
        enemy1.take_damage(dmg)
        print("You hit the enemy for", dmg, "points of damage!")
    elif index == 1:
        player.select_spell()
        spell = int(input("Select Spell:")) - 1

        magic = player.magic[spell]
        
        current_mp = player.get_mp()

        if magic.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP!\n" +bcolors.ENDC)
            continue
        
        player.spend_mp(magic.cost)
        if magic.type == "black":
            spell_dmg = magic.generate_damage()
            enemy1.take_damage(spell_dmg)
            print(bcolors.OKBLUE + "\n" + magic.name + " deals", str(spell_dmg), "points of damage!" + bcolors.ENDC)
        elif magic.type == "white":
            spell_heal = magic.generate_healing()
            player.get_healing(spell_heal)
            print(bcolors.OKBLUE + "\n" + magic.name + " heals player for", str(spell_dmg), "HP!" + bcolors.ENDC)
    
    enemy1_choice = 1

    enemy1_dmg = enemy1.generate_attack_damage()
    player.take_damage(enemy1_dmg)
    print("Enemy strikes for", enemy1_dmg, "points of damage!")

    print("--------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC + "\nEnemy MP:", bcolors.FAIL + str(enemy1.get_mp()) + "/" + str(enemy1.get_max_mp()) + bcolors.ENDC + "\n")
    print("Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\nPlayer MP:", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy1.get_hp() == 0:
        print(bcolors.OKGREEN, bcolors.BOLD, "You Win!", bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.BOLD, bcolors.FAIL, "You are dead! Try again!", bcolors.ENDC)
        running = False

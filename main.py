'''
Simple RPG Battle Simulator:
Based on foundations of Stack Skills' Python course and added significant flair
Make it easy to add new class types, spells, etc., adjust enemy
Daniel (Danny) C
'''

from classes.characters import characterTypes
from classes.game_classes import Person, bcolors

enemy1 = Person("enemy1", 1300, 20, 60, 30, 10, [], "Brute") #Instantiate the baddie; TODO - make it so there can be more than 1 enemy

running = True #keep the fight going until the end
i = 0

'''
print(bcolors.BOLD + bcolors.OKGREEN + "Welcome to the fight! Please input the size of your party (1-3):")#TODO establish dynamic Party number and loop through selections and actions

partysize = range(int(input("Members:")))
party = []
'''

'''Acquire user input'''
print(bcolors.BOLD + bcolors.OKGREEN + "Welcome to the fight! Please input your character's name!")
name = input("\n Character Name:")

print("\n Welcome, " + name + "!")
player = characterTypes(name,0,0,0,0,0,[],"","")
player.select_character()

charPick = int(input("\n" + name + ", please choose your character type:"))
player = player.build_character(charPick - 1)

player.name = name
print (bcolors.BOLD + bcolors.OKBLUE + bcolors.UNDERLINE + "\nGood to have you, " + name + " the " + player.char + "!" + bcolors.ENDC)


print (bcolors.FAIL + bcolors.BOLD + "\n\n\nA " + enemy1.desc + " approaches with malice!!!!" + bcolors.ENDC)

while running:

    print("========================")
    player.select_action()
    selection = input("Choose action:")
    index = int(selection) - 1

    if index == 0:
        dmg = player.generate_attack_damage()
        enemy1_def = enemy1.physical_defense()
        if enemy1_def < 0:
            enemy1_def = 0
        enemy1.take_damage(dmg-enemy1_def)
        print("\n" + name + " hits the enemy for", dmg, "points of damage!", "The enemy blocks ", enemy1_def, " points, taking a total of ", str(dmg-enemy1_def), " damage!")
    elif index == 1:
        player.select_spell()
        spell = int(input("Select Spell:")) - 1

        magic = player.magic[spell]
        
        current_mp = player.get_mp()

        if magic.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP!\n" + bcolors.ENDC)
            continue
        
        player.spend_mp(magic.cost)
        if magic.type == "black":
            spell_dmg = magic.generate_damage()
            enemey1_mgdef = enemy1.magic_defense()
            if enemey1_mgdef < 0:
                enemey1_mgdef = 0
            enemy1.take_damage(spell_dmg-enemey1_mgdef)
            print(bcolors.OKBLUE + "\n" + magic.name + " from " + name +  " deals " + str(spell_dmg) + " points of damage! " + enemy1.desc + " blocks " + str(enemey1_mgdef) + ", taking " + str(spell_dmg-enemey1_mgdef) + " damage!" + bcolors.ENDC)
        elif magic.type == "white":
            spell_heal = magic.generate_healing()
            player.get_healing(spell_heal)
            print(bcolors.OKBLUE + "\n" + magic.name + " heals " + name + " for ", str(spell_heal), "HP!" + bcolors.ENDC)
    
    enemy1_choice = 1 #TODO - give enemy randomized "AI" options for combat choices

    enemy1_dmg = enemy1.generate_attack_damage()
    player_def = player.physical_defense()
    
    if player_def < 0:
        player_def = 0

    enemy1_dmg_mod = enemy1_dmg-player_def
    if enemy1_dmg_mod < 0:
        enemy1_dmg_mod = 0
    player.take_damage(enemy1_dmg_mod)
    
    print("\n" + enemy1.desc + " strikes " +  name + " for " + str(enemy1_dmg) + " points of damage! " + name + " blocks " + str(player_def) + " points, taking " + str(enemy1_dmg_mod) + " damage!")

    print("--------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC + "\nEnemy MP:", bcolors.OKGREEN + str(enemy1.get_mp()) + "/" + str(enemy1.get_max_mp()) + bcolors.ENDC + "\n")
    print("Player HP:", bcolors.FAIL + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\nPlayer MP:", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy1.get_hp() == 0:
        print(bcolors.OKGREEN, bcolors.BOLD, name, "wins! CONGRATULATIONS!", bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.BOLD, bcolors.FAIL, name, "slumps to the ground, defeated. Try again!", bcolors.ENDC)
        running = False

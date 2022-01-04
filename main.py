'''
Simple RPG Battle Simulator:
Based on foundations of Stack Skills' Python course and added significant flair
Make it easy to add new class types, spells, etc., adjust enemy
Daniel (Danny) C
'''

from random import randrange
from classes.magic import Spell
from classes.characters import characterTypes
from classes.game_classes import Person, bcolors
from classes.magic import spells

enemy1 = Person("enemy1", 1300, 40, 60, 30, 10, [spells.fire,spells.thunder], "Brute") #Instantiate the baddie; TODO - make it so there can be more than 1 enemy

running = True #keep the fight going until the end
i = 0

'''
print(bcolors.BOLD + bcolors.OKGREEN + "Welcome to the fight! Please input the size of your party (1-3):")#TODO establish dynamic Party number and loop through selections and actions

partysize = range(int(input("Members:")))
party = []
'''

'''Acquire user input for character'''
print(bcolors.BOLD + bcolors.OKGREEN + "Welcome to the fight! Please input your character's name!")
name = input("\n Character Name:")#Player inputs string for name

print("\n Welcome, " + name + "!")
player = characterTypes(name,0,0,0,0,0,[],"","")#Instantiate Player object to be replaced with build_character func
player.select_character()

charPick = int(input("\n" + name + ", please choose your character type:"))
player = player.build_character(charPick - 1)

player.name = name
#playerspells = [str(num) for num in player.magic] TODO make printing spell names work

'''Print character info following randomized number building'''
print(bcolors.BOLD + bcolors.WARNING + bcolors.UNDERLINE + "\nGood to have you, " + name + " the " + player.char + "!" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + bcolors.UNDERLINE + "\nNAME -" + bcolors.ENDC + name)
print(bcolors.BOLD + bcolors.WARNING + bcolors.UNDERLINE + "\nHP -" + bcolors.ENDC + str(player.get_max_hp()))
print(bcolors.BOLD + bcolors.WARNING + bcolors.UNDERLINE + "\nMP -" + bcolors.ENDC + str(player.get_max_mp()))
#print(bcolors.BOLD + bcolors.WARNING + bcolors.UNDERLINE + "\nSpells -" + bcolors.ENDC + ",".join(playerspells)) TODO make printing list of spells work


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
    else:
        continue
    
    enemy1_choice = randrange(1,3)#'AI' of enemy to select either attack or magic

    if enemy1_choice == 1:
            enemy1_dmg = enemy1.generate_attack_damage()
            player_def = player.physical_defense()
        
            if player_def < 0:
                player_def = 0

            enemy1_dmg_mod = enemy1_dmg-player_def
            if enemy1_dmg_mod < 0:
                enemy1_dmg_mod = 0
            player.take_damage(enemy1_dmg_mod)
            
            print("\n" + enemy1.desc + " strikes " +  name + " for " + str(enemy1_dmg) + " points of damage! " + name + " blocks " + str(player_def) + " points, taking " + str(enemy1_dmg_mod) + " damage!")
    
    if enemy1_choice == 2:
        spell = randrange(0,len(enemy1.magic))#enemy selects a random spell to use

        magic = enemy1.magic[spell]
        
        current_mp = enemy1.get_mp()

        if magic.cost > current_mp:#if the enemy does not have enough MP for the spell, it defaults back to a standard pysical attack
            enemy1_dmg = enemy1.generate_attack_damage()
            player_def = player.physical_defense()
        
            if player_def < 0:
                player_def = 0

            enemy1_dmg_mod = enemy1_dmg-player_def
            if enemy1_dmg_mod < 0:
                enemy1_dmg_mod = 0
            player.take_damage(enemy1_dmg_mod)
            
            print("\n" + enemy1.desc + " is low on MP, and instead strikes " +  name + " for " + str(enemy1_dmg) + " points of damage! " + name + " blocks " + str(player_def) + " points, taking " + str(enemy1_dmg_mod) + " damage!")
            print("--------------------------------")
            print("Enemy HP:", bcolors.FAIL + str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC + "\nEnemy MP:", bcolors.OKGREEN + str(enemy1.get_mp()) + "/" + str(enemy1.get_max_mp()) + bcolors.ENDC + "\n")
            print("Player HP:", bcolors.FAIL + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\nPlayer MP:", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
            continue
        
        enemy1.spend_mp(magic.cost)
        if magic.type == "black":
            spell_dmg = magic.generate_damage()
            player_mgdef = player.magic_defense()
            if player_mgdef < 0:
                player_mgdef = 0

            enemy1_dmg_mod = spell_dmg - player_mgdef
            if enemy1_dmg_mod < 0:
                enemy1_dmg_mod = 0
            player.take_damage(enemy1_dmg_mod)

            print(bcolors.OKBLUE + "\n" + magic.name + " from " + enemy1.desc +  " deals " + str(spell_dmg) + " points of damage! " + player.name + " blocks " + str(player_mgdef) + ", taking " + str(enemy1_dmg_mod) + " damage!" + bcolors.ENDC)
        elif magic.type == "white":
            spell_heal = magic.generate_healing()
            enemy1.get_healing(spell_heal)
            print(bcolors.OKBLUE + "\n" + magic.name + " heals " + enemy1.desc + " for ", str(spell_heal), "HP!" + bcolors.ENDC)
    
    print("--------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC + "\nEnemy MP:", bcolors.OKGREEN + str(enemy1.get_mp()) + "/" + str(enemy1.get_max_mp()) + bcolors.ENDC + "\n")
    print("Player HP:", bcolors.FAIL + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\nPlayer MP:", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy1.get_hp() == 0:
        print(bcolors.OKGREEN, bcolors.BOLD, name, "wins! CONGRATULATIONS!", bcolors.ENDC)
        running = False #end the while loop based on whether player or enemy dies
    elif player.get_hp() == 0:
        print(bcolors.BOLD, bcolors.FAIL, name, "slumps to the ground, defeated. Try again!", bcolors.ENDC)
        running = False #end the while loop based on whether player or enemy dies
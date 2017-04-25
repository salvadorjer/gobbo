import random

#VALUES############################################################################################################################################
##Player Values##
pc_hp = 0
pc_spd = 0
pc_def = 0+pc_spd
pc_atk = 0
pc_str = 0
dam = 0
##Enemy Values##
en_spd = 0
en_def = 0
en_name = "0"
en_dam = 0
en_str = 0
en_hp = 0
en_atk = 0
###################################################################################################################################################

#DEFTIONS##########################################################################################################################################
#Should set up the statistics for the player and report them to the rest of the game.

def weapon_selection(pc_atk): ##sets up the offensive value of the player## ##works!##
    print ("On the table infront of you sits an Axe, a Sword, and two Daggers. Which would you like to select?")##sets up basic three choices
    player_weapon1=input()
    if player_weapon1 =="Axe":
        pc_atk = 3
        print ("You have picked up the worn battle axe.")
        return pc_atk
    elif player_weapon1 =="Sword":
        pc_atk = 2
        print ("You have picked up the rusty sword.")
        return pc_atk                    
    elif player_weapon1 == "Daggers":
        pc_atk = 1
        print ("You have picked up the two small daggers.")
        return pc_atk
    elif player_weapon1 == "GOD MODE!":
        pc_atk = 4
        return pc_atk

def player_weapon_damage (pc_atk, pc_spd, pc_str, dam, en_def): ##sets the damage int for the players weapon##
    x= pc_atk
    if x == 1:
        dam = random.randint(1, 4)+pc_spd-en_def
        return dam
    if x == 2:
        dam = random.randint(1, 8)+pc_str-en_def
        return dam
    if x == 3:
        dam = random.randint(1, 12)+pc_str-en_def
        return dam
    if x == 4:
        dam = 10000
        return dam
def player_race (pc_str, pc_spd, pc_hp): ##sets pc base stats!##
    print ("First things are first, what race are you? At the momment your choices are: Human, Fey, or Fel. Humans favor balance, Fey favor speed, and Fel favor strengt. Make your choice now.")
    race=input()
    if race == "Human":
        pc_str = 2; pc_spd = 2; pc_hp = 30
        return pc_str, pc_spd, pc_hp    
    elif race == "Fey":
        pc_str = 1; pc_spd = 4; pc_hp = 25
        return pc_str, pc_spd, pc_hp
    elif race == "Fel":
        pc_str = 4; pc_spd = 1; pc_hp = 25
        return pc_str, pc_spd, pc_hp
    
def training_dumby (en_atk, en_spd, en_hp, en_name, en_str, en_def): ##will randomly generate a training dumby to fight##
    training = random.randint(1, 4)
    if training == 1:
        en_atk = 0; en_spd = 0; en_hp = 1000; en_name = "Training Dumby 1"; en_str = 1; en_def = 1+en_spd
        return en_atk, en_spd, en_hp, en_name, en_str, en_def
    if training == 2:
        en_atk = 0; en_spd = 0; en_hp = 1000; en_name = "Training Dumby 2"; en_str = 3; en_def = 1+en_spd
        return en_atk, en_spd, en_hp, en_name, en_str, en_def
    if training == 3:
        en_atk = 0; en_spd = 0; en_hp = 1000; en_name = "Training Dumby 3"; en_str = 7; en_def = 1+en_spd
        return en_atk, en_spd, en_hp, en_name, en_str, en_def
    if training == 4:
        en_atk = 0; en_spd = 0; en_hp = 1000; en_name = "Training Dumby 1"; en_str = 1; en_def = 1+en_spd
        return en_atk, en_spd, en_hp, en_name, en_str, en_def
        
def combat (pc_hp, pc_def, pc_atk, pc_str, pc_spd, dam, en_atk, en_spd, en_hp, en_name, en_str, en_def): ##combat program!##s
    y=0
    print ("You step into the arena. Across the bloodied sand you see a fearsome", en_name) ##start combat##
    if pc_spd > en_spd:
        print ("You get the drop on", en_name, "what would you like to do? Charge(Charge) or Stand Your Ground(Defend)? Charging will allow you to strike the first blow.")
        initiate=input()
        if initiate == "Charge" or initiate == "c":
            print ("You rush forward before the", en_name, "is ready for you and deliver a mighty blow.")
            en_hp -= dam
            print ("You do:", dam)
            print ("The", en_name, "is now at:", en_hp)
        elif initiate == "Defend" or initisate == "d":
            print ("You raise your shield as the", en_name, "makes the first move.")
            pc_hp -= en_atk-(pc_def+pc_def)
        if pc_hp <= 0:
            print ("You have lost your fight!")
            print ("GAME OVER!")
            y=1
        if en_hp <= 0:
            print ("You have won your fight!")
            print ("Congrats!")
            y=1
    elif pc_spd < en_spd:
        print ("Before you have regained your composure from the sight before you", en_name, "charges!")
        pc_hp -= en_atk-pc_def
        print (en_name, "does:", pc_hp)
        print ("You are now at:". pc_hp)
        if pc_hp <= 0:
            print ("You have lost your fight!")
            print ("GAME OVER!")
            y=1
        if en_hp <= 0:
            print ("You have won your fight!")
            print ("Congrats!")
            y=1
    while y==0: ## start of repetition ##
        if pc_spd > en_spd:
            print ("It is your turn! What would you like to do? Brutally Attack (Attack twice at the cost of defense), Attack (Attack once with no penalty), Defend (Do not attack for additional defense).")
            action=input()
            if action== "Brutally Attack" or action=="b":
                print ("You swing your weapon at", en_name, "and deliver a blow.")
                en_hp -= dam
                print ("You do:", dam)
                print ("The", en_name, "is now at:", en_hp)
                print ("Throwing caution to the winds you swing again", en_name, "and deliver a mighty blow.")
                en_hp -= dam
                print ("You do:", dam)
                print ("The", en_name, "is now at:", en_hp)
                print ("The", en_name, "swings its weapon at you!")
                pc_hp -= en_atk
                print (en_name, "does:", en_atk)
                print ("You are now at:", pc_hp)
            elif action == "Attack" or action=="a":
                print ("You swing your weapon at", en_name, "and deliver a blow.")
                en_hp -= dam
                print ("You do:", dam)
                print ("The", en_name, "is now at:", en_hp)
                print ("The", en_name, "swings its weapon at you!")
                pc_hp -= en_atk-pc_def
                print (en_name, "does:", en_atk-pc_def)
                print ("You are now at:", pc_hp)
            elif action == "Defend"or action=="d":
                print ("You ready your weapon to defend yourself.")
                print ("The", en_name, "swings its weapon at you!")
                pc_hp -= en_atk-pc_def
                print (en_name, "does:", en_atk-pc_def)
                print ("You are now at:", pc_hp)
        if pc_hp <= 0:
                print ("You have lost your fight!")
                print ("GAME OVER!")
                y=1
        if en_hp <= 0:
                print ("You have won your fight!")
                print ("Congrats!")
                y=1
                
                
                
        
    
           

   
###################################################################################################################################################

#TEST##############################################################################################################################################

print ("Welcome to the Testing Range! What would you like to fight today? Right now we have a: Training Dumby.") 
enemy=input() ##this will eventually allow for additional enemies to be added##
if enemy== "Training Dumby" or enemy=="t":
    en_atk, en_spd, en_hp, en_name, en_str, en_def = training_dumby (en_atk, en_spd, en_hp, en_name, en_str, en_def) ##sets up training dumby to fight##
pc_str, pc_spd, pc_hp = player_race (pc_str, pc_spd, pc_hp) ##sets player race##
pc_atk = weapon_selection(pc_atk) ##sets player weapon##
dam = player_weapon_damage (pc_atk, pc_spd, pc_str, dam, en_def) ##sets player damage##
combat (pc_hp, pc_def, pc_atk, pc_str, pc_spd, dam, en_atk, en_spd, en_hp, en_name, en_str, en_def) ##the fight starts!##


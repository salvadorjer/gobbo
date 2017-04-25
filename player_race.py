def player_race (pc_str, pc_spd, pc_def, pc_atk, pc_hp): ##sets pc base stats!##
    print ("First things are first, what race are you? At the momment your choices are: Human, Fey, or Fel. Humans favor balance, Fey favor speed, and Fel favor strengt. Make your choice now.")
    race=input()
    
    if race == "Human":
        pc_str = 4; pc_spd = 4; pc_def = 0; pc_atk = 0; pc_hp = 30 ##str = mod to dam, pc spd = int order maybe def, pc atk = given by weapon##
                                                                   ##ignore cirts on humans##
    elif race == "Fey":
        pc_str = 2; pc_spd = 7; pc_def = 0; pc_atk = 0; pc_hp = 25 ##faster then humans##
        
    elif race == "Fel":
        pc_str = 7; pc_spd = 2; pc_def = 0; pc_atk = 0; pc_hp = 25 ##stronger then humans##



######
#Kind of ran in two different directions with this: do we want the fights to be 1v1
# or group v group?
#you need goblin.txt in the same directory to run this
######

######
#Attack types
#blast-hits all squares
#melee-hits a front rank of your choice or, if there is no front rank, a back of your choice
#range-hits any one target
#self-affects only user
#random-hits a random enemy
######

pc=["John","Cena"]#for less OP results replace pc[] with proper list of pc's



"""
def combat
    init_pc = grp_spd ##player initiative order##    ## 4 is an average stat. 6 should be the human maximum (maybe 7?) Above that is super human, below 4 is poor with 1 being the worst a person can be##
    init_en = pat_spd ##monster initiative##      ## if we are having other races they ofcourse would follow a diffrent racial noraml than humans##
    if init >= (2*init_en): ##player gets suprise round##                 ## need a character creator program##
    elif (init*2) <= init_en: ##if monster gets surprise round##          ## disciple 2 positioning ##
    elif init > init_en: ##player goes first##
    elif init < init_en: ##if monster goes first##
    elif init = init_en: ##tie breaker round##                          ## Need multiple people, need targeting, defend, attack ##
     "first" = random.randint (1, 2)
         if "first" == 1 ##player goes##
         if "first" == 2 ## monster goes first##
"""

def getenemy(enemy):
    stats=open("{}.txt".format(enemy),"r")#pulling from goblin.txt in same directory
    for line in stats:
        line=line.strip()
        if line[0:6]=="en_nam":
            en_nam=line[7:100]
            print(en_nam)
        elif line[0:6]=="en_htp":
            en_htp=int(line[7:100])
            print(en_htp)
        elif line[0:6]=="en_att":
            en_att=int(line[7:100])
            print(en_att)
        elif line[0:6]=="en_spd":
            en_spd=int(line[7:100])
            print(en_spd)
        elif line[0:6]=="en_str":
            en_str=int(line[7:100])
            print(en_str)
    return (en_nam,en_htp,en_att,en_spd,en_str)

enemy="goblin"#change value of enemy to pull from a different file
enemystats=getenemy(enemy)#all stats are saved as a tuple called enemystats
print(enemystats)

pcstats=("boondogle",20,3,1,3)#boondogle's arbitrary stats
print(pcstats)

def placeteam(pc):
    pc_teamsize=len(pc)
    w=3
    h=2
    pc_side=[["" for x in range(w)] for y in range(h)]
    en_side=[["" for x in range(w)] for y in range(h)]
    en_side[0][1]="1"
    for x in range(pc_teamsize):
        print("Do you want to put {} in front or back rank?".format(pc[x]))
        rank=input()
        print("Do you want to put {} in the left, middle or right?".format(pc[x]))
        place=input()

        if rank=="front" or rank=="f":
            if place=="left" or place=="l":
                pc_side[0][0]=pc[x]
            elif place=="middle" or place=="m":
                pc_side[0][1]=pc[x]
            elif place=="right" or place=="r":
                pc_side[0][2]=pc[x]
            else:
                print("You done f'd up!")
        elif rank=="back" or rank=="b":
            if place=="left" or place=="l":
                pc_side[1][0]=pc[x]
            elif place=="middle" or place=="m":
                pc_side[1][1]=pc[x]
            elif place=="right" or place=="r":
                pc_side[1][2]=pc[x]
            else:
                print("error error initiating launch sequence.")
        else:
            print("you screwed up: time to run the team placement definition again")
            placeteam()
        
    print(en_side[0])
    print(en_side[1])
    print()
    print(pc_side[0])
    print(pc_side[1])
    return en_side,pc_side

def combat(enemystats,pcstats):
    en_nam,en_htp,en_att,en_spd,en_str=enemystats#we now have all the stats for the fight
    pc_nam,pc_htp,pc_att,pc_spd,pc_str=pcstats

    print("this is a fight between {}".format(pc_nam),"and {}".format(en_nam))

    
placeteam(pc)
combat(enemystats,pcstats)

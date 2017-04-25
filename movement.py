###currently monster does nothing (will actually get overwitten by player)

#leave comments to one another here

#the only way i ever see skill coming into this w/o real time is monster resistances
#or different attributes like some might move towards you and if you have to rest
#you try to make sure they don't all hit you in a row or somthing like that.


import random

map=[["."]*5 for _ in range(5)]

currentx=0
currenty=0

player_HP=20


def printmap (map):#simple easy print, can get rid of shitty characters later but
        print(map[0])#will require more obtuse coding
        print(map[1])
        print(map[2])
        print(map[3])
        print(map[4])
        print("xy coordinates are",currentx,currenty)
        print("player HP:",player_HP)

def movesouth (map,currentx,currenty):
    if currentx<4:
        map[currentx][currenty]="."
        currentx=currentx+1
        if map[currentx][currenty]!=".":
                fight()
        map[currentx][currenty]="X"
        return (currentx)
    else:
        print("cannot go further south")
        return (currentx)

def movenorth (map,currentx,currenty):
    if currentx>0:
        map[currentx][currenty]="."
        currentx=currentx-1
        if map[currentx][currenty]!=".":
                fight()
        map[currentx][currenty]="X"
        return (currentx)
    else:
        print("cannot go further north")
        return (currentx)

def moveeast (map,currentx,currenty):
    if currenty<4:
        map[currentx][currenty]="."
        currenty=currenty+1
        if map[currentx][currenty]!=".":
                fight()
        map[currentx][currenty]="X"
        return (currenty)
    else:
        print("cannot go further east")
        return (currenty)

def movewest (map,currentx,currenty):
    if currenty>0:
        map[currentx][currenty]="."
        currenty=currenty-1
        if map[currentx][currenty]!=".":
                fight()
        map[currentx][currenty]="X"
        return (currenty)
    else:
        print("cannot go further west")
        return (currenty)

def randmonster(map):#places a random monster on a random square
    monsterx=random.randint(0,4)
    monstery=random.randint(0,4)
    gobormin=random.randint(1,2)#goblin or minotaur that is the question
    if gobormin==1:
        map[monsterx][monstery]="G"
    elif gobormin==2:
        map[monsterx][monstery]="M"

def fight():
    import Testing_Range
    print("Program a fight you lazy bum!!!!!")
    print("Program a fight you lazy bum!!!!!")
    print("Program a fight you lazy bum!!!!!")
    print("Program a fight you lazy bum!!!!!")
    print("Program a fight you lazy bum!!!!!")


randmonster(map)

map[0][0]="X"

printmap (map)

direction="null"
while direction!="done":#keeps doing until you enter done
    print("would you like to go north/south/east/west? done ends program")
    direction=input()
    if direction=="north"or direction=="n":
        print("now we move north")
        currentx=movenorth(map,currentx,currenty)#line to move north
        printmap(map)
    elif direction=="south"or direction=="s":
        print("now we move south")
        currentx=movesouth(map,currentx,currenty)#line to move south
        printmap(map)
    elif direction=="east"or direction=="e":
        print("now we move east")
        currenty=moveeast(map,currentx,currenty)#line to move east
        printmap(map)
    elif direction=="west"or direction=="w":
        print("now we move west")
        currenty=movewest(map,currentx,currenty)#line to move west
        printmap(map)
        

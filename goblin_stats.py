en_name="grunty"
en_hp=15
en_att=2
en_spd=3
en_str=3#could make this be the strength scaling so every attack would be att+random.randint(0,en_str)
en_res="none"

#when running a tuple it's: (name,hp,att,spd,str)

actions=2#sets number of possible actions for randomisation of attacks+data reading
action1=("stab","melee",2)
#------name^-type^-dmg mod^
action2=("throw rock","range",0)



###tried to expand, pretty sure import_test gets run twice
from import_test import x
print("i get auto run")
print(x)

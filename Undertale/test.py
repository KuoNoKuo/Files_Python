_list = [
    'Valorant',
    'Minecraft',
    'Horizon',
    'Brawlhalla',
    'Mario',
    'Halo: Infinite warfare',
    'Totally Accurate Battle Simulator',
    'Hollow Knight',
    'Cuphead',
]
def _________________________________________________________________():
    print()
#import libraries
import random
import time
#import another file's content

#-------MAIN SCRIPT

# FOR LOOPS
for i in range(len(_list)-1):
    print(_list[i])

_________________________________________________________________()
_________________________________________________________________()

deez = 0
while deez < 9:
    print(_list[deez])
    deez += 1

_________________________________________________________________()
_________________________________________________________________()

print('\n'.join(map(str, _list)))

_________________________________________________________________()
_________________________________________________________________()

[print(i) for i in _list]

_________________________________________________________________()
_________________________________________________________________()

for x in _list:
    print(x)

_________________________________________________________________()
_________________________________________________________________()

# FUNCTIONS (def)
def judgement(answer):
    if answer == 0:
        print("Get Lost")
    if answer == 1:
        print("nice")

answer = int(input("are you gay? (1 or 0)"))
judgement(answer)

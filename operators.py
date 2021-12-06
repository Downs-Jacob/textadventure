from objects import *
from rooms import *
import os
import sys
from time import sleep

#moves the user to another room, if it is possible to move in that direction.
def go(direction,room):
    possible=False
    if direction in exits[room]:
        if len(exits[room][direction])==1:     
            possible=True
        elif len(exits[room][direction])>1:
            if exits[room][direction][1] in inventory:
                possible=True
    if possible==True:
        room=exits[room][direction][0]
        roomDetails(room)
    else:
        print("It's not currently possible to move in that direction")
    return room

#moves an object that is hiding another object.
def move(object,room):
    if object in hidden and object in objects[room]:
        print("You have moved",object,"and revealed:",hidden[object])
        del hidden[object]
    else:
        print("It isn't possible to move this object")

#allows the user to add an object to their inventory.
def collect(object,room):
    if object in objects[room]:
        inventory.append(object)
        print(object,"has been added to your inventory.")
    else:
        print("It isn't possible to add this object to your inventory.")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def displayText(sentence):
    for char in sentence:
        sleep(0.06)
        sys.stdout.write(char)
        sys.stdout.flush()
def characterSetup():
    name = []
    charName = input()
    name.append(charName)
    print("Hello"+ name[0]+", welcome to the world of Lirr")
    
from rooms import *
from objects import *
from operators import *
from intro import intro

intro()

#sets the starting room and displays its details.
currentRoom="Street"
roomDetails(currentRoom)

#allows the user to enter a command and takes the appropriate action.
while True:
    command=input(": ")
    command=command.split()
    if command[0].lower()=="go":
        currentRoom=go(command[1].lower(),currentRoom)
    elif command[0].lower()=="move":
        move(command[1],currentRoom)
    elif command[0].lower()=="collect":
        collect(command[1],currentRoom)
    elif command[0].lower()=="inventory":
        print("You have the following items:")
        print(inventory)
    else:
        print("I'm sorry I didn't understand that command.")
    

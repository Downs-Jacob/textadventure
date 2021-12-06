from objects import *

#defines the rooms in the game with descriptions.
rooms={"Street":"outside the HQ",
       "Lobby":"the lobby of the HQ",
       "Lift":"the main lift",
       "1st Floor":"the first floor of the HQ"}


#defines the exits that each room has and which room the exits lead to
#optionally you can define an object that must be in the inventory in
#order to move through the exit.
exits={"Street":{"east":["Lobby"]},
       "Lobby":{"west":["Street"],"north":["Lift"]},
       "Lift":{"south":["Lobby"],"up":["1st Floor","KeyCard"]},
       "1st Floor":{"north":["Lift"]}}

#outputs the details for a room including non-hidden objects.
def roomDetails(room):
    print("\nCurrent Location:",room,"-",rooms[room])
    if len(objects[room]) > 0:
        print("Objects:")
        for object in objects[room]:
            if object not in hidden.values():
                print(object)
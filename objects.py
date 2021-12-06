#defines the objects that are present in each room.
objects={
    "Street":[],
    "Lobby":["WelcomeMat","KeyCard"],
    "Lift":[],
    "1st Floor":[]}

#defines objects that hide other objects and must be move to reveal them.
hidden={"WelcomeMat":"KeyCard"}

#creates an empty list to store the inventory.
inventory=[]
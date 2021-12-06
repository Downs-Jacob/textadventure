
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
from operators import *


def intro():
    cls()

    displayText("You need to create your character now! Please enter the name of your character:")
    characterSetup()
    


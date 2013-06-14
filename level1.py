import os
import time
import functions #

#Adds terminal color and style
from colorama import init
init(autoreset=True)
from colorama import Fore, Style

def loc3_1():

        print("You find yourself on the desktop of a virtual machine. The room is empty except for " +
              "a red light and the sound of a siren. You see some random " + Style.BRIGHT + "[pictures]" + Style.RESET_ALL + " scattered around " +
              "on the floor. There is a" + Style.BRIGHT + " [recycle bin] " + Style.RESET_ALL + "in the corner of the room. " +
              "You scan the area and find no immediate threats. The only possible exits are to the " + Style.BRIGHT + "[E]ast." + Style.RESET_ALL + "\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '4_1' # Go to 4,1

            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'PICTURES':
                    print("You attack the pictures and make an ever bigger mess!\n\r")
                elif perform[1] == 'RECYCLE':
                    print("You attack the recycle bin and it crashes against the wall.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the room and find  " + Style.BRIGHT + "[pictures]" + Style.RESET_ALL + " and a " + Style.BRIGHT + "[recycle bin]" + Style.RESET_ALL + " . Exits are  " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " .\n\r")
                elif perform[1] == 'PICTURES':
                    print("You scan the pictures. These are photos of someone's wedding.\n\r")
                elif perform[1] == 'RECYCLE':
                    print("You scan the recycle bin. It's empty.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None  #Clears the perform list before looping.

#4,1  ###################################################################################

def loc4_1():

        print("You enter an adjacent room. It looks like a control room of some sort. " +
              "There are various tools, gauges, monitors, and computers but they all appear to be broken. It looks like something big trampled through here. " +
              "There is a large " + Style.BRIGHT + "[safe]" + Style.RESET_ALL + " against the wall. The possible exits are " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " and " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " .\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '5_1' # Go to 5,1
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '3_1' # Go to 3,1
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'SAFE':
                    print("You attack the safe, but it is indestructible!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the room and find a " + Style.BRIGHT + "[safe]" + Style.RESET_ALL + " . Exits are " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " and " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " .\n\r")
                elif perform[1] == 'SAFE':
                    print("You check out the safe. It's unlocked and empty, except for a note that reads: 'cnffjbeq vf grfyn' It must be some kind of code.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#5,1  ##################################################################################

def loc5_1():

        print("You enter what looks like an arcade. There are many arcade " + Style.BRIGHT + "[games]" + Style.RESET_ALL + " and " + Style.BRIGHT + "[snack]" + Style.RESET_ALL + " machines. " +
              "On the East wall, you notice a large " + Style.BRIGHT + "[hole]" + Style.RESET_ALL + " to the outside. The possible exits are " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + " and  " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " .\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'E S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '5_2' # Go to 5,2
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '4_1' # Go to 4,1
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'GAMES':
                    print("You attack one of the games and break it. Why would you do that?\n\r")
                elif perform[1] == 'HOLE':
                    print("You reconsider attacking the hole as you may fall to your death!\n\r")
                elif perform[1] == 'SNACK':
                    print("DEHUNGERIZE! A Snickers bar falls to the dispenser.\n\r")          
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the room and find " + Style.BRIGHT + "[games]" + Style.RESET_ALL + ", " + Style.BRIGHT + "[snack]" + Style.RESET_ALL + " machines, and a " + Style.BRIGHT + "[hole]" + Style.RESET_ALL + " in the wall. Exits are " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + " and " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                elif perform[1] == 'GAMES':
                    import webbrowser
                    webbrowser.open('http://www.kongregate.com')
                elif perform[1] == 'SNACK':
                    print("There are various vending machines with tasty snacks. Unfortunately, you have no monies!\n\r")
                elif perform[1] == 'HOLE':
                    print("You investigate the hole. It is about 5 feet in diameter. It looks like the Kool-Aid guy smashed through here.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#5,2  ##################################################################################

def loc5_2():

        print("You enter a long empty hallway with various doors. You can enter the first room to the " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ", go " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ", or " +
              "proceed " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + " ,down the hallway.\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'E':
                print("You can't go that way!\n\r")
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '5_3' # Go to 5,3
            elif perform[0] == 'W':
                print("Entering the room...\n\r")
                time.sleep(0.5)
                return '4_2' # Go to 4,2
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '5_1' # Go to 5,1
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the hallway but don't see anything abnormal. Exits are " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ", " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ", and " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#4,2  ##################################################################################

def loc4_2():

        with open("player") as infile:  #Checks to see if the monster is already dead.
            for line in infile:
                if "4_2" in line:
                    virus4_2 = "DEAD"
                else:
                    virus4_2 = "ALIVE"

        if virus4_2 == "DEAD":
            print("You enter a large dark office. You see various spreadsheets and documents scattered everywhere. " +
              "There is a dead virus here. Exit is " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r\n\r")
        else:
            print("You enter a large dark office. You see various spreadsheets and documents scattered everywhere. " +
              "There is something in the SW " + Style.BRIGHT + "[corner]" + Style.RESET_ALL + " of the room. Exit is " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '5_2' # Go to 5,2
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'CORNER':
                    if virus4_2 == "DEAD":
                        print("There's nothing to attack over there.\n\r")
                    else:
                        print("You reconsider attacking blindly. You don't know what's over there!\n\r")
                elif perform[1] == 'VIRUS':
                    if virus4_2 == "DEAD":
                        print("You already decimated the virus!\n\r")
                    else:
                        print("You annihilate the virus with your " + Fore.RED + "HEURISTIC HAMMER OF RAGE!" + Fore.RESET +"\n\r")
                        virus4_2 = "DEAD"
                        file = open('player', 'a') #Tells our save file that the 4_2 monster has been killed.
                        file.write('4_2\n')
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the office. You see various spreadsheets and documents scattered everywhere. Exit is " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r")
                elif perform[1] == 'CORNER':
                    if virus4_2 == "DEAD":
                        print("There is a dead virus here!\n\r")
                    else:
                        print("You approach the corner. There is a slimy looking creature hunched over, facing the wall. This appears to be a " + Style.BRIGHT + "[virus]" + Style.RESET_ALL + "!\n\r")
                elif perform[1] == 'VIRUS':
                    if virus4_2 == "DEAD":
                        print("Yup, it's dead.\n\r")
                    else:
                        print("You approach the corner. There is a slimy looking creature hunched over, facing the wall. This appears to be a " + Style.BRIGHT + "[virus]" + Style.RESET_ALL + "!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#5,3  ##################################################################################

def loc5_3():

        print("You enter the hallway. You can enter a hallway to the " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " go " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ", or proceed " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ", down the current hallway.\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'E':
                print("You can't go that way!\n\r")
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '5_4' # Go to 5,4
            elif perform[0] == 'W':
                print("Entering the room...\n\r")
                time.sleep(0.5)
                return '4_3' # Go to 4,3
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '5_2' # Go to 5,2
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the hallway but don't see anything abnormal. Exits are " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + " , " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " , and " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#4,3  ##################################################################################

def loc4_3():

        print("You go down an adjacent hallway. The ceiling lights are flickering and there is a huge mess of papers and broken furniture. " +
              "You see a dead " + Style.BRIGHT + "[body]" + Style.RESET_ALL + " stuck under a tipped desk. You can go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " to the main hallway or go " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " down the current hallway.\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '3_3' # Go to 3,3
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '5_3' # Go to 5,3
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'BODY':
                    print("You attack the body. It becomes more mangled. You are a sick and twisted person!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("The ceiling lights are flickering and there is a huge mess of papers and broken furniture. " +
              "You see a dead " + Style.BRIGHT + "[body]" + Style.RESET_ALL + " stuck under a tipped desk. You can go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " to the main hallway or go " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " down the current hallway.\n\r\n\r")
                elif perform[1] == 'BODY':
                    print("You scan the body. It is mangled and covered in slime.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#3,3  ##################################################################################

def loc3_3():

        print("You walk in to a small break room. There are a couple of tables and a kitchenette. There is a restroom to the " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ". " +
              "There is a trail of slime leading to the restroom door. You may also go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '4_3' # Go to 4,3
            elif perform[0] == 'S':
                print("Entering the restroom...\n\r")
                time.sleep(0.5)
                return '3_2' # Go to 3,2
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("There are a couple of tables and a kitchenette. There is a restroom to the " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " and a hallway to the " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " . \n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#3,2  ##################################################################################

def loc3_2():

        with open("player") as infile:  #Checks to see if the monster is already dead.
            for line in infile:
                if "3_2" in line:
                    virus3_2 = "DEAD"
                else:
                    virus3_2 = "ALIVE"

        if virus3_2 == "DEAD":
            print("You enter the restroom. There is a dead virus in here. You can go " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")
        else:
            print("You enter the restroom. There is toilet " + Style.BRIGHT + "[paper]" + Style.RESET_ALL + " stuck to your shoe. The trail of slime leads to a toilet " + Style.BRIGHT + "[stall]" + Style.RESET_ALL + ". You can only go [N]orth.\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'W E S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'N':
                print("Leaving restroom...\n\r")
                time.sleep(0.5)
                return '3_3' # Go to 3,3
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'STALL':
                    print("You attack the stall and create a dent.\n\r")
                elif perform[1] == 'PAPER':
                    print("You give a feeble attempt to attack the toilet paper, but it is indestructible!\n\r")
                elif perform[1] == 'VIRUS':
                    if virus3_2 == "DEAD":
                        print("You already killed the virus.")
                    else:
                        print("You crush the virus' skull with your " + Fore.RED + "HEURISTIC HAMMER OF RAGE!" + Fore.RESET + " Its head falls in to the toilet.\n\r")
                        virus3_2 = "DEAD"
                        file = open('player', 'a') #Tells our save file that the 3_2 monster has been killed.
                        file.write('3_2\n')
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    if virus3_2 == "DEAD":
                        print("You scan the room. There is a dead virus in here. You can go " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r")               
                    else:
                        print("You scan the room. There is toilet " + Style.BRIGHT + "[paper]" + Style.RESET_ALL + " stuck to your shoe. The trail of slime leads to a toilet " + Style.BRIGHT + "[stall]" + Style.RESET_ALL + ". You can only go " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r")
                elif perform[1] == 'STALL':
                    if virus3_2 == "DEAD":
                        print("You examine the stall. It's very dented. There is a dead virus here.\n\r")
                    else:
                        print("You examine the stall. It's very dented. There is a slimy creature hunched over the toilet. It looks like a " + Style.BRIGHT + "[virus]" + Style.RESET_ALL + ".\n\r")
                elif perform[1] == 'VIRUS':
                    if virus3_2 == "DEAD":
                        print("Yup, it's dead.\n\r")
                    else:
                        print("There is a slimy creature hunched over the toilet.\n\r")
                elif perform[1] == 'PAPER':
                        print("Gross!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#5,4  ##################################################################################

def loc5_4():

        print("You enter a section of the hallway. There is an office area to the " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ". You can also go " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ", or proceed " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + " , down the current hallway.\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'E':
                print("You can't go that way!\n\r")
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '5_5' # Go to 5,5
            elif perform[0] == 'W':
                print("Entering the room...\n\r")
                time.sleep(0.5)
                return '4_4' # Go to 4,4
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '5_3' # Go to 5,3
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You scan the hallway but don't see anything abnormal. Exits are " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ", " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ", and " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#4,4  ##################################################################################

def loc4_4():

        print("You enter an adjacent office area. You see a reception " + Style.BRIGHT + "[desk]" + Style.RESET_ALL + " in front of another room. You may go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " or enter the room to the " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'W':
                print("Entering the West room...\n\r")
                time.sleep(0.5)
                return '3_4' # Go to 3,4
            elif perform[0] == 'E':
                print("Going back to hallway...\n\r")
                time.sleep(0.5)
                return '5_4' # Go to 5,4
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'DESK':
                    print("You attack the desk. You manage to leave a scratch, but that is all.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You see a reception " + Style.BRIGHT + "[desk]" + Style.RESET_ALL + " in front of another room. You may go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " or enter the room to the " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                elif perform[1] == 'DESK':
                    print("You scan the desk. There is a computer on the desk. It looks like someone left an " + Style.BRIGHT + "[email]" + Style.RESET_ALL + " open.\n\r")
                elif perform[1] == 'EMAIL':
                    print("You read the " + Style.BRIGHT + "[email]" + Style.RESET_ALL + ". It appears to be from a Nigerian gentleman thanking the recipient for a generous donation.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#3,4  ##################################################################################

def loc3_4():

        print("You enter the room. It looks like a records room. There are piles of papers and files everywhere. You see a " + Style.BRIGHT + "[whiteboard]" + Style.RESET_ALL + ". Exit is  " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going back to the office...\n\r")
                time.sleep(0.5)
                return '4_4' # Go to 5,4
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'WHITEBOARD':
                    print("You attack the whiteboard, but nothing happens.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You enter the room. It looks like a records room. There are piles of papers and files everywhere. You see a " + Style.BRIGHT + "[whiteboard]" + Style.RESET_ALL + ". Exit is [E]ast.\n\r")
                elif perform[1] == 'WHITEBOARD':
                    print("You examine the whiteboard. You see '68616c66776179207468657265' written in black marker.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#5,5  ##################################################################################

def loc5_5():

        print("You enter a corner hallway. You may go " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " or continue " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " to a new hallway.\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N E':
                print("You can't go that way!\n\r")
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '4_5' # Go to 5,4
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '5_4' # Go to 4,5
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You may go " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " or " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#4,5  ##################################################################################

def loc4_5():

        with open("player") as infile:  #Checks to see if the monster is already dead.
            for line in infile:
                if "4_5" in line:
                    virus4_5 = "DEAD"
                else:
                    virus4_5 = "ALIVE"

        if virus4_5 == "DEAD":
            print("You enter a hallway. There is a dead virus here. You can go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " or " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + ".\n\r\n\r")               
        else:
            print("You enter a hallway and a " + Style.BRIGHT + "[virus]" + Style.RESET_ALL + " monster swings his slime fist at you. You block the attack with your " + Fore.RED + "FIREWALL SHIELD OF THREAT PROTECTION!" + Fore.RESET + " You should retaliate! \n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S':
                 print("You can't go that way!\n\r")
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '3_5' # Go to 3,5
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '5_5' # Go to 5,5
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'VIRUS':
                    if virus4_5 == "DEAD":
                        print("There is not much left of the virus.\n\r\n\r")
                    else:
                        print("You counter the attack with a spinning swing of your " + Fore.RED + "HEURISTIC HAMMER OF RAGE" + Fore.RESET + ", obliterating the virus in to numerous giblets!\n\r")
                        virus4_5 = "DEAD"
                        file = open('player', 'a') #Tells our save file that the 4_5 monster has been killed.
                        file.write('4_5\n')
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You may go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " or " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + " .\n\r")
                elif perform[1] == 'VIRUS':
                    if virus4_5 == "DEAD":
                        print("There is not much left of the virus.\n\r")
                    else:
                        print("It is an angry virus monster, do something!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#3,5  ##################################################################################

def loc3_5():

        print("You enter the middle section of the hallway. Part of the ceiling has fallen and there's a tendril of " + Style.BRIGHT + "[slime]" + Style.RESET_ALL + " hanging from the ceiling. Go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " or " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + "?  \n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '4_5' # Go to 4,5
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '2_5' # Go to 2,5
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'SLIME':
                    print("You attack the slime and get it all over your clothes!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You may go " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " or " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                elif perform[1] == 'SLIME':
                    print("You taste the slime and it tastes like virus.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#2,5  ##################################################################################

def loc2_5():

        print("You enter another section of the hallway. There is a small janitorial room to the south. Go " + Style.BRIGHT + "[E]ast, [S]outh " + Style.RESET_ALL + " or " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + "?  \n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '3_5' # Go to 3,5
            elif perform[0] == 'W':
                print("Going West...\n\r")
                time.sleep(0.5)
                return '1_5' # Go to 1,5
            elif perform[0] == 'S':
                print("Entering the room...\n\r")
                time.sleep(0.5)
                return '2_4' # Go to 2,4
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You may go " + Style.BRIGHT + "[E]ast, [S]outh" + Style.RESET_ALL + " or " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#2,4  ##################################################################################

def loc2_4():

        print("You enter the janitorial room. Just as you expected, it's full of cleaners and tools. There's doesn't appear to be anything abnormal here." + Style.BRIGHT + "[N]orth!" + Style.RESET_ALL + "\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'S E W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'N':
                print("Leaving room...\n\r")
                time.sleep(0.5)
                return '2_5' # Go to 2,5
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("There's doesn't appear to be anything abnormal here. Just go " + Style.BRIGHT + "[N]orth!" + Style.RESET_ALL + "\n\r\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#1,5  ##################################################################################

def loc1_5():

        print("You enter another corner hallway. You can hear a faint humming sound coming from the end of the adjacent hallway. You can proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + "or go back " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '1_4' # Go to 1,4
            elif perform[0] == 'E':
                print("Going East...\n\r")
                time.sleep(0.5)
                return '2_4' # Go to 2,4
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You can hear a faint humming sound coming from the end of the adjacent hallway. You can proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " or go back " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + ".\n\r\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#1,4  ##################################################################################

def loc1_4():

        print("You're still in the hallway and can hear a humming sound coming from the end of the current. You can proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + "or go back " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'E W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '1_3' # Go to 1,3
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '1_5' # Go to 1,5
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You're still in the hallway and can hear a humming sound coming from the end of the current. You can proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + "or go back " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#1,3  ##################################################################################

def loc1_3():

        print("You're in the middle of the hallway. To the " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " you see a room with a sign that says 'Logging Room' above the door. You can also proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " or go back " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '1_2' # Go to 1,2
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '1_4' # Go to 1,4
            elif perform[0] == 'E':
                print("Entering the logging room...\n\r")
                time.sleep(0.5)
                return '2_3' # Go to 2,3
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You're in the middle of the hallway. To the " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " you see a room with a sign that says 'Logging Room' above the door. You can also proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + "or go back " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#2,3  ##################################################################################

def loc2_3():

        with open("player") as infile:  #Checks to see if the monster is already dead.
            for line in infile:
                if "2_3" in line:
                    virus2_3 = "DEAD"
                else:
                    virus2_3 = "ALIVE"

        if virus2_3 == "DEAD":
            print("You enter the logging room. There is a dead virus in here. There is also a large " + Style.BRIGHT + "[monitor]" + Style.RESET_ALL +  " on the wall. You can only go " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r\n\r")
        else:
            print("You enter the logging room. A furious " + Style.BRIGHT + "[virus]" + Style.RESET_ALL + " monster lunges at you!. You catch a glimpse at a large computer " + Style.BRIGHT + "[monitor]" + Style.RESET_ALL +  " on the wall, but you are too busy trying not to die! You can only go " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'N E S':
                print("You can't go that way!\n\r")
            elif perform[0] == 'W':
                print("Leaving room...\n\r")
                time.sleep(0.5)
                return '1_3' # Go to 1,3
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'VIRUS':
                    if virus2_3 == "DEAD":
                        print("The virus has de-pressurized!")
                    else:
                        print("You stuff your " + Fore.RED + "HEURISTIC HAMMER OF RAGE" + Fore.RESET + " down the throat of the virus. The virus glows red and explodes!\n\r")
                        virus2_3 = "DEAD"
                        file = open('player', 'a') #Tells our save file that the 2_3 monster has been killed.
                        file.write('2_3\n')
                elif perform[1] == 'MONITOR':
                    print("You try to attack the monitor but nothing happens. It appears to be behind some very thick glass.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    if virus2_3 == "DEAD":
                        print("You enter the logging room. There is a dead virus in here. There is also a large " + Style.BRIGHT + "[monitor]" + Style.RESET_ALL +  " on the wall. You can only go " + Style.BRIGHT + "[W]est" + Style.RESET_ALL + ".\n\r\n\r")
                    else:
                        print("You are in the logging room. A furious " + Style.BRIGHT + "[virus]" + Style.RESET_ALL + " monster is trying to kill you!. You catch a glimpse at a large computer " + Style.BRIGHT + "[monitor]" + Style.RESET_ALL +  " on the wall, but you are too busy trying not to die! Attack the bloody thing!\n\r\n\r")
                elif perform[1] == 'VIRUS':
                    if virus2_3 == "DEAD":
                        print("The virus has de-pressurized!\n\r")
                    else:
                        print("The virus is trying to kill you! Attack the bloody thing!\n\r")
                elif perform[1] == 'MONITOR':
                    if virus2_3 == "DEAD":
                        print("The monitor appears to be logging access attempts to some kind of computer or door. You see 'Access Denied' hundreds of times on the screen.\n\r")
                    else:
                        print("The virus is trying to kill you! You are too busy to read the monitor!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#1,2  ##################################################################################

def loc1_2():

        print("You stand in the hallway. There are elevators to the east, but they look demolished. There's no way you will be able to get in those. There is a " + Style.BRIGHT + "[tape]" + Style.RESET_ALL + " recorder on the ground, covered in slime. You can proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + " or go back " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'E W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'S':
                print("Going South...\n\r")
                time.sleep(0.5)
                return '1_1' # Go to 1,1
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '1_3' # Go to 1,3
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                elif perform[1] == 'TAPE':
                    print("Really? OK fine, you try to attack the tape recorder but it's made of lava and dragons, so nothing happens.\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("You stand in the hallway. There is a " + Style.BRIGHT + "[tape]" + Style.BRIGHT + " recorder on the ground, covered in slime. You can proceed " + Style.BRIGHT + "[S]outh" + Style.RESET_ALL + "or go back " + Style.BRIGHT + "[N]orth" + Style.RESET_ALL + ".\n\r\n\r")
                elif perform[1] == 'TAPE':
                    print("You listen to the tape to hear a distressed voice: 'They've overtook the east half and the Ghosts are quarantining us. We're going to try and take shelter in-'\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.

#1,1  ##################################################################################

def loc1_1():

        print("You reach the end of the hallway. There is a door leading to the " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " with a sign that says: 'PORT 80'. The door is secured and there is a keypad next to the door. I hope you have the code! You can always go back though...\n\r\n\r")

        while 1:
            perform = input(">> ")
            perform = perform.upper()
            perform = perform.split()
            
            #Check input for a valid command. Loop until valid.
            while functions.inputError(perform[0]):
                perform = input(">> ")
                perform = perform.upper()
                perform = perform.split()

            #Perform command
            if perform[0] in 'S W':
                print("You can't go that way!\n\r")
            elif perform[0] == 'E':
                print("You try to access the door...\n\r") #START EXIT CHECK
                time.sleep(0.5)
                exitcode = input("ENTER ACCESS CODE:")
                if exitcode.upper() == 'TESLA':
                    KILLCOUNT = 0
                    with open("player") as infile:  #Makes sure all monsters have been killed.
                        for line in infile:
                            if "4_2" in line:
                                KILLCOUNT += 1
                            if "3_2" in line:
                                KILLCOUNT += 1
                            if "4_5" in line:
                                KILLCOUNT += 1
                            if "2_3" in line:
                                KILLCOUNT += 1
                    if KILLCOUNT == 4:
                        print("\n\rACCESS GRANTED \n\r\n\r -- The door slides open and you step through. Congratulations! You have completed Level 1!\n\r")
                        time.sleep(30) #END OF LEVEL
                        return 'DONE'
                    else:
                        print("\n\rACCESS GRANTED \n\r\n\r -- You cannot leave until the area is secure. There are still viruses that need to be 'cleansed.'")

                else:
                    print("ACCESS DENIED \n\r")
            elif perform[0] == 'N':
                print("Going North...\n\r")
                time.sleep(0.5)
                return '1_3' # Go to 1,2
            elif perform[0] == 'ATTACK':
                if len(perform) == 1:
                    print("You attack nothing. Good job Einstein!\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            elif perform[0] == 'SCAN':
                if len(perform) == 1:
                    print("There is a door leading to the " + Style.BRIGHT + "[E]ast" + Style.RESET_ALL + " with a sign that says: 'PORT 80'. The door is secured and there is a keypad next to the door. I hope you have the code! You can always go back and look for the code...\n\r\n\r")
                else:
                    print("I don't understand " + perform[1] + ".\n\r")
            if len(perform) > 1: perform = None #Clears the perform list before looping.
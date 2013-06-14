import os
import time

# Created player profile to player.ini
def newPlayer():
    print("System>: Loading Spawning Module...")
    time.sleep(1)
    print("System>: Spawning Unit - Virus Fighter")
    time.sleep(1)
    playerName = input("System>: Please name the fighter: ")
    print("System>: Unit.Rename('Subject41877','" + playerName + "')")
    time.sleep(1)
    print("System>: Operation Completed... Welcome " + playerName + ".\n\r")

    print(".")    #Pointless animated loading dots.
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".\n\r")
    time.sleep(0.5)
    
    with open('player', 'w') as file:
          file.writelines(playerName + '\n')
    file.close()
    time.sleep(1)
    return newPlayer


#Returns true if the command is not valid.
def inputError(perform):
    if perform not in 'N S E W ATTACK SCAN':
        print("I'm sorry, that is not a valid command.\r\n" +
              "Use on of the following: N, S, E, W, ATTACK, SCAN\r\n")
        return 1
    else: return 0

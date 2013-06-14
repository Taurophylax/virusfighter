import fileinput
import os
import time
import functions #
import level1 #

functions.newPlayer()

print("System>: Our network is under attack. You have spawned on VM3_Win7 to clean up the threats. " +
      "Please secure the area and proceed to Port 80 for further instructions.\n\r\n\r Possible commands are N, S, E, W, ATTACK, and SCAN")

print(".")    #More pointless animated loading dots.
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".\n\r")
time.sleep(0.5)

status = level1.loc3_1()
#Start in room 3,1
#status = return value = next room

while 1:

    if status == '3_1':
        status = level1.loc3_1()
    elif status == '4_1':
        status = level1.loc4_1()
    elif status == '5_1':
        status = level1.loc5_1()
    elif status == '5_2':
        status = level1.loc5_2()
    elif status == '4_2':
        status = level1.loc4_2()
    elif status == '5_3':
        status = level1.loc5_3()
    elif status == '4_3':
        status = level1.loc4_3()
    elif status == '3_3':
        status = level1.loc3_3()
    elif status == '3_2':
        status = level1.loc3_2()
    elif status == '5_4':
        status = level1.loc5_4()
    elif status == '4_4':
        status = level1.loc4_4()
    elif status == '3_4':
        status = level1.loc3_4()
    elif status == '5_5':
        status = level1.loc5_5()
    elif status == '4_5':
        status = level1.loc4_5()
    elif status == '3_5':
        status = level1.loc3_5()
    elif status == '2_5':
        status = level1.loc2_5()
    elif status == '2_4':
        status = level1.loc2_4()
    elif status == '1_5':
        status = level1.loc1_5()
    elif status == '1_4':
        status = level1.loc1_4()
    elif status == '1_3':
        status = level1.loc1_3()
    elif status == '2_3':
        status = level1.loc2_3()
    elif status == '1_2':
        status = level1.loc1_2()
    elif status == '1_1':
        status = level1.loc1_1()
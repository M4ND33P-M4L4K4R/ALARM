#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import datetime
import time 

#start coding
os.system("clear")
os.system("rm alarm.py")
os.system("clear")

#Design 
print("\033[0m")
print("\033[31m")

print("""
 █████╗ ██╗      █████╗ ██████╗ ███╗   ███╗
██╔══██╗██║     ██╔══██╗██╔══██╗████╗ ████║
███████║██║     ███████║██████╔╝██╔████╔██║
██╔══██║██║     ██╔══██║██╔══██╗██║╚██╔╝██║
██║  ██║███████╗██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                      \033[4m\033[38;5;209mVersion 2.1
""")

print("\033[93m""======================================")
print("\033[37m"" [> CODED BY M4ND33P <]")
print("\033[31m""======================================")
#variable
print("\033[32m")

timer = int(input("\033[4m""[> SET YOUR ALARM <] : \033[38;5;209m"))
print("\033[93m")
print("\033[4m")
print("[#] PRESS 1 TO SET YOUR ALARM IN HOUR ")
print("[#] PRESS 2 TO SET YOUR ALARM IN MINUTE ")
print("[#] PRESS 3 TO SET YOUR ALARM IN SECOND")
print("[#] PRESS 4 ABOUT")
print("[#] PRESS 5 TO EXIT")
print()
print("\033[32m")
print("\033[4m")

option = int(input("\033[4m""ENTER YOUR CHOICE : \033[38;5;229m"))

while True:
    if option == 1:
        Alarm = 3600*timer
        print("\033[34m""Your ALARM will be ring after",timer,"Hour")
        time.sleep(Alarm)
        print("\033[36m""Your Alarm has been Activate Sir")
        os.system("mpv alarm.mp3")
    elif option == 2:
        Alarm = 60*timer
        print("\033[31m""Your ALARM will be ring after",timer,"Minutes")
        time.sleep(Alarm)
        print("\033[36m""Your Alarm has been Activate Sir")
        os.system("mpv alarm.mp3")
    elif option == 3:
        Alarm = timer
        print("\033[31m""Your ALARM will be ring after",timer,"Second")
        time.sleep(Alarm)
        print("\033[36m" "Your Alarm has been Activate Sir")
        os.system("mpv alarm.mp3")
    elif option == 5:
        
        print("\033[35m""YOU HAVE BEEN EXIT SIR !!")
    elif option == 4:
        while True:
            print("\033[38;5;129mHello Guys Myself is \033[38;5;48mMandeep Malakar Welcome\n -[\033[93mYou can Modify my script But give \033[38;5;245mCredit")
            break
        

    else:
        while True:
            print("\033[93m""Sorry Sir Invalid option\033[0m")
            break







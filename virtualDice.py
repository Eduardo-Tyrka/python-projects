# virtual dice

import random

programWorking = True
firstRun = True

while programWorking:

    print("welcome to the virtual dice")
    print("wich dice would you like to use?")
    print("options: (4) (6) (8) (10) (12) (20)")
    userSelect = int(input())
    rollingTheDice = True

    
    if userSelect == 4:
        while rollingTheDice:
            print("your number is: ", random.randint(1, 4))
            print("would you like to roll the same dice again? (s/n)")
            sameDice = input()
            if sameDice == "s":
                rollingTheDice = True
            elif sameDice == "n":
                rollingTheDice = False
            else:
                print("select a valid answer")
    elif userSelect == 6:
        while rollingTheDice:
            print("your number is: ", random.randint(1, 6))
            print("would you like to roll the same dice again? (s/n)")
            sameDice = input()
            if sameDice == "s":
                rollingTheDice = True
            elif sameDice == "n":
                rollingTheDice = False
            else:
                print("select a valid answer")
    elif userSelect == 8:
        while rollingTheDice:
            print("your number is: ", random.randint(1, 8))
            print("would you like to roll the same dice again? (s/n)")
            sameDice = input()
            if sameDice == "s":
                rollingTheDice = True
            elif sameDice == "n":
                rollingTheDice = False
            else:
                print("select a valid answer")
    elif userSelect == 10:
        while rollingTheDice:
            print("your number is: ", random.randint(1, 10))
            print("would you like to roll the same dice again? (s/n)")
            sameDice = input()
            if sameDice == "s":
                rollingTheDice = True
            elif sameDice == "n":
                rollingTheDice = False
            else:
                print("select a valid answer")
    elif userSelect == 12:
        while rollingTheDice:
            print("your number is: ", random.randint(1, 12))
            print("would you like to roll the same dice again? (s/n)")
            sameDice = input()
            if sameDice == "s":
                rollingTheDice = True
            elif sameDice == "n":
                rollingTheDice = False
            else:
                print("select a valid answer")
    elif userSelect == 20:
        while rollingTheDice:
            print("your number is: ", random.randint(1, 20))
            print("would you like to roll the same dice again? (s/n)")
            sameDice = input()
            if sameDice == "s":
                rollingTheDice = True
            elif sameDice == "n":
                rollingTheDice = False
            else:
                print("select a valid answer")
    else:
        print("select a valid answer")

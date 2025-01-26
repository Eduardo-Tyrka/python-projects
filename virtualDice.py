# virtual dice

import random

programWorking = True
firstRun = True

while programWorking:
    if firstRun:
        print("welcome to the virtual dice")
        print("wich dice would you like to use?")
    firstRun = False

    print("options: (4) (6) (8) (10) (12) (20)")
    userSelect = input()

    validAnswersStr = ["4", "6", "8", "10", "12", "20"]
    if userSelect in validAnswersStr:
        userSelect = int(userSelect)

    rollingTheDice = True

    validAnswersInt = [4, 6, 8, 10, 12, 20]

    if userSelect in validAnswersInt:
        if userSelect == 4:
            while rollingTheDice:
                print("your number is: ", random.randint(1, 4))
                print("would you like to roll the same dice again? (s/n)")
                answeredWrong = True
                while answeredWrong:
                    sameDice = input()
                    if sameDice == "s":
                        rollingTheDice = True
                        answeredWrong = False
                    elif sameDice == "n":
                        rollingTheDice = False
                        answeredWrong = False
                        firstRun = True
                    else:
                        print("select a valid answer")
        if userSelect == 6:
            while rollingTheDice:
                print("your number is: ", random.randint(1, 6))
                print("would you like to roll the same dice again? (s/n)")
                answeredWrong = True
                while answeredWrong:
                    sameDice = input()
                    if sameDice == "s":
                        rollingTheDice = True
                        answeredWrong = False
                    elif sameDice == "n":
                        rollingTheDice = False
                        answeredWrong = False
                        firstRun = True
                    else:
                        print("select a valid answer")
        if userSelect == 8:
            while rollingTheDice:
                print("your number is: ", random.randint(1, 8))
                print("would you like to roll the same dice again? (s/n)")
                answeredWrong = True
                while answeredWrong:
                    sameDice = input()
                    if sameDice == "s":
                        rollingTheDice = True
                        answeredWrong = False
                    elif sameDice == "n":
                        rollingTheDice = False
                        answeredWrong = False
                        firstRun = True
                    else:
                        print("select a valid answer")
        if userSelect == 10:
            while rollingTheDice:
                print("your number is: ", random.randint(1, 10))
                print("would you like to roll the same dice again? (s/n)")
                answeredWrong = True
                while answeredWrong:
                    sameDice = input()
                    if sameDice == "s":
                        rollingTheDice = True
                        answeredWrong = False
                    elif sameDice == "n":
                        rollingTheDice = False
                        answeredWrong = False
                        firstRun = True
                    else:
                        print("select a valid answer")
        if userSelect == 12:
            while rollingTheDice:
                print("your number is: ", random.randint(1, 12))
                print("would you like to roll the same dice again? (s/n)")
                answeredWrong = True
                while answeredWrong:
                    sameDice = input()
                    if sameDice == "s":
                        rollingTheDice = True
                        answeredWrong = False
                    elif sameDice == "n":
                        rollingTheDice = False
                        answeredWrong = False
                        firstRun = True
                    else:
                        print("select a valid answer")
        if userSelect == 20:
            while rollingTheDice:
                print("your number is: ", random.randint(1, 20))
                print("would you like to roll the same dice again? (s/n)")
                answeredWrong = True
                while answeredWrong:
                    sameDice = input()
                    if sameDice == "s":
                        rollingTheDice = True
                        answeredWrong = False
                    elif sameDice == "n":
                        rollingTheDice = False
                        answeredWrong = False
                        firstRun = True
                    else:
                        print("select a valid answer")

        wantAgainAnswer = True
        while wantAgainAnswer:
            print("would you like to select a new dice? (s/n)")
            tryAgain = input()
            if tryAgain == "s":
                programWorking = True
                wantAgainAnswer = False
            elif tryAgain == "n":
                programWorking = False
                wantAgainAnswer = False
            else:
                print("select a valid answer")

    else:
        print("select a valid answer")

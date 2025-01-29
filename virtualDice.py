# virtual dice 2.0
# used functions instead of doing the same thing changing just the numbers

import random

programWorking = True
firstRun = True

def rollTheDice(userSelect):
    rollingTheDice = True
    while rollingTheDice:
        print("your number is: ", random.randint(1, userSelect))
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

while programWorking:
    if firstRun:
        print("welcome to the virtual dice")
        print("wich dice would you like to use?")
        firstRun = False

    print("options: (4) (6) (8) (10) (12) (20)")
    userSelect = input()

    validAnswers = ["4", "6", "8", "10", "12", "20"]
    answerWrong = True
    while answerWrong:
        if userSelect in validAnswers:
            userSelect = int(userSelect)
            answerWrong = False
        else:
            print("select a valid answer")
            userSelect = input()

    rollTheDice(userSelect)

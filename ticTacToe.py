# Tic Tac Toe game

# the number of lines and columns
spaces = {
    "11": "-",
    "12": "-",
    "13": "-",
    "21": "-",
    "22": "-",
    "23": "-",
    "31": "-",
    "32": "-",
    "33": "-"
}


print("welcome to the tic tac toe game!")
print(spaces.get("11"), spaces.get("12"), spaces.get("13"))
print(spaces.get("21"), spaces.get("22"), spaces.get("23"))
print(spaces.get("31"), spaces.get("32"), spaces.get("33"))

programWorking = True

player1turn = True
player2turn = False

while programWorking:

    while player2turn:

        print("player 2 turn ( O )")
        print("where do you want to place? select the number of the line and of the column exemple: ( 23 )")

        player2select = input()
        avaliableSpace = spaces.get(player2select)

        if avaliableSpace == "-":
            spaces.update({player2select: "O"})
            player2turn = False
            player1turn = True
        else:
            print("this place is already taken")

        print(spaces.get("11"), spaces.get("12"), spaces.get("13"))
        print(spaces.get("21"), spaces.get("22"), spaces.get("23"))
        print(spaces.get("31"), spaces.get("32"), spaces.get("33"))

    while player1turn:
        print("player 1 turn ( X )")
        print("where do you want to place? select the number of the line and of the column exemple: ( 23 )")

        player1select = input()
        avaliableSpace = spaces.get(player1select)

        if avaliableSpace == "-":
            spaces.update({player1select: "X"})
            player1turn = False
            player2turn = True
        else:
            print("this place is already taken")

        print(spaces.get("11"), spaces.get("12"), spaces.get("13"))
        print(spaces.get("21"), spaces.get("22"), spaces.get("23"))
        print(spaces.get("31"), spaces.get("32"), spaces.get("33"))

    if "-" not in spaces.values():
        print("end game")
        programWorking = False

    # win conditions
    
    if spaces.get("11") == spaces.get("12") == spaces.get("13") and spaces.get("11") != "-":
        if spaces.get("11") == "X":
            winner = "player 1"
        elif spaces.get("11") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("21") == spaces.get("22") == spaces.get("23") and spaces.get("21") != "-":
        if spaces.get("21") == "X":
            winner = "player 1"
        elif spaces.get("21") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("31") == spaces.get("32") == spaces.get("33") and spaces.get("31") != "-":
        if spaces.get("31") == "X":
            winner = "player 1"
        elif spaces.get("31") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("11") == spaces.get("21") == spaces.get("31") and spaces.get("11") != "-":
        if spaces.get("11") == "X":
            winner = "player 1"
        elif spaces.get("11") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("12") == spaces.get("22") == spaces.get("32") and spaces.get("12") != "-":
        if spaces.get("12") == "X":
            winner = "player 1"
        elif spaces.get("12") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("13") == spaces.get("23") == spaces.get("33") and spaces.get("13") != "-":
        if spaces.get("13") == "X":
            winner = "player 1"
        elif spaces.get("13") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("11") == spaces.get("22") == spaces.get("33") and spaces.get("11") != "-":
        if spaces.get("11") == "X":
            winner = "player 1"
        elif spaces.get("11") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    if spaces.get("13") == spaces.get("22") == spaces.get("31") and spaces.get("13") != "-":
        if spaces.get("13") == "X":
            winner = "player 1"
        elif spaces.get("13") == "O":
            winner = "player 2"
        print("end game!")
        print("the winner is:", winner)
        programWorking = False
    

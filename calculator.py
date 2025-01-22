# calculator

done = 0

while done == 0:
    # numbers 
    print("choose a number")
    first_number = int(input())
    print("choose other number")
    second_number = int(input())

    # operation
    print("choose the operation")
    print("valid operations: addicion( + ) subtraction( - ) multiplication( * ) division( / )")
    operation = input()

    # calculate
    completed = 0
    while completed == 0:
        if operation == "+":
            result = first_number + second_number
            completed = 1
        elif operation == "-":
            result = first_number - second_number
            completed = 1
        elif operation == "*":
            result = first_number * second_number
            completed = 1
        elif operation == "/":
            result = first_number / second_number
            completed = 1
        else:
            print("enter a valid operation")
            operation = input()
    print("result:")
    print(result)

    # ask if the user want to do it again
    print("want to calculate again?")
    print("type: ( yes ) or ( no )")
    doItAgain = input()
    if doItAgain == "yes":
        done = 0
    elif doItAgain == "no":
        done = 1
    else:
        print("enter a valid answer (no capital letters)")

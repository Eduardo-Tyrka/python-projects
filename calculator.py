# calculator

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

#tasktracker

tasks = []

programWorking = True
firstRun = True
while programWorking:

    if firstRun:
        print("welcome to the task manager! what do you want to do first?")
        firstRun = False
    else:
        print("what do you want to do now?")

    print("add a new task (type 1)")
    print("delete a task (select 2)")
    print("see your tasks (type 3)")
    print("close program (type 4)")

    userSelect = int(input())

    if userSelect == 1:
        print("select the name of the task")
        tasks.append(input())
        print("task added!")
    elif userSelect == 2:
        if len(tasks) == 0:
            print("you dont have any task")
        else:
            print("wich task would you want ro delete? (select the number of the task)")
            print(tasks)
            removedTask = int(input())
            removedTask = removedTask - 1
            tasks.pop(removedTask)
            print("task deleted!")
    elif userSelect == 3:
        if len(tasks) == 0:
            print("you dont have any tasks")
        else:
            print("your tasks:")
            print(tasks)
    elif userSelect == 4:
        print("are you sure? your tasks wont be saved, type (yes) or (no)")
        sureWantToLeave = input()
        if sureWantToLeave == "yes":
            programWorking = False
    else:
        print("select a valid comand")

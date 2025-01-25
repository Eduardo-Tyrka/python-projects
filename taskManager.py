# tasktracker 2.0

tasks = {}

programWorking = True
firstRun = True
while programWorking:
    if firstRun:
            print("welcome to the task manager! what do you want to do first?")
            firstRun = False
    else:
        print("what do you want to do now?")

    print("add a new task (type 1)")
    print("delete a task (type 2)")
    print("see your tasks (type 3)")
    print("update a task status (type 4)")
    print("close program (type 5)")

    userSelect = int(input())

    if userSelect == 1:
        print("select the name of the task")
        newTasksName = input()
        print("select the status of the task")
        newTasksStatus = input()
        tasks[newTasksName] = newTasksStatus
        print("task added!")
    elif userSelect == 2:
        if len(tasks) == 0:
            print("you dont have any task")
        else:
            print("wich task would you want ro delete?")
            print(tasks)
            removedTask = input()
            tasks.pop(removedTask)
            print("task deleted!")
    elif userSelect == 3:
        if len(tasks) == 0:
            print("you dont have any tasks")
        else:
            print("your tasks:")
            print(tasks)
    elif userSelect == 4:
        if len(tasks) == 0:
            print("you dont have any tasks")
        else:
            print("wich task would you want to update?")
            print(tasks)
            updatedTask = input()
            print("select the new status of the task")
            newStatus = input()
            tasks.update({updatedTask: newStatus})
            print("task updated")
    elif userSelect == 5:
        print("are you sure? your tasks wont be saved, type (yes) or (no)")
        sureWantToLeave = input()
        if sureWantToLeave == "yes":
            programWorking = False
    else:
        print("select a valid comand")

monday = {}
tuesday = {}
wednesday = {}
thursday = {}
friday = {}

WeekDays = [monday, tuesday, wednesday, thursday, friday]

print("bem vindo ao gerenciador de horarios de aula")
print("vamos criar o seu horario")

setting = True
firstDay = True
settingDay = 0

while setting:

    daySet = True
    firstClass = True
    classCheck = True
    if settingDay < 6:
        dayBeingSetted = WeekDays[settingDay]
    firstAtTheDay = True
    while daySet:
        
        if classCheck and firstAtTheDay:
            if firstDay:
                print("vamos começar por segunda")
            else:
                print("muito bem, agora o proximo dia")

        if classCheck:
            if firstClass:
                print("qual é sua primeira aula?")
            else:
                print("muito bem, qual é a proxima aula?")
        classInput = input()

        if classInput not in dayBeingSetted:
            classCheck = True
        else:
            print("você já colocou essa aula")
            print("selecione a aula novamente")
            classCheck = False
            firstAtTheDay = False

        if classCheck:
            print("essa aula é com qual professor?")
            teacherInput = input()
            dayBeingSetted[classInput] = teacherInput
            firstAtTheDay = False

        firstClass = False
        if len(dayBeingSetted) == 6:
            daySet = False
            firstDay = False
            settingDay = settingDay + 1
            firstAtTheDay = True
        
        if settingDay == 5:
            print("seu cronograma está pronto!!!")
            setting = False


print("----------", "-segunda-feira-", "-terça-feira-", "-quarta-feira-", "-quinta-feira-", "-sexta-feira-")
numbers = [0, 1, 2, 3, 4, 5]
for n in numbers:
    print("----------", list(monday)[n], list(tuesday)[n], list(wednesday)[n], list(thursday)[n], list(friday)[n])

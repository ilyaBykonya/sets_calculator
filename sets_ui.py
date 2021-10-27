import data_structures as Data

#Считывание множеств
###################################
def readOneSet() -> (str, set):
    set_name = str(input("Input set name: "))
    
    set_values = set()
    set_size = int(input("Enter amount of elements: "))

    print("Input set elements:")
    for i in range (0, set_size):
        set_values.add(input())

    return (set_name, set_values)#set(), чтобы элементы множества были уникальными

def readSetsDict() -> dict:
    sets_dectionary = {}
    amount_of_sets = int(input("Enter amount of sets: "))
    for i in range (0, amount_of_sets):
        x, y = readOneSet()
        sets_dectionary[x] = y

    return sets_dectionary
###################################

#Вывод множеств
###################################
#Ну почему это уродство не даёт свернуть это несчатсную функцию....
def printOneSet(set_name: str, set_values: set):
    print('[' + set_name + ']', set_values)

def printAllSets(sets_data: dict):
    print("------------------------------")
    for set_name in sets_data:
        printOneSet(set_name, sets_data[set_name])
    print("------------------------------")
###################################

#Считывание выражений
###################################
def readOneExpression() -> Data.Expresssion:
    print("Input expression:")
    result_set_name = input("Result set name: ")
    first_set_name = input("First set name: ")
    operation_name = input("Operation: ")
    second_set_name = input("Second set name: ")
    print()
    return Data.Expresssion(result_set_name, first_set_name, second_set_name, operation_name)

def readAllExpressions() -> list:
    expressions_list = []
    amount_of_expressions = int(input("Enter amount of expressions: "))
    for i in range (0, amount_of_expressions):
        expressions_list.append(readOneExpression())

    return expressions_list
###################################


#Справка об операциях
###################################
def printHelp():
    print("---------- Help ----------")
    print("& — intersection")
    print("| — mergt")
    print("/ — difference")
    print("\ — symmetric difference")
    print("--------------------------")
###################################

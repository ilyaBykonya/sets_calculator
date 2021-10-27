import application_operations as App
import sets_ui as Ui

Ui.printHelp()

allSetsDictionary = Ui.readSetsDict()
Ui.printAllSets(allSetsDictionary)


for expression in Ui.readAllExpressions():
    new_set_name, new_set_value = App.calculate_expression(expression, allSetsDictionary)
    allSetsDictionary[new_set_name] = new_set_value
    Ui.printAllSets(allSetsDictionary)#Показываем юзеру изменения

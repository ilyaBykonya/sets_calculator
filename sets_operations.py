#Операции над множествами

def merge(first_set: set, second_set: set) ->set:
    result_elements = set()

    for elem in first_set:
        result_elements.add(elem)
    for elem in second_set:
        result_elements.add(elem)

    return result_elements

def intersection(first_set: set, second_set: set) ->set:
    result_elements = set()

    for elem in first_set:
        if elem in second_set:
            result_elements.add(elem)

    return result_elements

def sets_difference(first_set: set, second_set: set) ->set:
    result_elements = set()

    for elem in first_set:
        if not(elem in second_set):
            result_elements.add(elem)

    return result_elements

def symmetric_sets_difference(first_set: set, second_set: set) ->set:
    result_elements = set()

    for elem in first_set:
        if not(elem in second_set):
            result_elements.add(elem)
            
    for elem in second_set:
        if not(elem in first_set):
            result_elements.add(elem)

    return result_elements



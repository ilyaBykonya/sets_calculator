import sets_operations as Operations
import data_structures as Data

def calculate_expression(expression: Data.Expresssion, sets_dict: dict) -> (str, set):
    first_set = sets_dict[expression.first_set_name]
    second_set = sets_dict[expression.second_set_name]

    if expression.operation_name == '&':
        return (expression.result_set_name, Operations.intersection(first_set, second_set))
    elif expression.operation_name == '|':
        return (expression.result_set_name, Operations.merge(first_set, second_set))
    elif expression.operation_name == '/':
        return (expression.result_set_name, Operations.sets_difference(first_set, second_set))
    elif expression.operation_name == '\\':
        return (expression.result_set_name, Operations.symmetric_sets_difference(first_set, second_set))
    else:
        return (expression.result_set_name, set())

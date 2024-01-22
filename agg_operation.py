#!/venv/bin/python3

"""This is a further development of Convert and Aggregate mission. 
You are given a list of tuples. Each tuple consists of two values: a string and an integer.
You need to create and return a dictionary, where keys are string values (except the first character) 
from input tuples. Values are aggregated integer values from input tuples for each specific key. 
Each aggregating operation must be done according to the operation sign - the first character of string key. 
Division by zero should be ignored. The resulted dictionary should not include items with empty key or zero value."""

def aggr_operation(keys_values: list) -> dict:
    # create dictionary to hold key/value pairs
    dict = {}

    # extract key elements from tuples
    s = [i for i, j in keys_values]
    keys = [i[1] for i in s]
    operators = [i[0] for i in s]

    

    print(operators)

print(aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]))
#assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
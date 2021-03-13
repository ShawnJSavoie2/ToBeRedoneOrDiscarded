# IDLE (Python 3.8.0)

# Print List Or Dictionary

def print_vertical_lict(lict):
    for element in lict:
        print(element)

def print_horizontal_lict(lict):
    string = ''
    for element in lict:
        string = string + str(element) + ', '
    print(string)
    print()

def print_vertical_dictionary(dictionary):
    for key in dictionary:
        pair = key + ': ' + str(dictionary[key])
        print(pair)

def print_horizontal_dictionary(dictionary):
    string = ''
    for key in dictionary:
        string = string + key + ': ' + str(dictionary[key]) + ', '
    print(string)

def keys(dictionary):
    keys = []
    for key in dictionary:
        keys.append(key)
    return keys

def values(dictionary):
    values = []
    for key in dictionary:
        values.append(dictionary[key])
    return values

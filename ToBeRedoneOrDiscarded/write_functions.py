# IDLE (Python 3.8.0)

# write_list_or_dictionary

def write_vertical_lict(file_name, lict):
    file = open(file_name, 'w')
    for element in lict:
        element = str(element) + '\n'
        file.write(element)
    file.close()

def write_horizontal_lict(file_name, lict):
    row = ''
    for index in range(len(lict)):
        lict[index] = str(lict[index]) + ', '
        if len(row + lict[index]) > 64:
            lict[index - 1] = lict[index - 1] + '\n'
            row = lict[index]
        else:
            row = row + lict[index]
    file = open(file_name, 'w')
    for term in lict:
        file.write(term)
    file.close()

def write_vertical_dictionary(file_name, dictionary):
    file = open(file_name, 'w')
    for key in dictionary:
        pair = key + ': ' + str(dictionary[key]) + '\n'
        file.write(pair)
    file.close()

~def write_horizontal_dictionary(file_name, dictionary):
    file = open(file_name, 'w')
    row = ''
    for key in dictionary:
        term = term + ': ' + dictionary[term] + ', '
        if len(row + term) > 64:
            row = row + '\n'
            file.write(row)
            row = ''
        else:
            row = row + term
    file.close()


# IDLE (Python 3.8.0)

# user-input-handling functions

def user_input_handling_function_first():
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    while good_to_go == 'no':
        if ' ' in user_input:
            print('The sequence of characters contains one or more spaces.')
            errors.append('yes')
        if ',' in user_input:
            print('The sequence of characters contains one or more commas.')
            errors.append('yes')
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input

def user_input_handling_function_second(dictionary):
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    lict = []
    while good_to_go == 'no':
        for key in dictionary:
            lict.append(key):
        for element in user_input:
            if element not in lict
                print('The form can only contain a combination of the characters that represent the lists of characters.')
                errors.append('yes')
                break
        if len(user_input) < 2:
            print('The form is too short. It can\'t be less than two-characters long.')
            errors.append('yes')
        if len(user_input) > 8:
            print('The form is too long. It can\'t be more than eight-characters long.')
            errors.append('yes')
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = [] 
        else:
            good_to_go = 'yes'
    return user_input

def user_input_handling_function_third(): # yes_or_no
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    yes_or_no = ['yes', 'no']
    while good_to_go == 'no':
        if user_input not in yes_or_no:
            print('You have to answer yes or no.')
            errors.append('yes')
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input
    
def user_input_handling_function_fourth(dictionary):
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    while good_to_go == 'no':
        if user_input not in dictionary:
            print('The form you entered does not match one of the forms in your termal_dictionary. Each form in your')
            print('termal_dictionary is a name (key) that has an associated definition (value) that is a list of terms')
            print('that all have the same form as the name (key).')
            errors.append('yes')
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input

def user_input_handling_function_fifth():
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    while good_to_go == 'no':
        for i in user_input:
            if i not in digits:
                print('The number must consist of digits. For example: 1, 12, 123.1 or 1234.1.')
                errors.append('yes')
                break
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input
    
def user_input_handling_function_sixth():
    ''' float checker '''
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    while good_to_go == 'no':
        for_loop_broken = 'yes'
        while for_loop_broken == 'yes':
            for i in user_input:
                if i not in digits:
                    for_loop_broken = 'yes'
                    print('The number must consist of digits. For example: 1, 12, 123.1 or 1234.1')
                    print()
                    user_input = input('Re-enter: ')
                    print()
                    break
                else:
                    for_loop_broken = 'no'
        if float(user_input) <= 0:
            print('The velocity can\'t be less than or equal to 0 m/s.')
            errors.append('yes')
        if float(user_input) > 38_573_389.830_824_5:
            print('The velocity can\'t be greater than 38,573,389.830 824 5 m/s.')
            errors.append('yes')
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
            for_loop_broken = 'yes'
        else:
            good_to_go = 'yes'
    return float(user_input)

def user_input_handling_function_seventh():
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    unacceptable_characters = ['<', '>', '?', ':', '"', '|', '-', '/', '\ ']
    while good_to_go == 'no':
        if '.txt' not in user_input:
            user_input = user_input + '.txt'
        for i in user_input:
            if i == ' ': # <-- fix this.
                i = '_'
            elif i in unacceptable_characters:
                print('The file name can not contain any of the following characters: <, >, ?, :, ", |, -, /, \ ')
                errors.append('yes')
                break
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input

def user_input_handling_function_eighth():
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    while good_to_go == 'no':
        if user_input == 'None':
            user_input = None
            return user_input
        else:
            for inner in user_input:
                if inner not in digits:
                    print('The number must be an integer that consists of digits. For example: 1, -2, etc.')
                    errors.append('yes')
                    break
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return int(user_input)

def user_input_handling_function_ninth():
    ''' parser '''
    print()
    user_input = input('Enter: ')
    print()
    term = ''
    lict = []
    for element in user_input:
        if element != ' ':
            term = term + element
        else:
            lict.append(term)
            term = ''
    lict.append(term) # because term might not be empty....
    return lict

def user_input_handling_function_tenth(dictionary):
    ''' dictionary checker '''
    user_input = parser()
    good_to_go = 'no'
    errors = []
    while good_to_go == 'no':
        string = ''
        lict = []
        for element in user_input:
            string = string + element
        for key in dictionary:
            for element in dictionary[key]:
                lict.append(element)
        for element in string:
            if element not in lict:
                print('One of your unwanted characters or combination of characters does not match the characters you')
                print('entered earlier.')
                errors.append('yes')
                break
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input
    

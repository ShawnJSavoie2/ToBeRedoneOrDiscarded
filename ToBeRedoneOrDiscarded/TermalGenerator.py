# IDLE (Python 3.8.0)

# termal_generator

def termal_generator(lict):
    length_of_termal_generator = 16
    padding = length_of_termal_generator - len(lict)
    count = padding
    while count != 0:
        lict.append([''])
        count = count - 1
    termal_lict = []
    for first_inner in lict[0]:
        for second_inner in lict[1]:
            for third_inner in lict[2]:
                for fourth_inner in lict[3]:
                    for fifth_inner in lict[4]:
                        for sixth_inner in lict[5]:
                            for seventh_inner in lict[6]:
                                for eighth_inner in lict[7]:
                                    for ninth_inner in lict[8]:
                                        for tenth_inner in lict[9]:
                                            for eleventh_inner in lict[10]:
                                                for twelfth_inner in lict[11]:
                                                    for thirteenth_inner in lict[12]:
                                                        for fourteenth_inner in lict [13]:
                                                            for fifteenth_inner in lict [14]:
                                                                for sixteenth_inner in lict[15]:
                                                                    term = (
                                                                      first_inner + second_inner +
                                                                      third_inner + fourth_inner +
                                                                      fifth_inner + sixth_inner +
                                                                      seventh_inner + eighth_inner +
                                                                      ninth_inner + tenth_inner +
                                                                      eleventh_inner + twelfth_inner +
                                                                      thirteenth_inner + fourteenth_inner +
                                                                      fifteenth_inner + sixteenth_inner
                                                                    )
                                                                    termal_lict.append(term)
    return termal_lict


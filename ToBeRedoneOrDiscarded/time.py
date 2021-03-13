# IDLE (Python 3.8.0)

# YMDHMS (Years, Months, Days, Hours, Minutes, Seconds)

def WAF(FrO, O, ScO):
    # WAF means Whole And Fraction.
    # FrO means First Operand and is a value of a variable.
    # O means Operator and is a string of an operator symbol.
    # ScO means Second Operand and is a value of a variable.
    if O == ' + ':
        Sum = FrO + ScO
        Whole = int(Sum)
        Fraction = Sum - Whole
        return Whole, Fraction
    elif O == ' - ':
        Remainder = FrO - ScO
        Whole = int(Remainder)
        Fraction = Remainder - Whole
        return Whole, Fraction
    elif O == ' * ':
        Product = FrO * ScO
        Whole = int(Product)
        Fraction = Product - Whole
        return Whole, Fraction
    elif O == ' / ':
        Quotient = FrO / ScO
        Whole = int(Quotient)
        Fraction = Quotient - Whole
        return Whole, Fraction
    elif O == ' ** ':
        Power = FrO ** ScO
        Whole = int(Power)
        Fraction = Power - Whole
        return Whole, Fraction
    elif O == ' v ':
        NPower = FrO ** (1 / ScO)
        Whole = int(NPower)
        Fraction = NPower - Whole
        return Whole, Fraction

def YMDHMS(S):
    # YMDHMS means Years, Months, Days, Hours, Minutes, Seconds.
    SIY = 31536000
    # SIY means Seconds In Year.
    MIY = 12
    # MIY means Months In Year.
    DIM = 30.416
    # DIM means Days In Month.
    HID = 24
    # HID means Hours In Day.
    MIH = 60
    # MIH means Minutes In Hour.
    SIM = 60
    # SIM means Seconds In Minute.

    ###########################################################################

    years, F = WAF(S, ' / ', SIY)
    months, F = WAF(F, ' * ', MIY)
    days, F = WAF(F, ' * ', DIM)
    hours, F = WAF(F, ' * ', HID)
    minutes, F = WAF(F, ' * ', MIH)
    seconds, F = WAF(F, ' * ', SIM)
    Q = [years, months, days, hours, minutes, seconds]
    #Q means Quantities.
    U = [' year/s, ', ' month/s, ', ' day/s, ', ' hour/s, ', ' minute/s, ', ' second/s ']
    # U means Units.
    for I in Q:
        if I != 0:
            In = Q.index(I) 
            # In means Index.
            MQ = Q[In : ]
            # MQ means Modified Q.
            MU = U[In : ]
            # MU means Modified U.
            Time = 'The time is: '
            # St means String.
            for I in range(len(MQ)):
                Time = Time + (str(MQ[I]) + MU[I])
            return Time
            
        

T = YMDHMS(31622402)
print(T)

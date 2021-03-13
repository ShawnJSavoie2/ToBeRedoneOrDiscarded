# IDLE (Python 3.8.0)

# whole_and_fraction

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


T = WAF(8, ' v ', 3)
print(T)
        

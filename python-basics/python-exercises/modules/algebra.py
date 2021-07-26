#addition function
def add (*num):
    sum = 0
    for x in num:
        sum += x
    return sum

#substraction function
def subtract (firstNum, *otherNum):
        diff = 0
        acc = 0
        for x in otherNum: #accumulate all the difference numbers
            acc += x
        diff = firstNum - acc
        return diff

#division function
def divide (numerator, denominator):
    if (denominator == 0):
        raise ZeroDivisionError("Denominator cannot be 0")
        pass
    elif numerator == 0 or denominator == 0:
        raise ValueError("Both numerator and denominator cannot be 0")
        pass
    else:
        div = numerator / denominator
        div = round(div, 2)
        return div



#multiply function
def multiply (*num):
    if num is None:
        raise ValueError("At least one number should be provided")
        #pass
    else:
        mult = 1
        for x in num:
            mult *= x
        return mult






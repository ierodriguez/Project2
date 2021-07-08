def division(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "Error: can't divide by zero"

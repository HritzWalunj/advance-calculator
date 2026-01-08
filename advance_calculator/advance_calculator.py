
def power(a, b):
    return a ** b

def square(a):
    return a * a

def cube(a):
    return a * a * a

def average(a, b):
    return (a + b) / 2

def percentage(value, total):
    if total == 0:
        raise ValueError("Total cannot be zero")
    return value / total * 100

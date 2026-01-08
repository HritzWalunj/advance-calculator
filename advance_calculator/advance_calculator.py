from calculator.basic.calculator.calculator import add, mul, div

def power(a, b):
    return a ** b

def square(a):
    return mul(a , a)

def cube(a):
    return a * a * a

def average(a, b):
    return div(add(a, b), 2)

def percentage(value, total):
    if total == 0:
        raise ValueError("Total cannot be zero")
    return div(value , total) * 100

print(f"square= {square(3)}")

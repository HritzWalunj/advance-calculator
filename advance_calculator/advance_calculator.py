"""Add advance calculator functions"""

def power(a, b):
    """retrun a given power of a number"""
    return a ** b

def square(a):
    """retrun a square of a number"""
    return a * a

def cube(a):
    """retrun a cube of a number"""
    return a * a * a

def average(a, b):
    """retrun a average of a numbers"""
    return (a + b) / 2

def percentage(value, total):
    """retrun percentage"""
    if total == 0:
        raise ValueError("Total cannot be zero")
    return value / total * 100

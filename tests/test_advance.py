"""pytest test cases for testing """
from advance_calculator.advance_calculator import power, square, cube, average, percentage

def test_power():
     """test power functionality"""
    assert power(2 , 3) == 8

def test_square():
     """test power functionality"""
    assert square(2) == 4

def test_cube():
     """test power functionality"""
    assert cube(3) == 27

def test_average():
     """test power functionality"""
    assert average(2, 4) == 3

def test_percentage():
     """test power functionality"""
    assert percentage(22, 100) == 22
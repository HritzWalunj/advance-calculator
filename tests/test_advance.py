from advance_calculator.advance_calculator import power, square, cube, average, percentage

def test_power():
    assert power(2 , 3) == 8

def test_square():
    assert square(2) == 4

def test_cube():
    assert cube(3) == 27

def test_average():
    assert average(2, 4) == 3

def test_percentage():
    assert percentage(22, 100) == 22
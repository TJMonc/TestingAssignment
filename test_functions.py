import pytest
from functions import *

@pytest.mark.parametrize("fileNames", [66, "testing.txt", "Bruh.txt", True])
def test_openFile(fileNames):
    assert(openFile(fileNames) == None or -1)

@pytest.mark.parametrize("num1,num2", [(66, 30), (4.0, 0), ("3", 2), ("sixteen", 9), (True, "55")])
def test_numbers(num1, num2):
    assert(numbers(num1, num2) == "Error" or (float(num1)/float(num2)))

@pytest.mark.parametrize("x1, y1, x2, y2",
[(30, 2, 4, 5), (-4, -3, 5, -20), ("3", 2, "44", 3),("six", "seven", 9, 2), (True, False, 3, 3.3)])
def test_distance(x1, y1, x2, y2):
    assert(dist(x1, y1, x2, y2) == -1 or math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2))
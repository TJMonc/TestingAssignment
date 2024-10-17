import pytest
from functions import *
#test integers, correct input, incorrect input), very large number
@pytest.mark.parametrize("fileNames", [66, "testing.txt", "Bruh.txt", ["testing.txt", "5"], 10*10*1000])
def test_openFile(fileNames, capsys):
    if(openFile(fileNames) == -1):
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == "File Name incorrect"
    else:
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == "File opened."

#test correct input, divide by 0, convertable string, inconvertable string, bool input, and absurdly large number
@pytest.mark.parametrize("num1,num2", [(66, -30), (4.0, 0), (0,0), ("3", 10*10**1000), ("sixteen", 9), (True, "55")])
def test_numbers(num1, num2, capsys):
    if(numbers(num1, num2) == "Error"):
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == "Numbers not entered" or "You can't divide by 0" or "Number Too Big"
    else:
        assert(numbers(num1, num2) == "Error" or (float(num1)/float(num2)))

#Test correct input, negative input, convertable string, inconvertable string, boolean inputs, and very large numbers
@pytest.mark.parametrize("x1, y1, x2, y2",
[(30, 2, 4, 5), (-4, -3, 5, -20), ("3", 2, "44", 3),("six", "seven", 9, 2), (True, False, 3, 3.3), (20, -55, 9, 10*10**1000)])
def test_distance(x1, y1, x2, y2, capsys):
    if(dist(x1, y1, x2, y2) == -1):
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == "Numbers not entered" or "Number Too Big"
    else:
        assert(dist(x1, y1, x2, y2) == math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2))
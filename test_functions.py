import pytest
from functions import *

@pytest.mark.parametrize("fileNames", [66, "testing.txt", "Bruh.txt", 5.0])
def test_openFile(fileNames):
    if(fileNames == "testing.txt"):
        assert(openFile(fileNames) == None)
    else:
        assert(openFile(fileNames) == -1)

@pytest.mark.parametrize("num1, ", [66, "testing.txt", "Bruh.txt", 5.0])
def test_numbers(num1, num2)
    
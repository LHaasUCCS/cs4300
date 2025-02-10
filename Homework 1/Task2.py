import pytest

def add(a, b):
    return a + b

def compare(a, b):
    return a == b

def test_add():
    assert add(1, 2) == 3
    assert add(1, 2.75) == 3.75 #retains larger bucket
    assert add("hello", "world") == "helloworld" #concats
    assert add(True, True) == 2 #True = 1 

def test_compare():
    assert compare("hello", True) == False
    assert compare(1, True) == True
    assert compare(1, 1.00) == True # Somehow works in Python but i know this would fail in C++

print(add(1, 2))
print(add(1,2.75))
print(add("hello", "world"))
print(add(True, True))

print(compare("hello", True))
print(compare(1, True))
print(compare(1, 1.00))


   
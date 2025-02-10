import pytest

def output():
    print("Hello, World!")

def test_output(capsys):  
    output()  
    captured = capsys.readouterr()  
    assert captured.out == "Hello, World!"  

output()
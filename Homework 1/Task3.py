import pytest

def check_sign(num):
    if num > 0:
        result = "positive"
    elif num < 0:
        result = "negative"
    else:
        result = 0
    
    return result

def prime():
    primes = []  # list to store prime numbers
    for i in range(2, 100): #start at 2 to avoid divide by 0 and 1 is not prime  
        prime = True
        for j in range(2, i):  
            if i % j == 0: # divide by all previous numbers
                prime = False
                break  # preemptively stop inner loop if divisible
        if prime:
            primes.append(i)  # append the prime number to the list
    
    return primes  

def loop():
    x = 100
    result = 0
    while(x != 0):
        result = result + x
        x = x - 1
    
    return result

def test_check_sign():
    assert check_sign(6) == "positive"
    assert check_sign(-3) == "negative"
    assert check_sign(0) == 0

def test_prime():
    assert prime() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def test_loop():
    assert loop() == 5050

print(check_sign(6))
print(check_sign(-3))
print(check_sign(0))
print(prime())
print(loop())

    
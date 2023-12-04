"""List of prime numbers generator."""
from math import sqrt, floor

"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError
    list = []
    currentNumber = 2
    while len(list) != number_of_primes:
        is_prime = True
        for i in range (2,floor(sqrt(currentNumber))+1):
            if (currentNumber % i) == 0:
                is_prime = False
                break
        if is_prime:
            list.append(currentNumber)
        currentNumber += 1
    return list

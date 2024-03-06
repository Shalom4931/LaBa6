import time
from math import sqrt

def calculate_square_root(number, milliseconds):
    time.sleep(int(milliseconds) / 1000)  
    result = sqrt(int(number))
    return result

number = input()
milliseconds = input()

print(f"Square root of {number} after {milliseconds} milliseconds is {calculate_square_root(number, milliseconds)}")

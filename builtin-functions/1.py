from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None
    
    numbers = [int(num) for num in numbers.split()]
    
    result = reduce(lambda x, y: x * y, numbers)
    return result


my_list = input()

result = multiply_list(my_list)
print(result)
# Lab 5.4
# findNumbers.py

def find_numbers(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append("positive")
        elif num < 0:
            result.append("negative")
        else:
            result.append("zero")
    return result

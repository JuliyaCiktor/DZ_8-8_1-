def add_one(some_list):
    number = 0
    for digit in some_list:
        number = number * 10 + digit
    number += 1
    result = []
    while number > 0:
        result.append(number % 10)
        number //= 10
    result.reverse()
    return result or [0]
# Тест
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]

print("ОК")

numbers = {1, 2, 5, 5, 7}
numbers.add(3)
print(numbers)
print(len("hello"))

first = {1, 3, 7, 2}

print(numbers & first)
print(numbers | first)
print(numbers ^ first)

print((numbers - first).union((first - numbers)) == (numbers ^ first))

# def increment(number, by=1):
#     return number + by


# print(increment(34, 4))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total*=number
#     return total


# print(multiply(2, 3, 4, 5))

def save_user(**user):
    print(user["name"])


save_user(id=1, name='John', age=123)

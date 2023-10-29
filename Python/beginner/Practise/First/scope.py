message = "a"


def greet():
    global message
    message = "b"


greet()
print(message)

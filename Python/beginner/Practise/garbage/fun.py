# def hello(number, by=1):
#     return number, number+by


# print(hello(2))

def multiply(**hemlo):
    p = 1
    for number in hemlo:
        p *= hemlo[number]
    return p


print(multiply(x=1, y=2, z=3))

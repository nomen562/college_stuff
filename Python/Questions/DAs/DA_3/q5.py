n = int(input("Enter number of terms"))


def fact(n):
    return 1 if n == 0 else n * fact(n-1)


def sin():
    result = "x"
    for i in range(n-1):
        sign = ' - ' if i % 2 == 0 else ' + '
        term = f"x^{2*i+1}/{fact(2*i+1)}"
        result += sign + term
    return result


def cos():
    result = "1"
    for i in range(n-1):
        sign = ' - ' if i % 2 == 0 else ' + '
        term = f"x^{2*(i+1)}/{fact(2*(i+1))}"
        result += sign + term
    return result


def tan():
    result = [" + 1/3x^3"," + 17/375x^7"," + 62/2835x^9"]
    s = "x^2"
    for i in range(n-1):
        s += result[i]
    return s

print(f"Series of sinx: {sin()}")
print(f"Series of cosx: {cos()}")
print(f"Series of tanx: {tan()}")
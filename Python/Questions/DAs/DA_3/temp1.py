def nth_derivative_tan(x, n):
    if n == 0:
        return x
    elif n % 2 == 1:
        return nth_derivative_tan(x, n - 1) + ((-1) ** ((n - 1) // 2)) * factorial(2 * (n - 1)) * x ** (2 * (n - 1) + 1)
    else:
        return nth_derivative_tan(x, n - 1)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# Specify the order of the derivative (n)
n = 3  # Change n to the desired order of the derivative

# Specify the value of x
x = 2.0  # Change this value to the desired value of x

# Calculate the nth derivative of tan(x)
result = nth_derivative_tan(x, n)

# Print the result
print(f"The {n}th derivative of tan(x) is:")
print(result)

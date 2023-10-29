def fizz_buzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return ("Fizzbuzz")
    if n % 3 == 0:
        return ("Fizz")
    if n % 5 == 0:
        return ("Buzz")
    else:
        return (n)


str = "Enter number>"
print(f"{fizz_buzz(n = int(input(str)))}")

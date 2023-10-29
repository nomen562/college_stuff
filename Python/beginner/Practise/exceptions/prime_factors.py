n1, n2, n3 = int(input("Enter 1st number>")), int(
    input("Enter 2nd number>")), int(input("Enter 3rd number>"))
limit = n1*n2*n3
factor = '1'
x = 2
limit = min(n1, n2, n3)


def is_prime(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    return True if c == 2 else False


while not is_prime(limit):
    if n1 % x == 0 and n2 % x == 0 and n3 % x == 0 and limit % x == 0:
        factor += f"*{x}"

        limit //= x
    else:
        x += 1
print(factor)

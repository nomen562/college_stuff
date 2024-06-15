n1 = int(input("Enter 1st number>"))
n2 = int(input("Enter 2nd number>"))
n3 = int(input("Enter 3rd number>"))
c = 2
pf = "1"


def co_prime(n1, n2, n3):
    c = 0
    for i in range(1, min(n1, n2, n3)+1):
        if n1 % i == 0 and n2 % i == 0 and n3 % i == 0:
            c += 1
    return True if c == 2 else False


while not co_prime(n1, n2, n3):
    r1, r2, r3 = n1 % c, n2 % c, n3 % c

    if r1 == 0 and r2 == 0 and r3 == 0:
        n1 //= c
        n2 //= c
        n3 //= c
        pf += f"*{c}"
    else:
        c += 1
print(pf)

# Write a Python to find nCr and nPr from the values of n and r.
n = int(input("Enter the value of n>"))
r = int(input("Enter the value of r>"))


def fact(num):
    f = 1
    for i in range(num):
        f *= (i+1)
    return f


print(f"nCr is> {fact(n)/(fact(n-r)*fact(r))}")
print(f"nPr is> {fact(n)/(fact(n-r))}")

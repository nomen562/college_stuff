a = float(input("Enter your number>"))
b = int(a)
x = 1.1
y = 1
while x != int(x):
    x = a*y
    y = y*10

p = b
q = int(x)
i = 0
j = 0

while p > 0:
    p = p//10
    i += 1

while q > 0:
    q = q//10
    j += 1

print(
    f"Number of digits before decimal point are>{i}\nThe number of digits after decimal point are>{j-i}")

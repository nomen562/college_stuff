# Write a python program to get a floating-point number from the user
# and find the number of digits in the whole number part and fractional
# part.
n = float(input("Enter your number>"))
dup = n
real = 0
c1, c2 = 0, 0


while n != 0.0:
    c1 += 1
    real = (int(n) % 10) + real*10
    n //= 10

while (float(dup) > int(dup)):
    dup = dup * 10
    c2 += 1

print(
    f"Number of digits before decimal point are>{c1}\nThe number of digits after decimal point are>{c2}")

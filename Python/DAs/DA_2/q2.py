# Obtain an integer number (containing any number of digits) from the
# user and print it in the reverse order and check if the number is an
# Armstrong number or not.

n = int(input("Enter your number>"))
dup = n
sum = 0
rev = 0
c = 0  # counter variable for counting number of digits
# Finding reverse and counting the number of digits
while n != 0:
    rev = rev * 10 + n % 10
    n //= 10
    c += 1
# Finding if n is an armstrong number
n = dup
while n >= 1:
    sum += (n % 10)**c
    n //= 10
print(f"The reverse of the number is>{rev}")
if sum == dup:
    print("It is an armstrong number")
else:
    print("Not an armstrong number")

num = float(input("Enter the number: "))

var = num

while var != int(var):
    var *= 10

temp1 = int(num)
temp2 = int(var)
cnt1 = 0
cnt2 = 0

while temp1 > 0:
    temp1 //= 10
    cnt1 += 1

while temp2 > 0:
    temp2 //= 10
    cnt2 += 1

print()
print("No. of digits in whole part:", cnt1)
print("No. of digits in fractional part:", (cnt2 - cnt1))

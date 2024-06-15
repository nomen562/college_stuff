n = int(input("Enter your number>"))
c = 0
flag = True
while n > 1:
    if n % 2 == 0:
        c+=1
    else:
        flag = False
        break
    n//=2
if flag:
    print(f"The power of 2's are {c} that is 2^{c}")
else:
    print("Cannot be expressed in the form of 2^n")
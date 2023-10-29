n = int(input("Enter number of fibonacci numbers>"))
a, b = 0, 1
strk = "0 1 "
for i in range(n-2):
    c = a + b
    strk += (str(c)+" ")
    t = b
    b = c
    a = t
print(strk)

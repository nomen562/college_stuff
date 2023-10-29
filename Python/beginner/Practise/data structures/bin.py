n = int(input("Enter binary number>"))
bin = ""
while n!=0:
    bin = str(n%2) + bin  
    n//=2
print(bin)
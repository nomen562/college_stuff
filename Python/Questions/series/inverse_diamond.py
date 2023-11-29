n = int(input("Enter no of lines"))
no_of_spaces = n//2 - 1
while abs(no_of_spaces) < n:
    print((n//2 +1 - no_of_spaces)*"*"+" "*no_of_spaces+(n//2 +1 - no_of_spaces)*"*")
    no_of_spaces -= 1  
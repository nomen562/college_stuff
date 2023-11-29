# python program to find all lucky numbers before N

# take input from the user
num = int(input("Enter the number: "))

# initialize array
arr = [i for i in range(1, num + 1)]

# find lucky number
step = 1
while (step < num) :
    i = step
    while (i < num) :
        j = i
        while (j < num - 1) :
            arr[j] = arr[j + 1]
            j += 1
        num -= 1
        i += step
    step += 1

# print array
for i in range(num):
    print(arr[i], end=" ")d
print()
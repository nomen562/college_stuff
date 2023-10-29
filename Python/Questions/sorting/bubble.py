x = [45, 7, 345, 52, 90, 21, 32]
sorted = False
while not sorted:
    sorted = True
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            sorted = False
            x[i], x[i+1] = x[i+1], x[i]
print(x)

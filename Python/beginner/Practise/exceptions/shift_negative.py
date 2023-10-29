l = []
neg = []
n = int(input("Enter N>"))
for x in range(n):
    l.append(int(input(f"Enter {x+1} element>")))
print(l)

for i, x in enumerate(l):
    if x < 0:
        neg.append(x)
        del l[i]
        i += 1
print(l+neg)

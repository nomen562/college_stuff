l = [6, 8, 1, 4, 5, 3, 7, 2]
for index, element in enumerate(l):
    to_comp = l[index+1]
    j = index+1
    for i in range(index, 0, -1):
        if to_comp > l[i]:
            to_comp = l[i]
            l[j], l[i] = l[i], l[j]
            j = i
print(l)

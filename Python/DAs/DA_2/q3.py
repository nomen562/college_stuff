# Sort the given numbers in list-1 and list-2 and combine the sorted lists.
# Use suitable and efficient logic to sort the combined list.

l1 = [5, 23, 12, 51, 3, 1, 99]
l2 = [7, 124, 61, 523, 11, 12, 145, 52, 2]
l = []


def sort_list(l):

    for i in range(len(l)-1):
        for x in range(i+1, len(l)):
            if l[x] < l[i]:
                t = l[i]
                l[i] = l[x]
                l[x] = t
    return l


l1, l2 = sort_list(l1), sort_list(l2)
print(f"Sort2ed l1>{l1}\nSorted l2>{l2}")
i, j = 0, 0
while i < len(l1) and j < len(l2):
    if l1[i] == l2[j]:
        l.append(l1[i])
        i += 1
        j += 1
    if l1[i] < l2[j]:
        l.append(l1[i])
        i += 1
    else:
        l.append(l2[j])
        j += 1

print(f"Combined list>{l + l1[i:] + l2[j:]}")

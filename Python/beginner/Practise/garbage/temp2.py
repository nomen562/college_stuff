l = [[1, 0, 2, 13], [134, 0, 123], [2, 3, 5]]


def sortk(item):
    return item[2]


print(sorted(l, key=sortk))

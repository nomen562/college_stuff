l = [3, 425, 52, 23, 35, 6345, 23, 1]


def smallest_element(*l):
    min = l[0]
    pos = 0
    for x in enumerate(l):
        if min > x[1]:
            min = x[1]
            pos = x[0]
    return min, pos


print(smallest_element(l))

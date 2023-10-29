import random
cycle = True
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
matrix = [[a, b, c], [d, e, f], [g, h, i]]
while cycle:
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = random.choice(list)
    list.remove(a)
    b = random.choice(list)
    list.remove(b)
    c = random.choice(list)
    list. remove(c)
    d = random.choice(list)
    list. remove(d)
    e = random.choice(list)
    list. remove(e)
    f = random. choice(list)
    list. remove(f)
    g = random.choice(list)
    list. remove(g)
    h = random.choice(list)
    list. remove(h)
    i = random.choice(list)
    list.remove(i)
    matrix = [[a, b, c], [d, e, f], [g, h, i]]
    if a+b+c == d+e+f == g+h+i == a+e+i == a+d+g == b+e+h == c+f+i == i+e+a:
        print(matrix)
        cycle = False
    else:
        print(matrix)
        print("cycled")

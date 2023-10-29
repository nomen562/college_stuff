s = range(5)
k = [*"Hello"]
print(list(s))
print(*list(s))
print(*"Hello")
print([*range(5)], [*"Hello"])
# Combination
first = [1, 2]
second = [3]
values = [first + second]
print(values)
print(*first, 32, *second, *"hello")
# Unpacking dictionary with two **
dick_1 = dict(x=1)
dick_2 = dict(x=10, y=2)
combi = {**dick_1, **dick_2, "z": 4}
print(combi)

item = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def price(x):
    return x[1]


x = map(price, item)
y = filter(lambda a: a[1] >= 10, item)
print(list(x))
print(list(y))
print([item[1] for item in item])
print([item for item in item if item[1] >= 10])

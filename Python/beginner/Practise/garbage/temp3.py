items = (
    ("a", 423),
    ("b9"),
    ("c12")
)

prices = []
for item in items:
    prices.append(item[1])

print(prices)

z = map(lambda a: tuple(a), items)
for i in z:
    print(i)

filter

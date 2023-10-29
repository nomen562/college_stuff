
# numbers = list("Hello")
# numbers[-1] = "sd"
# print(numbers[::2])
# l = [
#     ("Product1", 1),
#     ("Product3", 98),
#     ("Product3", 12)
# ]


# def sort_items(item):
#     return (item[1])


# print(sorted(l, key=sort_items))

# l = [
#     ("Product1", 12),
#     ("Product2", 93),
#     ("Product3", 4)
# ]


# l.sort(key=lambda item: item[1], reverse=True)
# print(l)

l = [
    ("Product1", 23),
    ("Product2", 4),
    ("Product3", 93)
]

# prices = []
# for i in l:
#     prices.append(i[1])
# print(prices)

x = map(lambda m: m[1], l)
for i in x:
    print(x)
print(x)

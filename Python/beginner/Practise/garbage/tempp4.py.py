item = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = filter(lambda item: item[1] > 10, item)
print(list(filtered))

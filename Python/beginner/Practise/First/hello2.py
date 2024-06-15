items = [
    ("Product1", 10),
    ("Product2", 17),
    ("Product3", 11)
]


def sort_item(items):
    return items[1]


items.sort(key=sort_item)
print(items)

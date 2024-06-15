items = [
    ("Product1", 21),
    ("Product2",20),
    ("Product3",30)
]
# def sort_item(item):
#     return item[1]
# print(sorted(items, key=lambda item:item[1]))
print(list(filter(lambda item:item[1]>20,items)))
print([item[1] for item in items])
print(list(map(lambda item:item[1],items)))
print([item for item in items if item[1]>20])
x = [1, 2, 3]
y=[20, 30, 40]
z = "abcd"
print(list(zip(x,y,z))) #Combines several iterables into a tuple
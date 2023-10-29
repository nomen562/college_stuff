dick = {"abc": 123, 123: "abc"}
for x, y in dick.items():
    print(x, y)
point = dict(x=1, y=2)
print(point)
for item in point:
    print(item)
print(point.get('', 5))
del point["x"]
print(point)

n = [1,2,3,4,5]
def length(n):
    return 1 + length(n[1:]) if n else 0
    print(length(n))
print(length(n))
# l = 0
# iterable = [1,2,3,4,5]
# while iterable:
#     l += 1 
#     iterable = iterable[1:]
# print(l)
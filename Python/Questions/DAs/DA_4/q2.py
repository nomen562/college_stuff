# Method 1
def length(n):
    return 1 + length(n[1:]) if n else 0
li = list(input("Enter list separted by space>").split())
tu = input("Enter tuple separted by space>").split()
st = input("Enter string>")
print(f"length of list>{length(li)}\nsize of tuple>{length(tu)}\nlength of string>{length(st)}")
# Method 2
# l = 0
# iterable = [1,2,3,4,5]
# while iterable:
#     l += 1 
#     iterable = iterable[1:]
# print(l)
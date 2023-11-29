# n = int(input(">"))
# l = [r for r in range(1,99)]
# def rem_element(li,i):
#     lis = li
#     t=i
#     for x in range(len(lis)//(i+1)):
#         lis.pop(i)
#         i += t    
#     return lis
    

# def fun():
#     i = 1
#     l = [r+1 for r in range(n)]
#     while True:
#         rem_element(l,i)
#         s = l
#         print(l)
#         i += 1
#         if s == rem_element(list(l),i):
#             break
#     return l
# fun()
# print(fun())
"Method 2"
num = int(input("Enter num>"))
arr = [i+1 for i in range(num)]
step = 1
while step < num:
    i = step
    while i < num:
        j = i
        while j < num - 1:
            arr[j] = arr[j+1]
            j += 1
    step += 1
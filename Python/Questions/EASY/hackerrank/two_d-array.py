# https://www.hackerrank.com/challenges/2d-array/problem
sum_l = []
# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
#        [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
arr = []
for i in range(6):
    print(f"Enter {i+1} row", end=">")
    arr.append(list(map(int, input().rstrip().split())))
for i in range(4):
    for j in range(4):
        s = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+arr[i+1][j+1] + \
            (arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        sum_l.append(s)
print(max(sum_l))

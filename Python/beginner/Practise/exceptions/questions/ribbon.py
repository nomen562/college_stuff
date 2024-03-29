# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:

# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.

# Input
# The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.

# Output
# Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.
n, a, b, c = input().split()
l = [a, b, c]
c = 0
for x in range(len(l)-1):
    for y in range(x+1, len(l)):
        if l[x] == n:
            c += 1
            break
        if int(l[x]) + int(l[y]) == int(n):
            c += 1
print(c)

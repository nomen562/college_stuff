# 1 + (1+2) + (1+2+3) + (1+2+3+4)
s = 0
c = 0
for x in range(1, int(input(">"))+1):
    s += x
    c += s
print(c)

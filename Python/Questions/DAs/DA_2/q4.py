# Get the input data from the user and form 3X3 matrix [A]. Find the
# inverse of the matrix [A] and prove [A][A-1]=[I]

# A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
A = [[2, 0, -1], [5, 1, 0], [0, 1, 3]]
co_fac = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
adj = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
inv = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
l = [0, 1, 2]*3
det = 0
# # Taking input from the user
# for r in range(3):
#     for c in range(3):
#         A[r][c] = int(input(f"Enter A[{r}][{c}] element>"))
print(f"Matrix A is>{A}")
# Forming Cofactor Matrix
index = 1
for r in range(3):
    index = 1
    for c in range(3):
        co_fac[r][c] = (A[l[r+index]][l[c+index]] *
                        A[l[r+index+1]][l[c+index+1]]) - (A[l[r+index]][l[c+index+1]]*A[l[r+index+1]][l[c+index]])
    det += A[r][c]*(co_fac[r][c])
    index += 1
print(f"det>{det}")
print(f"Cofactor matrix is>{co_fac}")
# Forming the adjoint of the matrix
for r in range(3):
    for c in range(3):
        adj[r][c] = co_fac[c][r]
print(f"Adjoint is>{adj}")
for r in range(3):
    for c in range(3):
        inv[r][c] = adj[r][c]/det
print(f"Inverse of the matrix is>{inv}")
# A X A-1 = I
AXB = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
for r in range(3):
    for c in range(3):
        for k in range(3):
            AXB[r][c] += A[r][k]*inv[k][c]


print(f"AXB>{AXB}")
print("Since A X A(-1)=I, Hence Proved")

# A computer game to ascend a building with a specified number of floors. You have three different facilities for each floor to reach the top: the elevator(1), the escalator(2), and walking up the stairs(3). Each facility has its own scoring rule. Assume the initial score is zero.

# • Elevator(1): Score increments to the next even number.

# • Escalator(2): Score increments to the next odd number.

# • Walk (3): Score increments to the next prime number.

# Write an algorithm and python code to display the score to ascend a building.

# Example: If number of floors 4 and person chosen 3 for first floor, 2 for second floor, 3 for third floor and 2 for fourth floor. The score is 2(first prime number) +1(first odd number) +3(next prime number) +3(next odd number) =9.

# Input & Output format

# Inputs

# Number of floors (n)

# Enter facility number (1 or 2 or 3 ntimes)

# Output

# Score
n = int(input("Enter no of floors>"))
f = [0]*n
t = 2
e = 0
o = 1
for i in range(n):
    f[i] = int(input(f"Enter facility for {i+1} floor>"))


def next_prime(t, n):
    c = 0
    for i in range(t, n+1):
        for x in range(1, i+1):
            if i % x == 0:
                c += 1
        if c == 2:
            return i


s = 0
for i in f:
    if i == 1:
        s += e
        e += 2
    if i == 2:
        s += o
        o += 2
    if i == 3:
        s += next_prime(t, n)
        t += 1
print(s)

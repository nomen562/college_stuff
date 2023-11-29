def main():
    n = int(input("Enter your number>"))
    f = 1
    s = 0
    while n != 1:
        if n % f == 0 and f % 2 != 0 and f != 1:
            s += f
            n /= f
        else:
            f += 1
            if f == n:
                break
    kk = (f"The sum of odd factors are>{s+1}")
    return kk
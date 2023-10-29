# Write a python code to get the coefficients of a quadratic equation
# from the user and find the roots of the quadratic equation.

r1 = int(input("Enter the first root>"))
r2 = int(input("Enter the second root>"))
s, p = r1 + r2, r1*r2
sign1 = ' - ' if s >= 0 else ' + '
sign2 = ' + ' if p >= 0 else ' - '
print(f"x^2{sign1}{abs(s)}x{sign2}{abs(p)} = 0")

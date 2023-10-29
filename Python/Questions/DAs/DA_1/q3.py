# X1, X2 and X3 are the roots of a cubic equation. Write a python code
# to print the cubic equation.
x1, x2, x3 = int(input("Enter first root>")), int(
    input("Enter second root>")), int(input("Enter third root>"))
sumk = x1 + x2 + x3
sum_r = x1*x2 + x2*x3 + x3*x1
pro = x1 * x2 * x3
sign1 = " - " if sumk >= 0 else " + "
sign2 = " + " if sum_r >= 0 else " - "
sign3 = " - " if pro >= 0 else " + "
print(f"x^3{sign1}{abs(sumk)}x^2{sign2}{abs(sum_r)}x{sign3}{abs(pro)} = 0")

'''
Write a python program to the find simple interest and compound
interest
'''

p, r, t, n = int(input("Enter principal amount>")), int(
    input("Enter rate of interest>")), int(input("Enter number of years>")), int(input("Enter number of times interest is charged per year>"))

print(
    f"Simple Interest is> {p*r*t/100}\nCompound Interest is> {(p*((1 + (r/(n*100)))**(n*t)))-p}")

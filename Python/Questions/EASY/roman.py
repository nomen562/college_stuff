# Convert the given year into roman equivalent. Roman equivalents are M:1000, D:500, C:100, L:50, X:10, V:5, I:1.

# Example: Input number : 4565(1000+1000+1000+1000+500+50+10+5)=MMMMDLXV

# Sample Input/ Output Format

# Input: Enter any number

# Output: Equivalent roman number

n = int(input("Enter your number>"))
no_of_dig = len(str(n))

before_thousands = 'M'*((n//1000))
n = str(n)[no_of_dig-3:]
roman = ""

l = [('C', 'D', 'M'), ('X', 'L', 'C'), ('I', 'V', 'X')]


def convert(i, f):
    if f <= 3:
        return f*l[i][0]
    if f == 4:
        return (l[i][0] + l[i][1])
    if f == 0:
        return ''
    if f == 9:
        return (l[i][0]+l[i][2])
    if f == 5:
        return (l[i][1])
    else:
        return l[i][1] + (f-5)*l[i][0]


i = 3 - len(str(n))

print(n)
while i < 3:
    f_dig = int(str(n)[i])
    roman = roman + convert(i, f_dig)
    i += 1

roman = before_thousands + roman

print(roman)

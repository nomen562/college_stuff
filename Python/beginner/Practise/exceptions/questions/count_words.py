s = input("Enter your sentence>")
s += ' '
dick = {}
word = ''
for letter in s:
    if letter == ' ':
        if word not in dick:
            dick[word] = 1
        else:
            dick[word] += 1
        word = ''
        continue
    word += letter
print(dick)

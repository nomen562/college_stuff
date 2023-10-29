word = input("Enter your word>")
wd = ''
vowels = ['a', 'e', 'i', 'o', 'u']


def is_vowel(word):
    is_vowe = False
    for x in word:
        if x in vowels:
            return True
    return is_vowe


def count_vowel(word):
    c = 0
    for x in word:
        if x in vowels:
            c += 1
    return c


c = 0
for index in range(len(word)):
    wd = ''
    for j in range(index, len(word)):
        wd += word[j]
        if is_vowel(wd):
            print(wd)
            c += 1
print(c)

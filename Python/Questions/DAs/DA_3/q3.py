import re
s = input("Enter you sentence>")


def is_dup(word):
    word = r"\b" + word + r"\b"
    l = re.findall(word, s)
    return len(l) > 1 

pattern = r"\b[A-Za-z]+\b"
words = re.findall(pattern, s)
# finding only the duplicated elements
dup_words = []
seen_words = []
for word in words:
    if word not in seen_words:
        seen_words.append(word)
    else:
        if word not in dup_words:
            dup_words.append(word)
print(dup_words)
for word in dup_words:
    print(word+" ", end='')
    word_n = r"\b"+word+r"\b"
    while re.search(word_n, s):
        print(re.search(word_n, s).span(), end=' ')
        s = re.sub(word_n, '', s, 1)
    print()

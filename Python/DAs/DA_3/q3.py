import re
s = input("Enter your sentence>")
# def index_count:


def dup_rem(word, lis):
    for x in range(len(lis)-3):
        if lis[x] == word:
            lis.pop(x)
    return lis


def word_remover(word):
    sen = s
    pattern = r"\b"+word+r"\b"
    sen = re.sub(pattern, x, sen, 1)
    return sen


def pos_finder(word):
    sen = s
    t = []
    while re.search("\\b"+f"{word}"+"\\b", sen):
        match = re.search("\\b"+f"{word}"+"\\b", sen)
        t.append(match.span())
        sen = re.sub("\\b"+f"{word}"+"\\b", '', sen, 1)
    return t


list_of_words = re.findall(r"\b\w+\b", s)
for word in list_of_words:
    x = re.findall("\\b"+f"{word}"+"\\b", s)
    if len(x) > 1:
        print(f"{word} repeated {len(x)} times. Positions are {pos_finder(word)}")
        list_of_words = dup_rem(word, list_of_words)
        re.sub(f"{word}", '', s)

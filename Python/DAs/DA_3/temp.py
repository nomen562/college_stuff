# import re
# s = input("Enter your sentence>")
# # def index_count:


# def word_remover(word):
#     sen = s
#     pattern = r"\b"+word+r"\b"
#     sen = re.sub(pattern, '', sen, 1)
#     return sen


# print(word_remover('sorry'))

def dup_rem(word, lis):
    for x in range(4):
        if lis[x] == word:
            lis.pop(x)
    return lis


print(dup_rem('hello', ['hello', 'are', 'you', 'hello']))

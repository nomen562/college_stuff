# s = input("Enter your sentence>")
# key = int(input("Enter your key>"))
# l = []
# encoded = ''
# for x in range(ord('a'), ord("z")+1):
#     l.append(chr(x))

# l *= 1 + (26+key)//26

# for letter in s:
#     encoded += l[l.index(letter)+key]
# print(decoded)

# Method 2
s = input("Enter your sentence>")
key = int(input("Enter your key>"))
encoded = ''
for x in s:
    if x.islower():
        factor = (26*((ord(x)+key)//122))
        encoded += chr(ord(x) + key - factor)
print(encoded)

from pprint import pprint
sentence = "Hello How are youguys the quick browwn fox jumps over the lazy dog"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1)
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda x: x[1], reverse=True)
print(char_frequency_sorted[0])

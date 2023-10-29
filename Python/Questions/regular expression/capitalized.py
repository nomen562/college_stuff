# Match and extract all words that start with a capital letter from a given text.
import re

text = "This is a AbcSample2 text with Some Capitalized Words."
pattern = r"[A-Z]\w*"
matches = re.findall(pattern, text)
print(matches)

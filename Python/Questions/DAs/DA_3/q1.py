import re
s = input("Enter your sentence>")
pattern_v = r"\b[AEIOUaeiou]\w*\b" # Finding words starting with vowel
pattern_c = r"\b[^AEIOUaeiou ]\w*\b" # Finding words starting with constant
l1 = re.findall(pattern_v, s)
l2 = re.findall(pattern_c, s)
print("Vowel list:", l1)
print("Consonant list:", l2)

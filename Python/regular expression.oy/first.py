import re
# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
# user_input = input("Enter input>")
# if re.search(pattern, user_input):
#     print("Valid email")
# else:
#     print("Invalid Email")
# import re
# text = "The price is   $1599"
# pattern = "\d{-2}"
# print(re.findall(pattern, text))
text = "1234"
pattern = r"[\d*]"  # ^ matches the start of a string
if re.search(pattern, text):  # returns a match object
    print("Match found!")
print((re.search(pattern, text)))

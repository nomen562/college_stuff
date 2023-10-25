import re
text = "Contact us at email@example.com or support@my-website.co"
pattern = r"[\w-]+@[\w-]+\.\w+"
print(re.findall(pattern, text))

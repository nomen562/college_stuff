import re
text = "<html><head><title>Sample Page</title></head><body><h1>Hello, World!</h1></body></html>"
pattern = r"<.*?>"
print(re.findall(pattern, text))

import re
d = '2*sec^2(x)*tan(x)'

terms = re.findall(r"\b[a-z]+\^?\d?\(x\)|\d+\b", d)
print(terms)

# Match and extract all dates in the format "dd/mm/yyyy" from a given text.
import re
text = "Here are some important dates: 01/12/2022 and 15/05/2023."
pattern = r"\d{2}/\d{2}/\d{4}"
print(re.findall(pattern, text))

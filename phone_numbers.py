# Match and extract all phone numbers in the format "(123) 456-7890" or "123-456-7890" from a given text.
import re
text = "Contact us at (123) 456-7890 or 555-555-5555."
pattern = r"(\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{3}-\d{4})"
matches = re.findall(pattern, text)

print(matches)

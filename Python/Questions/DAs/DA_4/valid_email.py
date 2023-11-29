# def main():
#     import re
#     text = input("Enter maybe email>")
#     pattern = r"[\w-]+@[\w-]+\.\w+"
#     print(re.findall(pattern, text))
import re

def is_valid_email(email):
    # Define the regular expression for a valid email address
    pattern = r'[\w-]+@[\w-]+\.\w+'

    # Use re.match to search for the pattern at the beginning of the string
    match = re.match(pattern, email)

    # If a match is found and it spans the whole string, then it's a valid email
    return match is not None and match.span()[1] == len(email)

def main():
    # Example usage within a single function
    email_input = input("Enter an email address: ")

    if is_valid_email(email_input):
        return (f"{email_input} is a valid email address.")
    else:
        return (f"{email_input} is not a valid email address.")


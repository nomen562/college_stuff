# Get a floating-point number from the user
try:
    number = float(input("Enter a floating-point number: "))
except ValueError:
    print("Invalid input. Please enter a valid floating-point number.")
    exit(1)

# Get the absolute value of the number
number = abs(number)

# Initialize variables to count digits
num_digits_whole = 0
num_digits_fractional = 0

# Calculate the number of digits in the whole part
whole_part = int(number)
while whole_part > 0:
    whole_part //= 10
    num_digits_whole += 1

# Calculate the number of digits in the fractional part
fractional_part = number - int(number)
epsilon = 1e-9  # A small value to handle precision issues
while fractional_part > epsilon:
    fractional_part *= 10
    num_digits_fractional += 1

# Print the results
print(f"Number of digits in whole part: {num_digits_whole}")
print(f"Number of digits in fractional part: {num_digits_fractional}")

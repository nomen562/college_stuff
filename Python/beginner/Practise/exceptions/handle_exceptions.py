# Handling Value error exception
try:
    with open(first.py) as file:
        file.__exit__
    age = int(input("Enter a number>"))
    xfactor = 10 / age
# except ValueError as exx:
#     print("You didnt eneter a valid age")
#     print(exx)
#     print(type(exx))
# except ZeroDivisionError:
#     print("You didnt eneter a valid age")
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
except ZeroDivisionError:
    # Only code in first except blockk was executed
    # Other excpt clauses were ignored whenever one matches it goes into that and ignores the others
    print("You didnt eneter a valid age")
else:
    print("No exceptions were throen")
    # Optional only executes if no exception is found
finally:
    print(2)
    # This clause is always executed wheather an exception was thrown or not
    # It is used to free up resources
print("Exection continues")

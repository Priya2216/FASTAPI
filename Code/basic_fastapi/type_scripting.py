# def add(firstName: str | list[int], lastName: str):
#     if isinstance(firstName, str):
#         firstName = firstName.capitalize()
#     return firstName + "   " + lastName

# fname = "priya"
# lname = "Raut"

# name = add(fname, lname)
# print(name)


# # ========

def add(firstName: str | list[int], lastName: str) -> str:
    if isinstance(firstName, str):
        firstName = firstName.capitalize()
    elif isinstance(firstName, list):
        # Convert list of ints to string, e.g., [1, 2, 3] -> '1 2 3'
        firstName = ' '.join(map(str, firstName))
    else:
        raise TypeError("firstName must be a string or list of integers")

    return firstName + "   " + lastName

# Example 1: With string
fname1 = "priya"
lname1 = "Raut"
print(add(fname1, lname1))  # Output: Priya   Raut

# Example 2: With list of integers
fname2 = [1, 2, 3]
lname2 = "Numbers"
print(add(fname2, lname2))  # Output: 1 2 3   Numbers

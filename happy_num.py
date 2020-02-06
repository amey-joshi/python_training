#!/usr/bin/python3

def get_digits(n):
    """Returns the digits in the argument as a list."""

    if type(n) != type(1):
        raise ValueError(f"{n} is not an integer")

    if n < 0:
        n = -n

    digits = []
    while n%10 != n:
        digits.append(n%10)
        n = n // 10

    digits.append(n)

    return digits

def is_happy(n):
    """Checks if an integer is a happy number. If the integer is negative, its absolute
       value is considered.

       ValueError is raised if the argument is not an integer."""

    ss = [] # Sum of squares of digits
    n = sum([d**2 for d in get_digits(n)])
    ss.append(n)

    result = True
    while n != 1:
        n = sum([d**2 for d in get_digits(n)])

        if n in ss:
            result = False
            break
        else:
            ss.append(n)

    return result

for n in range(1, 50):
    if is_happy(n):
        print(f"{n} is a happy number.")
    else:
        print(f"{n} is not a happy number.")


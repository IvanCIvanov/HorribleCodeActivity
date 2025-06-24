# Calculator Project - Violated Practice Version
# Group Members - Carter Meadows, Aidan Oback

# Practices Violated: Documentation, KISS, DRY, and Single Responsibility

# KISS is violated in the calculator functions by not keeping the code simple and
# repeating lines that could be condensed.
#
# Single Responsibility is violated by the functions each doing multiple tasks,
# such as taking inputs, type casting the inputs, and then performing the calculation.
#
# Documentation is violated by the lack of comments and unclear names of each function.

def function1():
    a = input("Please enter a number: ")
    b = input("Please enter a number: ")
    a = int(a)
    b = int(b)
    final = a + b
    return final

def function2():
    a = input("Please enter a number: ")
    b = input("Please enter a number: ")
    a = int(a)
    b = int(b)
    final = a - b
    return final

def function3():
    a = input("Please enter a number: ")
    b = input("Please enter a number: ")
    a = int(a)
    b = int(b)
    final = a * b
    return final


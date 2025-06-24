# Calculator Project - Proper Practice Version
# Group Members - Ivan Ivanov, Grishma Howale

# Practices Displayed: Documentation, KISS, DRY, and Single Responsibility
#
# KISS Principle is being used by using a switch case, and the print statements
# immediately jump into the functions without an extra line for variables.
#
# Single Responsibility is being used by splitting the project into multiple functions which do one
# task each. Main prompts the user and displays their outcome, the rest of the project is split up.
#
# DRY (Don't Repeat Yourself) is being displayed here by grabbing user input once, and using a loop instead
# of repeating the prompt over and over. Each line here is required with no additional lines.


def user_input():
    x = int(input("Please enter a number: "))
    return x

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b



def main():
    print("Please select an option:\n")
    print("1. Addition\n")
    print("2. Subtraction\n")
    print("3. Multiplication\n")
    option = int(input("Enter your option: "))
    a = user_input()
    b = user_input()
    if option == 1:
        print(f"Answer: {addition(a, b)}")
    if option == 2:
        print(f"Answer: {subtraction(a, b)}")
    if option == 3:
        print(f"Answer: {multiplication(a, b)}")

running = True
while running:
    main()
    running = bool(input("\nDo you want to continue? (y/n): "))

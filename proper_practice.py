# Calculator Project - Proper Practice Version
# Group Members - Ivan Ivanov, Grishma Howale

# Practices Displayed: Documentation, KISS, DRY, and Single Responsibility

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

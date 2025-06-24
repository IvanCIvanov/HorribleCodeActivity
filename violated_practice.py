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
#
# DRY (Don't Repeat Yourself) is being violated here by grabbing user input multiple times,
# repeating the prompt over and over.

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

def main():
    print("Enter 1 for addition, 2 for subtraction, 3 for multiplication:")
    thing1 = input("Enter your option: ")
    if thing1 == "1":
        thing4 = function1()
        print("Your answer is: " + str(thing4))
        thing2 = input("Do you want to enter an additional number? (y/n): ")
        if thing2 == "y":
            main()
        elif thing2 == "n":
            print("Okay, goodbye!")
        else:
            print("Goodbye!")
    elif thing1 == "2":
        thing5 = function2()
        print("Your answer is: " + str(thing5))
        thing2 = input("Do you want to enter an additional number? (y/n): ")
        if thing2 == "y":
            main()
        elif thing2 == "n":
            print("Okay, goodbye!")
        else:
            print("Goodbye!")
    elif thing1 == "3":
        thing3 = function3()
        print("Your answer is: " + str(thing3))
        thing2 = input("Do you want to enter an additional number? (y/n): ")
        if thing2 == "y":
            main()
        elif thing2 == "n":
            print("Okay, goodbye!")
        else:
            print("Goodbye!")
    else:
        main()
if __name__ == "__main__":
    main()
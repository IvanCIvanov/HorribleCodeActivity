# Calculator Project - Violated Practice Version
# Group Members - Carter Meadows, Aidan Oback
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
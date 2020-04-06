import sys
import keyboard

intro = 0
cor_op = 0
proceed = 0
num1 = None
num2 = None
operator = None

while intro < 1:

    print("Welcome to Deano's second calculator, a slightly improved version from the previous")
    print("")
    print(input("Press ENTER to continue..."))
    print("")
    not_robot = float(input("To check you're not a robot,\nwhat is 5+5?: "))

    if not_robot == 10:
        print("")
        print("")
        print("You may proceed! :)")
        print("")
        print("")
        break
    else:
        print("You have failed the human test.\nExiting calculator...\n...\n...")
        sys.exit()

while cor_op < 1:
    print("")
    print("")
    proceed = input("Would you like to continue? (y/n): ")
    if proceed == "y":
        num1 = float(input("Enter your first number: "))
        operator = (input("Enter your operator (+, -, *, /): "))
        num2 = float(input("Enter your second number: "))

        if operator == "+":
            print()
            print(num1 + num2)
            print("")
            print("")
            print("")

        elif operator == "-":
            print()
            print(num1 - num2)
            print("")
            print("")
            print("")
        elif operator == "*":
            print()
            print(num1 * num2)
            print("")
            print("")
            print("")
        elif operator == "/":
            print()
            print(num1 / num2)
            print("")
            print("")
            print("")
        elif operator != "+-/*":
            print()
            print("Please re-enter your numbers, when prompted use an operator please use +, -, / or *. Thank you.")
            print("")
            print("")
            print("")

    if proceed == "n":
        print("Thank you for using Deano's awesome calculator.")
        break



















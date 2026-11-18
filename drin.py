print("==========================================")
print("========= PYTHON TUTORIAL PROGRAM ======")
print("==========================================")


def introduction():
    print("\n================================")
    print("     INTRODUCTION TO PROGRAMMING")
    print("================================")

    print("\nWhat is Programming?")
    print("Programming is the process of making")
    print("guidelines to a computer.")

    print("\nWhat is Python?")
    print("Python is a popular programming language.")

    print("\nExample of Python Programming:")
    print("Hello, World!")

    print("\nOutput:")
    print("Hello, World!")


def basic_syntax():
    print("\n================================")
    print("        PYTHON BASIC SYNTAX")
    print("================================")

    print("\nWhat is Syntax?")
    print("Syntax refers to the rules of writing")
    print("a correct Python program.")

    print("\nExample 1: Print Statement")
    print("Hi Python")

    print("\nVariables")
    print('name = "Aldrin"')
    print("age = 18")

    print("\nIndentation")
    print("if age >= 18:")
    print("Adult")


def printing_output():
    print("\n================================")
    print("          PRINTING OUTPUT")
    print("================================")

    print("\nThe print() function displays information")
    print("on the screen.")

    print("\nExample 1:")
    print("Hello Ccst")

    print("\nOutput:")
    print("Hello Ccst")

    print("\nExample 2:")
    print("My name is Aldrin")
    print("18")

    print("\nOutput:")
    print("My name is Aldrin")
    print("18")


def python_comments():
    print("\n================================")
    print("          PYTHON COMMENTS")
    print("================================")

    print("\nComments are ignored by python")
    print("they are use to explain the code.")

    print("\nSingle-line Comment")
    print("# This is a comment")
    print("Hello")

    print("\nMultiple-line Comment")
    print("This is a")
    print("multiple-line comment")

    print("\nComments help programmers really understand")
    print("and arranged their code.")


def variables_constants():
    print("\n================================")
    print(" VARIABLES, CONSTANTS AND DATA TYPES")
    print("================================")

    print("\nWhat is a Variable?")
    print(" storage location used to keep data in a program.")

    name = "Aldrin"
    age = 18

    print("\nExample:")
    print('name = "Aldrin"')
    print("age = 18")

    print("\nOutput:")
    print("Name:", name)
    print("Age:", age)

    print("\nWhat is a Constant?")
    print("A constant is a value intended to remain unchanged.")
    print("Python programmers commonly use uppercase names.")

    SCHOOL = "MNHS"
    print("SCHOOL =", SCHOOL)

    print("\nCommon Data Types:")
    print("String - Text")
    print("Integer - Whole numbers")
    print("Float - Decimal numbers")
    print("Boolean - True or False")


def basic_data_types():
    print("\n================================")
    print("       BASIC DATA TYPES")
    print("================================")

    name = "Aldrin"
    age = 18
    grade = 90.5
    is_student = True

    print("\n1. STRING (str)")
    print(" text.")
    print("Example:", name)

    print("\n2. INTEGER (int)")
    print("whole numbers.")
    print("Example:", age)

    print("\n3. FLOAT (float)")
    print("decimal numbers.")
    print("Example:", grade)

    print("\n4. BOOLEAN (bool)")
    print("True or False values.")
    print("Example:", is_student)

    print("\nChecking Data Types:")
    print(name)
    print(age)
    print(grade)
    print(is_student)


def arithmetic_operators():
    print("\n================================")
    print("   ARITHMETIC OPERATORS")
    print("================================")

    print("\nAre symbols used to perform mathematical calculations on number.")

    a = 20
    b = 10

    print("\nExample:")
    print("a = 20")
    print("b = 10")

    print("Addition (+):", a + b)
    print("Subtraction (-):", a - b)
    print("Multiplication (*):", a * b)
    print("Division (/):", a / b)
    print("Floor Division (//):", a // b)
    print("Modulus (%):", a % b)
    print("Exponent (*):", a * b)

    print("\nthey work the same way as the operators")


def Basic_input_and_output():
    print("\n================================")
    print("      BASIC INPUT AND OUTPUT")
    print("================================")

    print("\nThe input() function allows users")
    print("to enter information.")

    print("\nProgram:")

    name = input("\nEnter your name: ")
    print("Hello, " + name + "! Nice to meet you!")

    age = int(input("\nEnter your age: "))
    print("You are", age, "years old.")


def Conditional_statement_in_python():
    print("\n============================")
    print(" CONDITIONAL STATEMENT IN PYTHON")
    print("==============================")

    print("\nWHAT IS CONDITIONAL STATEMENT?")

    print("\nA conditional statement allows a program to")
    print("\nmake decisions based on whether a condition")
    print("\nis True or False")


age = int(input("Enter your age: "))

if age >= 18:
    print("you are adult")
print("finished!")

number = int(input("Enter your number: "))

if number >= 15:
    print("the number is 15 or greater")
else:
    print("the number is less than 15")

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Excellent")
elif grade >= 85:
    print("Very Good!")
elif grade >= 75:
    print("Passed!")
else:
    print("Failed!")


def Logical_operator():
    print("\n============================")
    print(" LOGICAL OPERATOR")
    print("==============================")

    print("\nWHAT IS LOGICAL OPERATOR?")

    print("\nAre used to combine or reverse condition")
    print("\nIn a python program")


print("\n1.AND OPERATOR")
age = 18
has_id = True

print("Age:", age)
print("Has_id:", has_id)
print("enter:", age >= 18 and has_id)

print("\n2.OR OPERATOR")
grade = 90
attendance = 95

print("Grade:", grade)
print("attendance:", attendance)
print("Passed:", grade >= 80 or attendance >= 90)

print("\n3.NOT OPERATOR")
its_raining = False

print("it's raining:", its_raining)
print("it's not raining:", not its_raining)


def Introduction_to_iteration_and_loops():
    print("=" * 40)
    print("\nWHAT IS ITERATION AND LOOP?")
    print("\nRepeating process in programming.")

    print("\n1. For loop")
    print("2. while loop")
    print("3. back to main menu")


choice = input("Enter your choice: ")

if choice == "1":
    print("\nFor loop")
    for number in range(1, 11):
        print(number)

elif choice == "2":
    print("\nWHILE LOOP")
    count = 1
    while count <= 20:
        print(count)
        count += 1

elif choice == "3":
    print("Back to the menu")

else:
    print("Invalid code!")

while True:
    print("\n================================")
    print("          MAIN MENU")
    print("================================")
    print("1. Introduction to Programming")
    print("2. Python Basic Syntax")
    print("3. Printing Output")
    print("4. Python Comments")
    print("5. Variables, Constants and Data Types")
    print("6. Basic Data Types")
    print("7. Arithmetic Operators")
    print("8. Basic input and output")
    print("9. Conditional statement in python")
    print("10. Logical operator")
    print("11. Introduction to iteration and loops")
    print("12. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        introduction()

        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What is programming?")
                print("A. Making guidelines for a computer \nB. To coding \nC. To promote computer \nD. Playing games")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. What is python?")
                print("A. Computer  \nB. Videos \nC. Programming language \nD. Word")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

    elif choice == "2":
        basic_syntax()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What is syntax?")
                print("A. Rules of  correct grammar \nB. Wrong grammar\nC. Change the word\nD. To Input word")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. Identify the correct variable")
                print("A. name = Aldrin \nB. grade == 91.5 \nC. gra-de = 27.5\nD. 2Name = Aldrin")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue
    elif choice == "3":
        printing_output()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What function is used to display information on the screen?")
                print("A. Input \nB. Print \nC. Int \nD. Syntax")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score  + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. What will print('Hello') display?")
                print("A. Hello \nB. print \nC. Error \nD. Nothing")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score  + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue
    elif choice == "4":
        python_comments()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What are comments used for in Python?")
                print("A. To code the number \nB. To input \nC. Output \nD. To repeat instructions")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("22. Which symbol is used for a single-line comment?")
                print("A. @ \nB. # \nC. $ \nD. //")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue
    elif choice == "5":
        variables_constants()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What is a variable?")
                print("A. A storage location for data \nB. A computer need to explain \nC. A programming correct grammar \nD. To comment in computer")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. Which of the following is an example of a variable?")
                print("A. age = 18 \nB. # Hello \nC. print() \nD. if")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

    elif choice == "6":
        basic_data_types()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. Which data type is used for text?")
                print("A. Integer \nB. String \nC. Float \nD. Boolean")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. Which data type is used for whole numbers?")
                print("A. bool \nB. float \nC. str \nD. int")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score + 1
                        print("Great job! You've got the correct answer!")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

    elif choice == "7":
        arithmetic_operators()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What operator is used for multiplication?")
                print("A. - \nB. * \nC. / \nD. **")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. What is the result of 20  + 10?")
                print("A. 30 \nB. 20 \nC. 150 \nD. 10")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

    elif choice == "8":
        Basic_input_and_output
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What function allows users to enter information?")
                print("A. print \nB. Int \nC. Input \nD. Word")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. What function displays information on the screen?")
                print("A. input \nB. Boolean \nC. print \nD. range")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

    elif choice == "9":
        Conditional_statement_in_python()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What is the purpose of a conditional statement?")
                print("A. repeat instructions \nB. make decisions \nC. display pictures \nD. store information")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. Which keyword is used to check a condition?")
                print("A. if \nB. Input \nC. Output \nD. def")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

    elif choice == "10":
        Logical_operator()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What are logical operators used for?")
                print("A. To combine or reverse conditions \nB. To print information \nC. To compute the numbers \nD. To comment")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. Which operator returns False when both conditions are False?")
                print("A. NOT  \nB. OR \nC. AND \nD. IF")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue
    elif choice == "11":
        Introduction_to_iteration_and_loops()
        while True:
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What is iteration in programming?")
                print("A. Repeating a process \nB. Deleting a picture \nC. Variable \nD. print the comment")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score
                        print("Oops! That's not the correct answer.")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")

                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("Which keyword is used to create a while loop?")
                print("A. for  \nB. if \nC. while \nD. Not")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "b":
                        score = score
                        print("Oops! That's not the correct answer.")
                    elif answer == "c":
                        score = score + 1
                        print("Great job! You've got the correct answer!")
                    else:
                        score = score
                        print("Oops! That's not the correct answer.")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue
    elif choice == "12":
        print("Thank you for making  Python Tutorial!")
        break
    else:
        print("Invalid code!")
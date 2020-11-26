# Author: Gaurang Ruparelia
# Assignment #2 - Calculator
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


def main():
    """Runs a program for performing basic arithmetic
    operations between two numbers
    """

    run_calculator()

def run_calculator():
    """Runs the calculator as a repeated sequence of
    displaying the calculator menu and performing a
    calculation based on the user's choice.

    :return: None
    """
    print("Welcome to the CS 1114 Calculator!")


    run_condition= True
    while run_condition == True:

        print_menu()
        option_chosen_by_user = do_calculation()

        if option_chosen_by_user == "q":
            print()
            print("Goodbye.")
            run_condition = False





    # call run_calculator() here and remove pass below
def print_menu():
    """Prints available calculator
    operations.

    :return: None"""

    print()
    print("1) Perform addition")
    print("2) Perform subtraction")
    print("3) Perform multiplication")
    print("4) Perform division")

def do_calculation():
    """Prompts user for calculation choice and calls
    function to perform calculation

    :return: the character entered by user
    """


    option= input("Please enter an option (1-4) or 'q' to quit: ")
    if option == "1":
        do_addition()

        return option

    elif option == "2":
        do_subtraction()
        return option

    elif option == "3":
        do_multiplication()
        return option

    elif option == "4":
        do_division()
        return option

    elif option == "q":

            #return option
        return option

    else:
        print()
        print("That was not a valid choice. Try again.")
        return option



def do_addition():
    """Informs user that addition was chosen, sums two
    numbers input by the user, and outputs the result.

    :return: None
    """
    print()
    print("You have chosen the addition operation.")
    first_number= float(input("Enter first number: "))
    second_number= float(input("Enter second number: "))
    add_answer = first_number + second_number

    print("The sum is", " ", add_answer, ".", sep="")

    return None

def do_subtraction():
    """Informs user that subtraction was chosen, calculates
    the difference between two numbers input by the user, and
    outputs the result.

    :return: None
    """
    print()
    print("You have chosen the subtraction operation.")
    first_number= float(input("Enter first number: "))
    second_number= float(input("Enter second number: "))
    subtract_answer = first_number - second_number

    print("The difference is", " ", subtract_answer, ".", sep="")

    return None

def do_multiplication():
    """Informs user that multiplication was chosen, multiplies two
    numbers input by the user, and outputs the result.

    :return: None
    """
    print()
    print("You have chosen the multiplication operation.")
    first_number= float(input("Enter first number: "))
    second_number= float(input("Enter second number: "))
    multiply_answer = first_number * second_number

    print("The product is", " ", multiply_answer, ".", sep="")

    return None

def do_division():
    """Informs user that division was chosen, divides two
    numbers input by the user, and outputs the result.

    :return: None"""
    print()
    print("You have chosen the division operation.")
    first_number= float(input("Enter first number: "))
    second_number= float(input("Enter second number: "))
    division_answer = first_number / second_number

    print("The result of the division of the two numbers is", " ", division_answer, ".", sep="")

    return None

# Welcome to the CS 1114 Calculator!
# 1) Perform addition
# 2) Perform subtraction
# 3) Perform multiplication
# 4) Perform division
# Please enter an option (1-4) or ’q’ to quit: 1
#
# You have chosen the addition operation.
# Enter first number: 3.6
# Enter second number: 4.5
# The sum is 8.1.
#
# 1) Perform addition
# 2) Perform subtraction
# 3) Perform multiplication
# 4) Perform division
# Please enter an option (1-4) or ’q’ to quit: 2
#
# You have chosen the subtraction operation.
# Enter first number: 10.8
# Enter second number: 17.2
# The difference is -6.4.
#
# 1) Perform addition
# 2) Perform subtraction
# 3) Perform multiplication
# 4) Perform division
# Please enter an option (1-4) or ’q’ to quit: 3
#
# You have chosen the multiplication operation.
# Enter first number: 7.3
# Enter second number: 10.1
# The product is 73.73.
#
# 1) Perform addition
# 2) Perform subtraction
# 3) Perform multiplication
# 4) Perform division
# Please enter an option (1-4) or ’q’ to quit: 4
#
# You have chosen the division operation.
# Enter first number: 17
# Enter second number: 20
# The result of the division of the two numbers is 0.85.
#
# 1) Perform addition
# 2) Perform subtraction
# 3) Perform multiplication
# 4) Perform division
# Please enter an option (1-4) or ’q’ to quit: q

# Goodbye.

####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()

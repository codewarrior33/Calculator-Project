# Import the os module to interact with the operating system
import os

# Function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art for a simple logo
logo = """

             CALCULATOR
  |~|~~~~~~~~~~~~~~~~~~~~~~~~~~|~|
  |_|__________________________|_|
  |  __  |  7  |  8  |  9  |  ÷  |
  | |__| |-----|-----|-----|-----|
  |  __  |  4  |  5  |  6  |  ×  |
  | |__| |-----|-----|-----|-----|
  |  __  |  1  |  2  |  3  |  -  |
  | |__| |-----------------|-----|
  |      |  0  |  .  |  =  |  +  |
  |______|-----------------|_____|

"""
# Display the logo
print(logo)

# Define arithmetic functions

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Dictionary to map symbols to corresponding arithmetic functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Get the first number from the user
num1 = int(input("Enter first number: "))

# Display available arithmetic symbols
for symbol in operations:
    print(symbol)

# Initialize a loop for continuous calculations
should_continue = True
while should_continue:
    # Get the arithmetic symbol from the user
    select_operation = input("Select an operand from the symbol list: ")
    # Get the second number from the user
    num2 = int(input("Enter second number: "))
    # Retrieve the corresponding arithmetic function based on the selected symbol
    calculation_function = operations[select_operation]
    # Perform the calculation
    answer = calculation_function(num1, num2)

    # Display the result
    print(f"{num1} {select_operation} {num2} = {answer}")

    # Check if the user wants to continue or exit
    operate_again = input("Type 'y' to continue or 'n' to exit: ")
    if operate_again == "y":
        # Clear the screen and update the current result for the next iteration
        clear_screen()
        num1 = answer
        print(f"current result: {num1}")
    elif operate_again == "n":
        # Exit the loop if the user chooses to stop
        should_continue = False
        break

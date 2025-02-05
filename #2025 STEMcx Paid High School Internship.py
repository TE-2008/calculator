#2025 STEMcx Paid High School Internship calculator codeApplication
#  Testmony Efunbajo
# start:01/19/2025- end:02/02/2025
# Internship Application for 2025 STEMcx Paid High School Internship Application - Cybersecurity and Coding

# Code Instuctons:Write a program using Python or another programming language of your choice that functions 
# as a calculator. The program should prompt the user to input two numbers and choose an operation. It should 
# then perform the selected operation (addition, subtraction, multiplication, or division) on the two numbers 
# and display the result. Each operation should be implemented in its own function, and these functions should
#  be called from the main program.

# what my program does: It is a calculator program that calulates 2 numbers the user input using operations like
#                       addition (+),subtraction (-),multiplication or division(/) the user chose

# whats in my program:- It askes the user to put in 2 numbers and then choose an operation 
#                     ((+)addition,(-)subtraction,(*) multiplication,(/) division)

#                     - It calculates the 2 numbers by the operation 
#                      ((+)addition,(-)subtraction,(*) multiplication,(/) division)
#                      the user selected and then displays the result.

#                     -Each operation is in its own function, and 
#                     the functions are called from the main program.
#                 
#                     -If the user inputs something that not a number, 
#                      operator or is 0 for number1 or number2 or
#                      operator it will  ask for the user  to put the 
#                      correcct input for  number1 or number2 or
#                      operator.

# This function makes sure that the user only inputs a number to calculate

def get_numbers(only):
    while True:
         try:
            numbers=float(input(only))
            return numbers 
         except ValueError:
             print("please enter a number")

#    This function makes sure that the user only inputs a operator to calculate
def get_operators(only):
    while True:
        operators=input(only)
        if operators in ['+','-','*' ,'/' ,]:
            return operators
        else:
            print("Please enter the operators(+,-,*,/)")

# Functions to add, subtract, multiply and divide the 2 numbers the user inputs
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2==0 or number1==0:
        print("you can't divide by 0")
        return None
    return number1 / number2

continue_calculation = "yes"

while continue_calculation == "yes":
    number1=get_numbers("Enter your 1st number: ")
    number2=get_numbers("Enter your 2nd number: ")

    operators=get_operators("choose a operation (+,-,*,/):")

    if operators== "+":
       result = number1 + number2
       print(f"The result is: {round(result,3)}")
    elif operators== "-":
      result = number1 - number2
      print(f"The result is: {round(result,3)}")
    elif operators== "*":
      result = number1 * number2
      print(f"The result is: {round(result,3)}")
    elif operators== "/":
      
      if number1==0:
          print("you cannot divide by 0")
          number1= get_numbers("please enter any number other than 0 for number 1:")
      while number2==0:
          print("you cannot divide by 0")
          number2= get_numbers("please enter any number other than 0 for number 2:")
      result = number1 / number2
      print(f"The result is: {round(result,3)}")

      continue_calculation = input("Do you want to perform another calculation? Type yes or no:  ").lower()
print("Thanks for using my calculator!")
    







  
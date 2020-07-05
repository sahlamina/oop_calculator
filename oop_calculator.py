# I am importing the functions from my operators file and will use them in my if statements
import operators

# I will try to make this calculator using a class
class Oop_Calculator:
    def calculate(self):

    # these prompts will communicate the instructions to the user
        prompt1 = int(input("Please input your first number "))
        prompt2 = int(input("Please input your second number "))

        # this uses the input function to ask the user to choose an operation
        user_choice = input("Which operation do you want to perform: +, -, /, *, %, ^, cm-in, in-cm ")

        #  this sets the condition for what should happen if the user chooses to add
        if user_choice == "+":
            print(str(prompt1) + " Plus " + str(prompt2) + " is equal to ", operators.addition(prompt1, prompt2))

        #  this sets the condition for what should happen if the user chooses to subtract
        elif user_choice == "-":
            print(str(prompt1) + " Minus " + str(prompt2) + " is equal to ", operators.subtraction(prompt1, prompt2))

        #  this sets the condition for what should happen if the user chooses to divide
        elif user_choice == "/":
            print(str(prompt1) + " Divided by " + str(prompt2) + " is equal to ", operators.division(prompt1, prompt2))

        #  this sets the condition for what should happen if the user chooses to multiply
        elif user_choice == "*":
            print(str(prompt1) + " Multiplied by " + str(prompt2) + " is equal to ", operators.multiply(prompt1, prompt2))

        #  this sets the condition for what should happen if the user chooses to use modulus
        elif user_choice == "%":
            print(str(prompt1) + " Mod " + str(prompt2) + " is equal to ", operators.modulo(prompt1, prompt2))

        #  this sets the condition for what should happen if the user chooses to find the area of a triangle
        elif user_choice == "^":
            print("The area is ", operators.area(prompt1, prompt2))

        # i intended to use this to add the cm/in converter function to my calculator, but the calculator takes two arguments
        # this means that it would work normally for the cm/in calculator because
        # elif user_choice == "in-cm":
        #     print(str(prompt1) + " inch " + " is ", operators.inch_cm(prompt1), "cm")
        #
        # elif user_choice == "cm-in":
        #     print(str(prompt1) + " cm " + " is ", operators.inch_cm(prompt1), " inch")

        else:
            print("Please choose a valid input")



casio = Oop_Calculator()
casio.calculate()
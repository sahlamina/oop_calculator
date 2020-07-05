import operators2

class Calc2:
    def calc(self):

        num1 = int(input("Please enter your first number "))
        num2 = int(input("Please enter your second number "))

        operator = input("Which operation will you like to perform +, -, *, /? ")

        if operator == "+":
            print(str(num1) + " Plus " + str(num2) + " equals ",  operators2.addition(num1, num2))

        elif operator == "-":
            print(str(num1)) + " minus " + str(num2) + " equals ", operators2.subtraction(num1, num2)

        elif operator == "*":
            print(str(num1) + " times " + str(num2) + " equals ", operators2.multiply(num1, num2))

        elif operator == "/":
            print(str(num1) + "divided by " + str(num2) + " equals ", operators2.division(num1, num2))

        else:
            print("Please enter a valid input")

sharp = Calc2()
sharp.calc()



















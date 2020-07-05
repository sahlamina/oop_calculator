# In this file I am creating functions which will be able to carry out basic operations based on two numerical inputs

# operator for addition
def addition(num1, num2):
    return num1 + num2

# operator for subtraction
def subtraction(num1, num2):
    return num1 - num2

# operator for division
def division(num1, num2):
    return num1 / num2

# operator for multiply
def multiply(num1, num2):
    return num1 * num2

# operator for modulo
def modulo(num1, num2):
    if num1 % num2 == "0":
        print("False")
        return num1 % num2
    else:
        print("True")
        return num1 % num2

# instructions for the area of a triangle
def area(num1, num2):
    return num1 * num2 /2

def cm_inch(num1):
    return num1 * 2.54

def inch_cm(num1):
    return num1 * 0.393901

# here i am testing out my functions to see if they work
# print(addition(4,5))
# print(subtraction(30, 14))
# print(division(26, 9))
# print(multiply(7, 3))
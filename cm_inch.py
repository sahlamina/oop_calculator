# i imported all my operations from the operators file
import operators

# i make my inch calculator by creating a class and calculate the method
class Inch_converter():
    def convert(self):

        # i used a similar layout to my actual calculator with the prompts and choices
        prompt1 = int(input("Which number would you like to convert? "))

        user_choice = input("cm-in or in-cm ")

        # if the user chooses to convert inch to cm, i use my imported inch-cm method to carry out the operation
        if user_choice == "in-cm":
            print(str(prompt1) + " inch " + " is ", operators.inch_cm(prompt1), "cm")

        # if the user chooses to convert cm to inch, i use my imported cm-inch method to carry out the operation
        elif user_choice == "cm-in":
            print(str(prompt1) + " cm " + " is ", operators.inch_cm(prompt1), " inch")

        else:
            print("Please enter a valid value")

# conva in an instance of the inch converter class
conva = Inch_converter()
# i am asking conva to perform the convert method which runs through the prompts
conva.convert()
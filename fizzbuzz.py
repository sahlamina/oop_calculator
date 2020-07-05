# i make my fizzbuzz by creating a class and fibu short for fizz buzz the method
class Fizzbuzz:
    def fibu(self):
        # instead of writing the numbers 1-100, i use the range function
        x = range(1, 101)
        # i then use the modulus operator to find numbers in the range that have no remainders when divided by 3 and 5
        for i in x:
            if i % 3 == 0 and i % 5 == 0:
                print(i, "FizzBuzz")

            # this finds the numbers with no remainder when divided by 5
            elif i % 5 == 0:
                print(i,  "Buzz")

            # this finds the numbers with no remainder when divided by 3
            elif i % 3 == 0:
                print(i,  "Fizz")


            else:
                print(i)
# fissbuzz is an instance of the Fizzbuzz class and fibu is a methos
fizzbuzz = Fizzbuzz()
fizzbuzz.fibu()



# I created a class called character tally
class Character_tally:
    # then i made method called string parsing that takes one argument
    def string_parsing(str):
        # i created an empty dictionary
        dict = {}
        # then i used a for loop to iterate through the characters in the string i will later pass in the argument of my
        # string parsing function
        for n in str:
            # find the keys in the empty dictionary
            keys = dict.keys()
            # if a character is found in the string, add 1 one to a tally
            if n in keys:
                dict[n] += 1
            # otherwise, move along one character in the string
            else:
                dict[n] = 1
        return dict
    print(string_parsing("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

tally = Character_tally
tally.string_parsing('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')


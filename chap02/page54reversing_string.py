def str_reverse(input):
    """ A function that returns the passed string in reversed order """
    return input[-1::-1]

while True:
    phrase = input("Enter the phrase that you want reversed(press enter to quit): ")
    if len(phrase) == 0:
        break  # The user wants to quit!  
    else:
        print(str_reverse(phrase) )
print("Thank you ")  

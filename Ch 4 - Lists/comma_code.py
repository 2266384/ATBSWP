spam = ['apples','bananas', 'tofu', 'cats']

def comma_code(myinput):
    global myString                             # Define global variable
    x = 1                                       # Set counter to 1 (second item in our List
    myString = myinput[0]                       # Define myString as first item in List - index 0
    #print(len(myinput)-1)
    for items in myinput[1:]:                   # Loop through items in list starting from second item - index 1
        #print(x)
        if x == len(myinput)-1:                 # Check if counter is equal to the length of our list and append the ', and ' & item strings
            myString += ', and ' + items
        else:                                   # Else just add ', ' and item strings
            myString += ', ' + items
        x += 1                                  # Increment our counter

comma_code(spam)
print(myString)

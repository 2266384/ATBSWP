def collatz(number):
    global myVal
    if number % 2 == 0:
        colval = number // 2
    else:
        colval = 3 * number + 1
    # print(colval)
    myVal = colval

# Run the Collatz sequence
print('Enter an integer value')
while True:
    try:
        myVal = int(input())
        if type(myVal) == int:
            break
    except ValueError:
        print('Value entered is not an integer')

while myVal > 1:
    collatz(myVal)
    print(myVal)

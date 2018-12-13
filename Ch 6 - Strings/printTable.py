tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tablevals):
    i = 0       # integer to store length of longest string in our list of lists
    a = 0       # integer to store the longest list

    for items in tablevals:       # get the length of the longest list
        if len(items) > a:
            a = len(items)

        for item in items:        # get the length of the longest string in our lists
            if len(item) > i:
                i = len(item)

    # go through the list of lists and print all the first items on one line, second items on next line, etc
    for y in range(a):
        for x in range(len(tablevals)):
            if x == len(tablevals)-1:
                print(tablevals[x][y].rjust(i))
            else:
                print(tablevals[x][y].rjust(i), end='')

printTable(tableData)

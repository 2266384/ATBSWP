grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def picture(myList):
    ylen = len(myList)-1                    # Get size of elements in grid list
    xlen = len(myList[0])

    for x in range(0,xlen,1):               # Loop through elements in each list item
        for y in range(ylen,-1,-1):         # Loop through list items in grid list
            if y == 0:                      # If we reach the end of the list add a new line break
                print(grid[y][x])
            else:                           # Else print each element on same line
                print(grid[y][x],end='')


picture(grid)

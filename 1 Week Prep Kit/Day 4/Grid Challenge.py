def gridChallenge(grid):
    # Write your code here
    print(grid)
    for row in range(0, len(grid)):
        #print("orj row:",grid[row])
        grid[row] = "".join(sorted(grid[row]))
        #print("sorted row:",grid[row])

    for i in range(0, len(grid[0])):
        unsorted_column = ""
        for j in range(0, len(grid)):
            unsorted_column += grid[j][i]
        # print("unsorted_column",unsorted_column)
        if unsorted_column == "".join(sorted(unsorted_column)):
            continue
        else:
            return "NO"
    return "YES"

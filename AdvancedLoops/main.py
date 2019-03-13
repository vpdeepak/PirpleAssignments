"""
This is the solution for the Homework #6: Advanced Loops

"""

print("Assignment on Advanced Loops")


def DrawBoard(rows, columns):
    result = False
    if(rows < 70 and columns < 235):
        result = True
        for row in range(rows):
            if(row % 2 == 0):
                for column in range(columns):
                    if(column % 2 == 0):
                        if(column != columns - 1):
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        if(column != columns - 1):
                            print("|", end="")
                        else:
                            print("|")
            else:
                for column in range(columns):
                    if(column != columns - 1):
                        print("-", end="")
                    else:
                        print("-")
    return result

result = DrawBoard(69, 234)

if(result is False):
    print("Playing Board doesn't fit the screen !! Please re-consider rows and column values")



"""
This is the solution for the Project #1: Connect 4

"""

print("Assignment on Connect 4", "\n")

rows = 12
columns = 14
winCount = 4

fieldRowSize = int(rows/2)
fieldColumnSize = int(columns/2)


def DrawBoard(fields):
    for row in range(rows):
        if(row % 2 == 0):
            practicalRow = int(row / 2)
            for column in range(columns):
                if(column % 2 == 0):
                    practicalColumn = int(column / 2)
                    if(column != columns - 1):
                        print(fields[practicalColumn][practicalRow], end="")
                    else:
                        print(fields[practicalColumn][practicalRow])
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


def PlaceEntry(fields, currentColumn, entry):
    succeeded = False
    previousRow = 0
    for currentRow in range(fieldRowSize):
        if(fields[currentColumn][currentRow] == " "):
            if(currentRow == fieldRowSize - 1):
                fields[currentColumn][currentRow] = entry
                succeeded = True
            else:
                previousRow = currentRow
                continue
        else:
            if(fields[currentColumn][previousRow] == " "):
                fields[currentColumn][previousRow] = entry
                succeeded = True
            break
    return succeeded


def IsColumnCompleted(fields, currentColumn, entry):
    success = False
    counter = 0
    for currentRow in range(fieldRowSize):
        if(fields[currentColumn][currentRow] != entry):
            counter = 0
            continue
        else:
            counter += 1
        if(counter >= winCount):
            success = True
            break
    return success


def IsRowCompleted(fields, currentColumn, entry):
    success = False
    for currentRow in range(fieldRowSize):
        if(fields[currentColumn][currentRow] != entry):
            continue
        else:
            # check on left
            leftCounter = 1
            for column in range(currentColumn - 1, -1, -1):
                if(fields[column][currentRow] != entry):
                    break
                else:
                    leftCounter += 1
            # check on right
            rightCounter = 1
            for column in range(currentColumn + 1, fieldColumnSize):
                if(fields[column][currentRow] != entry):
                    break
                else:
                    rightCounter += 1
            break
    if(leftCounter >= winCount or rightCounter >= winCount):
        success = True
    return success


def getLeftBottomDiagonal(fields, column, row):
    counter = 1
    row += 1
    column -= 1
    while(row < fieldRowSize and column >= 0):
        if(fields[column][row] != entry):
            break
        else:
            counter += 1
            row += 1
            column -= 1
    return counter


def getLeftUpDiagonal(fields, column, row):
    counter = 1
    row -= 1
    column -= 1
    while(row >= 0 and column >= 0):
        if(fields[column][row] != entry):
            break
        else:
            counter += 1
            row -= 1
            column -= 1
    return counter


def getRightBottomDiagonal(fields, column, row):
    counter = 1
    row += 1
    column += 1
    while(row < fieldRowSize and column < fieldColumnSize):
        if(fields[column][row] != entry):
            break
        else:
            counter += 1
            row += 1
            column += 1
    return counter


def getRightUpDiagonal(fields, column, row):
    counter = 1
    row -= 1
    column += 1
    while(row >= 0 and column < fieldColumnSize):
        if(fields[column][row] != entry):
            break
        else:
            counter += 1
            row -= 1
            column += 1
    return counter


def IsDiagonalCompleted(fields, currentColumn, entry):
    success = False
    for currentRow in range(fieldRowSize):
        if(fields[currentColumn][currentRow] != entry):
            continue
        else:
            # check left bottom
            leftBottomCounter = getLeftBottomDiagonal(fields, currentColumn,
                                                      currentRow)
            # check left up
            leftUpCounter = getLeftUpDiagonal(
                fields, currentColumn, currentRow)
            # check right bottom
            rightBottomCounter = getRightBottomDiagonal(
                fields, currentColumn, currentRow)
            # check right up
            rightUpCounter = getRightUpDiagonal(
                fields, currentColumn, currentRow)
            break

    if(leftBottomCounter >= winCount or leftUpCounter >= winCount or
       rightBottomCounter >= winCount or rightUpCounter >= winCount):
        success = True

    return success


def HasWon(fields, currentColumn, entry):
    success = False
    # vertical downward check
    if(IsColumnCompleted(fields, currentColumn, entry)):
        success = True
    # horizontal row checks
    elif(IsRowCompleted(fields, currentColumn, entry)):
        success = True
    # diagonal checks
    elif(IsDiagonalCompleted(fields, currentColumn, entry)):
        success = True
    return success


currentFields = []
for column in range(fieldColumnSize):
    currentFields.append([])
    for row in range(fieldRowSize):
        currentFields[column].append(" ")

Player = 1
NumberOfMoves = 1
gameWon = False
while(NumberOfMoves <= (fieldColumnSize * fieldRowSize) and not gameWon):
    DrawBoard(currentFields)
    try:
        currentColumn = int(input(
            "Move {0} : Player {1} : Enter the column to insert : ".
            format(NumberOfMoves, Player)))
    except ValueError:
        continue
    if(currentColumn > fieldColumnSize):
        continue
    if(Player == 1):
        entry = "X"
        nextPlayer = 2
    else:
        entry = "O"
        nextPlayer = 1

    if(PlaceEntry(currentFields, currentColumn - 1, entry)):
        if(not HasWon(currentFields, currentColumn - 1, entry)):
            Player = nextPlayer
            NumberOfMoves += 1
        else:
            gameWon = True

print("\n====== GAME OVER ======")
if(gameWon):
    print("Player {0} : has won the game. \n".format(Player))
else:
    print("It's a DRAW \n")

DrawBoard(currentFields)

"""
This is the solution for the Project #1: Connect 4

"""
print("Assignment on Connect 4" , "\n")

def DrawBoard(fields) :
    rows = 12
    columns = 14
    for row in range(rows) :
        if(row % 2 == 0) :
            practicalRow = int(row / 2)
            for column in range(columns) :
                if(column % 2 == 0) :
                    practicalColumn = int(column / 2)
                    if(column != columns - 1) :
                        print(fields[practicalColumn][practicalRow], end = "")
                    else:
                        print(fields[practicalColumn][practicalRow])
                else :
                    if(column != columns - 1) :
                        print("|", end = "")
                    else:
                        print("|")
        else :
            for column in range(columns) :
                if(column != columns - 1) :
                    print("-", end = "")
                else :
                    print("-")
    return

def checkResult(fields) :
    result = False

    return result

currentFields = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "]]
DrawBoard(currentFields)

nextPlayer = 1
while(True) :
    Player = nextPlayer
    column = int(input("Player {0} : Enter the column to insert : ".format(Player)))
    column -= 1
    rows = currentFields[column]
    if(Player == 1) :
        entry = "X"
        nextPlayer = 2
    else :
        entry = "O"
        nextPlayer = 1

    previousRow = 0
    for row in range(len(rows)) :
        if(currentFields[column][row] == " ") :
            if(row == len(rows) - 1) :
                currentFields[column][row] = entry
            else : 
                previousRow = row
                continue
        else :
            if(currentFields[column][previousRow] == " ") :
                currentFields[column][previousRow] = entry
            else :
                nextPlayer = Player
            break

DrawBoard(currentFields)
print("\n")
"""
This is the solution for the Homework #8: Input and Output (I/O)

"""
import os

print("Assignment on Input and Output (I/O)")


def WriteToFile(fileName, option):
    content = input("Please enter the text to be put to the file " + fileName + " : ")
    with open(fileName, option) as inputFile:
        inputFile.write(content + "\n")
    return


def ReadFile(fileName):
    with open(fileName, "r") as inputFile:
        for line in inputFile:
            print(line)
    return


def DeleteFile(fileName):
    os.remove(fileName)
    return


def ReplaceLine(fileName):
    lineNumber = int(input("Please enter the line number to be replaced : "))
    replacementText = input("Please enter the replacement text : ")
    with open(fileName, "r") as inputFile:
        content = []
        counter = 1
        for line in inputFile:
            if(counter == lineNumber):
                content.append(replacementText + "\n")
            else:
                content.append(line)
            counter += 1
    with open(fileName, "w") as newFile:
        for line in content:
            newFile.write(line)
    return


def DisplayOptions():
    print(" A) Read the file")
    print(" B) Delete the file and start over")
    print(" C) Append the file")
    print(" D) Replace a single line")
    print(" E) Exit")


fileName = input("Please enter the name of the file : ")
if(not os.path.exists(fileName)):
    print("File doesn't exit. Hence creating it.")
    WriteToFile(fileName, "w")
else:
    optionChosen = ""
    while(optionChosen != "E"):
        DisplayOptions()
        optionChosen = input("Please enter the option chosen : ")

        if(optionChosen == "A"):
            ReadFile(fileName)

        elif(optionChosen == "B"):
            DeleteFile(fileName)
            WriteToFile(fileName, "w")

        elif(optionChosen == "C"):
            WriteToFile(fileName, "a")

        elif(optionChosen == "D"):
            ReplaceLine(fileName)

        else:
            print("Exiting the file options")
            break


"""
This is the solution for the Homework #4: Lists
Solution 2

"""

print("Solution 2 : Assignment on Lists")

myUniqueList = []
myLeftovers = []

print(myUniqueList)

def addToList(value) :
    result = False
    try :
        index = myUniqueList.index(value)
        result = False
        myLeftovers.append(value)
    except ValueError :
        result = True
        myUniqueList.append(value)
    return result

print(addToList(1))
print(addToList(2))
print(addToList(2))
print(addToList("Deepak"))
print(addToList("Deepak"))
print(addToList(3.2))
print(addToList(6))
print(addToList(1))
print(addToList(1))

print("myUniqueList : ", myUniqueList)
print("myLeftovers : ", myLeftovers)

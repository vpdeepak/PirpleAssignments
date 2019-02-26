"""
This is the solution for the Homework #3: "If" Statements.

"""

print("Assignment on If Statements")

def Comparer(param1, param2, param3):
    result = False
    if(int(param1) == int(param2) or int(param1) == int(param3)) :
        result = True
    elif(int(param2) == int(param3)) :
        result = True
    else :
        result = False
    return result

print(Comparer(1,1,1))
print(Comparer(1,2,2))
print(Comparer(2,2,1))
print(Comparer(2,1,2))
print(Comparer(1,2,3))

print(Comparer(6,5,"5"))
print(Comparer("5","5","5"))
print(Comparer("5","6","7"))

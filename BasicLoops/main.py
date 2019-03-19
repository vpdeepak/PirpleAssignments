"""
This is the solution for the Homework #5: Basic Loops

"""

print("Assignment on Basic Loops")

for num in range(1, 101, 1):
    show = num
    if(num % 3 == 0 and num % 5 == 0):
        show = "FizzBuzz"
    elif(num % 3 == 0):
        show = "Fizz"
    elif(num % 5 == 0):
        show = "Buzz"

    counter = 0
    for i in range(1, num + 1, 1):
        if(num % i == 0):
            counter += 1
            if(counter > 2):
                break

    if(counter == 2):
        show = "prime"

    print(show)

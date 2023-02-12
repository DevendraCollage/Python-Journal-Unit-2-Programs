# Handling Exception Program In Python

try:
    print("Try Block")
    x = int(input("Enter a Number One : "))
    y = int(input("Enter a Number Two : "))
    z = x / y
except ZeroDivisionError:
    print("Except Block")
    print("Division by 0 is not accepted")
else:
    print("Else Block")
    print("Division = ", z)
finally:
    print("Finally Block")
    x = 0
    y = 0
print("Out of try, except, else, and finally block")


"""
Output :
Try Block
Enter a Number One : 10
Enter a Number Two : 20
Else Block
Division = 0.5
Finally Block
Out of try, except, else, adn finally block
"""

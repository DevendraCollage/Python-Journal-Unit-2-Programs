# Handling Exception-2 In Python Program

try:
    x = int(input("Enter a number under 100 : "))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "Number Is Out Of Range")
else:
    print(x, "Number is in the Range")


"""
Output :
Enter a number under 100 : 200
Number Is Out Of Range
Enter a number under 100 : 20
Number is in the Range
"""

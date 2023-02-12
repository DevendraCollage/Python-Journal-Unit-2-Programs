# Searching Algorithm Programs In Python
# Binary Search Demo

def search(L, e):
    """Assumes L is a list, the elements of which are in ascending order
       Returns True if e is in L and False Otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


list = [10, 20, 30, 40, 50]
n = int(input("Enter The Search Value : "))
if (search(list, n)):
    print(n, "Is In The List")
else:
    print(n, "Is Not In The List")


"""
Output :
Enter The Search Value : 20
20 Is In The List
Enter THe Search Value : 80
80 Is Not In The List
"""

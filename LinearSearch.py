# Searching Algorithm Programs In Python
# Linear Search Demo

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        return False


list = [10, 20, 30, 40, 50]
n = int(input("Enter Search Value : "))
if (search(list, n)):
    print(n, "Is In The List")
else:
    print(n, "Is Not In The List")


"""
Output :
Enter Search Value : 60
60 Is Not In The List
Enter Search Value : 10
10 Is In The List
"""

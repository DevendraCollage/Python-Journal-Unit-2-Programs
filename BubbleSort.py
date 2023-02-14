# Sorting Algorithm Programs In Python
# Bubble Sort Demo

def bubble_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if (alist[j+1] > alist[j]):
                alist[j], alist[j+1] = alist[j+1], alist[j]
                no_swap = False
        if no_swap:
            return


alist = input("Enter the list of numbers:").split()
alist = [int(x) for x in alist]
bubble_sort(alist)
print("Sorted list :", end="")
print(alist)


"""
Output :
Enter the list of numbers : 64 45 2 11 78 98 
Sorted list : [98,78,64,45,11,2]
"""

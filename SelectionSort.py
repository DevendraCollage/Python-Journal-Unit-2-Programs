# Sorting Algorithm Programs In Python
# Selection Sort Demo

def selection_sort(alist):
    for i in range(0, len(alist)-1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]


alist = input("Enter the list of numbers : ").split()
alist = [int(x) for x in alist]
selection_sort(alist)
print("Sorted List : ", end="")
print(alist)


"""
Output : 
Enter the list of numbers : 77 88 100 45 2 14 74
Sorted List : [2,14,45,74,77,88,100]
"""

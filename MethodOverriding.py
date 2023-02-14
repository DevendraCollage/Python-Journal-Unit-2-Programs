# Method Overriding in Python

class A():
    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)


class B(A):
    def __init__(self):
        self.value = "Inside Child"

    def show(self):
        print(self.value)


ob1 = A()
ob2 = B()
ob1.show()
ob2.show()


"""
Output :
Inside Parent
Inside Child
"""

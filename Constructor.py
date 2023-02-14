# Constructor in Python

class A:

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j", format(self.real, self.imag))


c1 = A(2, 3)
c1.getData()

c2 = A(5)
c2.attr = 10
print((c2.real, c2.imag, c2.attr))


"""
Output :
2 + 3j
(5,0,10)
"""

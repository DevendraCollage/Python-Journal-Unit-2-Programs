# Encapsulation Demo in Python

class Students:
    def __init__(self, name, rank, points):
        self.name = name
        self.rank = rank
        self.points = points

    # custom function
    def demofunc(self):
        print("I am "+self.name)
        print("I got Rank ", +self.rank)


# create 4 objects
st1 = Students("Devendra", 1, 100)
st2 = Students("Mohit", 2, 90)
st3 = Students("Shahil", 3, 76)
st4 = Students("Dharmik", 4, 60)

# call the functions using the objects created above
st1.demofunc()
st2.demofunc()
st3.demofunc()
st4.demofunc()


"""
Output : 
I am Devendra
I got Rank  1
I am Mohit
I got Rank  2
I am Shahil
I got Rank  3
I am Dharmik
I got Rank  4
"""

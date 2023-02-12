# Inheritance Demo In Python

class Animal:
    def speak(self):
        print("Animal Speaking")
# The child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("Dog barking")
# The child class DogChild inherits another child class Dog


class DogChild(Dog):
    def eat(self):
        print("Eating bread...")


d = DogChild()
d.bark()
d.speak()
d.eat()


"""
Output :
Dog Barking
Animal Speaking
Eating Bread... 
"""

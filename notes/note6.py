
#inheitance and class program

class Animals:
    def speak(self):
        print("speaking")

class Dog(Animals):
    def bark(self):
        print('barking')

class Puppy(Dog):
    pass
    #here i can use the  methods speak() and bark() because i'm inheriting the Dog class

obj=Puppy()
obj.bark()
obj.speak()

#barking
#speaking

dog=Dog()
dog.speak()
dog.bark()
#speaking
#barking


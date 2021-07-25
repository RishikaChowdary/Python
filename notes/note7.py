from note6 import Animals



#here we are importing Animals class in Animals A is capital consider it as class

class Lion(Animals):
    def roar(self):
        print("roaring")

obj=Lion()

obj.roar()
obj.speak()

#roaring
#speaking

# it prints extra stuff because in notes6 program we printed 
# dog=Dog()
#dog.speak()
#dog.bark()



#importing modlues
#inheritance intro

from note import Add

# in Add A is capital that means it is importing class from note.py if it is small letter then it is importing functions(methods)

#importing module

class B(Add):

    pass

    #B(A) - B inheriting A class we can access methods of class Add

a=B()

x=a.add(1,1)

print(x)


#here out put is 
#2 
#2 
#2
#because in note.py we printed add(1,1) 2 times 3rd 2 is from here


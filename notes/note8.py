class Phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    # __init__ is a super constructor it exectues when ever the object of class is created 
    # it is a good way of declaring the variables in __init__ because it executes when is runed
    
    
    #consider the print statement below it prints the output as  is created
    print("__init__ executed")

    def details(self):

        print('phone brand:',self.brand)
        print('phone model:',self.model)

i6=Phone('Apple','iphone6')
i7=Phone('Apple','iphone7')

moto=Phone('Lenovo','X')

i6.details()

i7.details()

moto.details()





# in class self is used because it points to the object
# consider above program :

'''
self in python:

for object i6,i7 and moto

    for i6 object 
    self.brand will be as i6.brand
    self.model will be i6.model

    for moto object

    self.brand =moto.brand
    self.model=moto.model

    here mainly self is used and you shoud use it in classes
    to point the object 
    and it is programatic way of considering the which object variables to get

    consider above program:
    
    in details we defined self as 'details(self)' if i call moto.details self is pointing to the moto object it calls the details of it


  '''

''' thank you '''

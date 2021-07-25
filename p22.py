#simple calculator
class Calculator:
    def __init__(self,x=0):
        self.x=x
    def __str__(self):
        return "({0})".format(self.x)
    def __add__(self,other):
        x=self.x+other.x
        return Calculator(x)
    def __sub__(self,other):
        x=self.x-other.x
        return Calculator(x)
    def __mul__(self,other):
        x=self.x*other.x
        return Calculator(x)
    def __truediv__(self,other):
        x=self.x/other.x
        return Calculator(x)
while True:
        print('1.Addition')
        print('2.Substraction')
        print('3.Multiplication')
        print('4.Division')
        ch=input('enter your choice')
        
        if(ch=='+'):
            a=int(input('enter a:'))
            b=int(input('enter b:'))
            obj1=Calculator(a)
            obj2=Calculator(b)
            print(obj1 + obj2)
        elif(ch=='-'):
            a=int(input('enter a:'))
            b=int(input('enter b:'))
            obj1=Calculator(a)
            obj2=Calculator(b)
            print(obj1-obj2)
        elif(ch=='*'):
            a=int(input('enter a:'))
            b=int(input('enter b:'))
            obj1=Calculator(a)
            obj2=Calculator(b)
            print(obj1 * obj2)
        elif(ch=='/'):
            a=int(input('enter a:'))
            b=int(input('enter b:'))
            obj1=Calculator(a)
            obj2=Calculator(b)
            print(obj1/obj2)
        else:
            print('operation invalid')
    


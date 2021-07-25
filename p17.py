#method overloading
class DemoOverloading:
    def add(self,a=None,b=None,c=None,d=None):
        if((a!=None and b!=None)and(c!=None and d!=None)):
            s=a+b+c+d
        elif((a!=None and b!=None)and(c!=None)):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        print('Sum=',s)
obj=DemoOverloading()
obj.add(10,20,30,40)
obj.add(10,20,30)
obj.add(10,20)
obj.add(10)

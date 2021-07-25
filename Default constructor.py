# default constructor
class Demo:
    def __init__(self):
        self.n=int(input('enter number'))
        self.a=int(input('enter base'))
        self.b=int(input('enter power'))
        self.original=input('enter the string').split(' ')
        self.substring=input('enter the substring')
        self.replace=input('enter string to be replaced')
    def strReplacement(self):
        for i in range(len(self.original)):
           if(self.original[i]==self.substring):
            self.original[i]=self.replace
        for x in self.original:
           print(x,end=' ')
    def calReverse(self):
       self.rev=0
       while(self.n!=0):
         self.rem=self.n%10
         self.rev=self.rev*10+self.rem
         self.n=self.n//10
       print(self.rev)
    def calPower(self):
       self.res=1
       for i in range(self.b):
         self.res=self.res*self.a
       print(self.res)
ob=Demo()
ob.strReplacement()
ob.calReverse()
ob.calPower()

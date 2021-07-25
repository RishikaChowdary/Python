#class variables and function variables
class Number:
    def Show(self,a,b):
        self.first=int(input('enter firstvalue:'))
        self.second=int(input('enter second value:'))
        first=a
        second=b
        print('Class variable')
        print(self.first,' ',self.second)
        print('function variable')
        print(first,' ',second)
no1=Number()
no2=Number()
no3=Number()

no1.Show(123,532)
no2.Show('vjit','cse')
no3.Show(23.42,12.43)

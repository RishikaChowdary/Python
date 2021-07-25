class Number:
    def input(self):
        self.x=int(input('enter x:'))
        self.y=int(input('enter y:'))
    def show(self):
        print('X=',self.x,'and Y=',self.y)
    def add(self,anotherObject):
        temp=Number()
        temp.x=self.x+anotherObject.x
        temp.y=self.y+anotherObject.y
        return temp
no1=Number()
no2=Number()
no3=Number()
no1.input()
no2.input()
no3=no1.add(no2)
print('From no1')
no1.show()
print('From no2')
no2.show()
print('From no3')
no3.show()

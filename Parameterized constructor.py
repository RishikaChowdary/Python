#parameterized constructor
class Addition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def process(self):
        self.z=self.x+self.y
    def output(self):
        print('addition is:',self.z)
x,y=int(input('enter x=')),int(input('enter y='))
task1=Addition(x,y)
task2=Addition(10,20)
task1.process()
task1.output()
task2.process()
task2.output()

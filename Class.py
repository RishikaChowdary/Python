#class
class Addition():
    def input(self):
        self.a,self.b=int(input('enter a=')),int(input('enter b='))
    def process(self):
        self.c=self.a+self.b
    def output(self):
        print('Addition is:',self.c)
task=Addition()
task1=Addition()
print('From task')
task.input()
task.process()
task.output()
print('From task1')
task1.input()
task1.process()
task1.output()

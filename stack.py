class Stack:
    def __init__(self):
        self.list=[]
    def push(self,item):
        self.item=item
        self.list.append(item)
    def pop(self):
        self.list.pop()
    def show(self):
        for i in self.list:
            print(i)
obj=Stack()
while True:
    print('1.push')
    print('2.pop')
    print('3.show')
    print('4.exit')
    ch=int(input('enter your choice'))
    if(ch==1):
        item=int(input('enter element to insert'))
        obj.push(item)
    elif(ch==2):
        obj.pop()
    elif(ch==3):
        obj.show()
    else:
        break
    
        

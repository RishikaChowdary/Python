class Queue:
    def __init__(self):
        self.tuple=()
    def insert(self,item):
        self.item=item
        self.list=list(self.tuple)
        self.list.append(item)
        self.tuple=tuple(self.list)
        print('inserted')
    def delete(self):
        self.list=list(self.tuple)
        self.list.remove(self.list[0])
        self.tuple=tuple(self.list)
        print('deleted')
    def show(self):
        for i in self.tuple:
           print(i)
obj=Queue()
while True:
        print('1.insert')
        print('2.delete')
        print('3.show')
        print('4.exit')
        ch=int(input('enter your choice:'))
        if(ch==1):
            item=int(input('enter value to be inserted'))
            obj.insert(item)
        elif(ch==2):
            obj.delete()
        elif(ch==3):
            obj.show()
        else:
            break

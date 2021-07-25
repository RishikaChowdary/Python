class LinearSearch:
    def __init__(self):
       self.l=[12,4,20,5,7,19]
       self.pos=0
    def search(self,key):
      for i in range(len(self.l)):
        if(self.l[i]==key):
            globals()['pos']=i
            print('True found at',pos,'position')
            break
      else:
        print('False')
obj=LinearSearch()
key=int(input('enter element to be searched:'))
obj.search(key)

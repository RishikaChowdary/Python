#double linked list
class Node:
    def __init__(self,Dval):
        self.prev=None
        self.next=None
        self.val=Dval
class DLinkedList:
    def __init__(self):
        self.head=None
    def insertAtBegining(self,Dval):
        if self.head==None:
            new=Node(Dval)
            self.head=new
        else:
            new=Node(Dval)
            temp=self.head
            self.head=new
            new.next=temp.prev
            new.prev=None
    def insertAtEnd(self,Dval):
        last=self.head
        while last.next:
            last=last.next
        new=Node(Dval)
        last.next=new
        new.prev=last
        new.next=None
    def removeAtBegining(self):
        if self.head.next is None:
            self.head=None
        elif self.head is None:
            print('No istem in list')
        else:
            newHead=self.head.next
            self.head=newHead
            self.head.prev=None
    def removeAtEnd(self):
        counter=self.head
        prevNode=None
        while counter.next:
            prevNode=counter
            counter=counter.next
        prevNode.next=None
        counter.prev=None
    def insertMiddle(self,exist,Dval):
        cur=self.head
        while cur:
            if cur.val==exist:
                break
            cur=cur.next
        newNext=cur.next
        new=Node(Dval)
        cur.next=new
        new.next=newNext
        newNext.prev=new
        new.prev=cur
    def removeMiddle(self,exist):
        cur=self.head
        prevNode=None
        while cur:
           if cur.val==exist:
             temp=cur
             break
           prevNode=cur
           cur=cur.next
        if cur is None:
            print('Node not available')
        else:
            newNext=cur.next
            prevNode.next=newNext
            temp.prev=prevNode
    def showLinkedList(self):
        counterNode=self.head
        print('values from double linked list:',end='')
        while counterNode:
            print(counterNode.val,'--->',end='')
            counterNode=counterNode.next
        print('\r')
obj=DLinkedList()
while True:
    print('1.insert node at beginning of doubly linked list')
    print('2.insert node at end of doubly linked list')
    print('3.delete node from beginning of doubly linked list')
    print('4.delete node from end of doubly linked list')
    print('5.insert node at middle of linked list')
    print('6.delete node at middle of linked list')
    print('7.show doubly linked list')
    print('8.exit')
    ch=int(input('enter your choice:'))
    if(ch==1):
        Dval=1
        obj.insertAtBegining(Dval)
    elif(ch==2):
        Dval=2
        obj.insertAtEnd(Dval)
    elif(ch==3):
        obj.removeAtBegining()
    elif(ch==4):
        obj.removeAtEnd()
    elif(ch==5):
        exist=1
        Dval=3
        obj.insertMiddle(exist,Dval)
    elif(ch==6):
        exist=2
        obj.removeMiddle(exist)
    elif(ch==7):
        obj.showLinkedList()
    else:
        break
        

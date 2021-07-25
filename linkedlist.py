#container for node
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
#container for linked list
class LinkedList:
    def __init__(self):
        self.head=None
    def addItems(self,newNode):
        new=Node(newNode)
        new.next=self.head
        self.head=new
        print('Node added to linked list')
    def addItemsAtEnd(self,newNode):
        new=Node(newNode)
        if(self.head==None):
            self.head=new
            new.next=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.next=None
    def removeNodeAtBegining(self):
        if(self.head==None):
            print('Linked list is empty')
        else:
            self.head=self.head.next
            print('Node deleted from starting point')
    def removeNodeAtEnd(self):
        newHead=self.head
        prevNode=None
        if(self.head==None):
            print('Linked list is empty')
        else:
            while newHead.next:
                prevNode=newHead
                newHead=newHead.next
            prevNode.next=None
            print('Node deleted from end point')
    def showLinkedList(self):
        counterNode=self.head
        print('Values from Linked List:',end='')
        while counterNode:
            print(counterNode.val,'--->',end='')
            counterNode=counterNode.next
        print('\r')
    def insertMiddleNode(self,exist,newNode):
        temp=self.head
        while temp is not None:
            if temp.val==exist:
                break
            temp=temp.next
        if temp is None:
            print('Node is not available')
        else:
            newNext=temp.next
            new=Node(newNode)
            temp.next=new
            new.next=newNext
    def removeMiddleNode(self,nodeval):
        temp=self.head
        prevNode=None
        while temp is not None:
            if temp.val==nodeval:
                break
            prevNode=temp
            temp=temp.next
        if temp is None:
            print('Node is not available')
        else:
            newNext=temp.next
            prevNode.next=newNext
n=LinkedList()
while True:
    print('1.insert node at beginning of linked list')
    print('2.insert node at end of linked list')
    print('3.delete node from beginning of linked list')
    print('4.delete node from end of linked list')
    print('5.show linked list')
    print('6.insert node at middle of linked list')
    print('7.delete node at middle of linked list')
    print('8.exit')
    ch=int(input('enter your choice:'))
    if(ch==1):
        newNode=1
        n.addItems(newNode)
    elif(ch==2):
        newNode=3
        n.addItemsAtEnd(newNode)
    elif(ch==3):
        n.removeNodeAtBegining()
    elif(ch==4):
        n.removeNodeAtEnd()
    elif(ch==5):
        n.showLinkedList()
    elif(ch==6):
        exist=1
        newNode=2
        n.insertMiddleNode(exist,newNode)
    elif(ch==7):
        nodeval=2
        n.removeMiddleNode(nodeval)
    else:
        break
    
    

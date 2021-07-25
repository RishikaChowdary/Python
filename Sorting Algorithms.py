class Sort:
    list=[]
    arr=[]
    def bubbleSort(self,list):
        for i in range(len(self.list)):
            for j in range(i+1,range(self.list)):
                if self.list[j] < self.list[i]:
                    temp=self.list[j]
                    self.list[j]=self.list[i]
                    self.list[i]=temp
        for x in range(len(self.list)):
            print(list,end='')
    def selectionSort(self,list):
        for i in range(len(self.list)):
            min=i
            for j in range(i,len(self.list)):
                if self.list[j] < self.list[min]:
                    min=j
            temp=self.list[min]
            self.list[min]=self.list[i]
            self.list[i]=temp
    def mergeSort(self,arr):
        if(len(arr)>1):
            mid=len(arr)//2
            L=arr[:mid]
            R=arr[mid:]
            mergeSort(L)
            mergeSort(R)
            i=j=k=0
            while i < len(L) and j < len(R):
                if(L[i] < R[j]):
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                K+=1
            while i < len(L):
               arr[k]=L[i]
               i+=1
               k+=1
            while i < len(L):
                arr[k]=R[j]
                j+=1
                k+=1
    def printMergeList(self,arr):
        for i in range(len(arr)):
            print(arr[i],end=' ')
        print()
obj=Sort()
while True:
    print('1.Bubblesort')
    print('2.Selection sort')
    print('3.Merge sort')
    print('4.show merged list')
    ch=int(input('enter your choice'))
    if(ch==1):
        list=[12,3,1,20,45,2,30]
        obj.bubbleSort(list)
    elif(ch==2):
        list=[12,3,1,20,45,2,30]
        obj.selectionSort(list)
    elif(ch==3):
        arr=[12,5,2,23,8]
        obj.mergeSort(arr)
    elif(ch==4):
        arr=[12,5,2,23,8]
        obj.printMergeList(arr)
    else:
        break

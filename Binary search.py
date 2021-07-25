pos=0
def sort():
        for i in range(len(list)):
            min=i
            for j in range(i,len(list)):
                if list[j] < list[min]:
                    min=j
            temp=list[min]
            list[min]=list[i]
            list[i]=temp
def search(list,key,start,end):
    if(end>=1):
        globals()['pos']=i
        mid=(start+end)//2
        if(list[mid]==key):
            return True
        elif(list[mid]>key):
            return search(list,key,start,mid-1)
        elif(list[mid]<key):
            return search(list,key,mid+1,end)
        else:
            return False
list=[]
count=int(input('enter number of elements in list'))
for i in range(count):
    ele=int(input('enter element:'))
    list.append(ele)
key=int(input('enter element to be searched:'))
list.sort()
if search(list,key,0,len(list)):
    print('Element found at: ',pos)
else:
    print('Element not found')

    

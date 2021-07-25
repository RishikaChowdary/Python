class MergeSort:
    def mergeSort(arr):
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
obj=MergeSort()
arr=[21,4,12,5,6,8,2]
print("Given array is:",end="\n")
obj.printMergeList(arr)
obj.mergeSort(arr)
print("sorted array is:",end="\n")
obj.printMergeList(arr)

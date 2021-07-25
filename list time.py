from time import process_time 
list1=[10,20,30,40,50,60]
t1_start = process_time() 
for i in range(len(list1)): 
	list1[i]=2*list1[i]
for i in list1:
    print(i,end=' ')
print() 
t1_stop = process_time() 
print("Elapsed time:", t1_stop, t1_start) 
print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)


									     

from time import process_time
from array import *
values=array('i',[10,20,30,40,50,60])
t1_start = process_time() 
for i in range(len(values)): 
	values[i]=2*values[i]
for i in values:
    print(i,end=' ')
print() 
t1_stop = process_time() 
print("Elapsed time:", t1_stop, t1_start) 
print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)


									     

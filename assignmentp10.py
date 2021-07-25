#program 10
list1=[10,20,30,40,50]
list2=[10,30,40]
newlist1=set(list1)
newlist2=set(list2)
reslist=list(newlist1-newlist2)
print('difference is:',reslist)

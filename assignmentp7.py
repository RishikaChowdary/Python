#program 7
n=int(input('enter number of elements'))
num=0
for i in range(n):
    ele=int(input('enter values:'))
    num=num+ele
mean=(num)/n
print('mean is:',mean)
add=0
for i in range(n):
    ele=int(input('enter values:'))
    val=ele-mean
    vals=val**2
    add=add+vals
var=(add)/(n-1)
print('variance is:',var)
            

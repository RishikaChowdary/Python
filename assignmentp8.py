#program 8
a=input('enter lowercase string:')
for i in range(0,len(a)):
    b=ord(a[i])
    if(b>=97 and b<=122):
        b=b-32
    res=chr(b)
    print(res,end='')

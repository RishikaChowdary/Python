#program 3
x=int(input('enter first number:'))
y=int(input('enter second number:'))
z=int(input('enter third number:'))
if(x>y):
    if(x>z):
        res=x
    else:
        res=z
else:
    if(y>z):
        res=y
    else:
        res=z
print('largest of 3 numbers=',res)

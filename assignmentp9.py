#program 9
no1=int(input('enter first number'))
no2=int(input('enter second number'))
if(no1>no2):
    res=no2
else:
    res=no1
for i in range(1,res+1):
    if((no1%i==0) and (no2%i==0)):
        gcd=i
print('gcd is',gcd)

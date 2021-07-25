#parameterized functions
def Reverse(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print(rev)
def Grade(m1,m2,m3):
    m1,m2,m3
    total=(m1+m2+m3)
    percent=total/3
    if(percent>85):
        print('A grade')
    elif(percent<85 and percent>75):
        print('B grade')
    elif(percent<75 and percent>65):
        print('C grade')
    elif(percent<65 and percent>45):
        print('D grade')
    else:
        print('fail')
def Power(a,b):
    res=1
    for i in range(b):
        res=res*a
    print(res)
Reverse(12)
Grade(50,70,70)
Power(2,3)

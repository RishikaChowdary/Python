#program 4
wt=float(input('enter weight'))
ht=float(input('enter height'))
bmi=wt/(ht**2)
print('body mass index is:',bmi)
if(bmi<15):
    print('very underweight')
elif(bmi>=15 and bmi<18):
    print('underweight')
elif(bmi>=18 and bmi<25):
    print('healthy')
elif(bmi>=25 and bmi<=30):
    print('overweight')
else:
    print('very overweight')

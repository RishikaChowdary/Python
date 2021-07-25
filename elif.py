#elif
a=int(input('enter marks'))
if(a>85):
    print('Grade A')
elif(a<85 and a>75):
    print('Grade B')
elif(a<75 and a>65):
    print('Grade C')
elif(a<65 and a>55):
    print('Grade D')
elif(a<55 and a>40):
    print('Grade E')
else:
    print('fail')

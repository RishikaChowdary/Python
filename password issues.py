#password issues
pwd=input('enter password:')
nos,non=0,0
for ch in pwd:
    if(ch=='@' or ch=='!' or ch=='#' or ch=='&' or ch=='^' or ch=='%' or ch=='*'):
       nos=nos+1;
    if(ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9' or ch=='0'):
       non=non+1;


l=len(pwd)
if(l>=8 and (nos>=1 and non>=1)):
    print('very good password')
elif(l>=6 and (nos>=1 and non>=1)):
    print('good password')
else:
    print('bad password')

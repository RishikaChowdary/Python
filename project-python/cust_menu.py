from cust_signup import *
from cust_login import *
import getpass,sys,os
while True:
    print('1.register')
    print('2.login')
    ch=int(input('enter your choice'))
    if(ch==1):
        obj=cust_signup()
        break
    elif(ch==2):
        obj=cust_login()
        self.username=input('enter username:')
        self.password=input('enter password:')
        self.password=getpass.getpass(prompt='enter password:',stream=stderr)
        result=obj.checklogin(username,password)
    else:
        print('Wrong credentials')
        break

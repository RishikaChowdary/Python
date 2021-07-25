import getpass,sys
from admin_dash import *

def Login():
    count=0
    while True:
        print('ADMIN LOGIN')
        user=input('enter username:')
        pwd=getpass.getpass(prompt='Enter password:',stream=sys.stderr)
        if(user=='admin' and pwd=='admin'):
            print('Login success')
            obj=admin_dash()
            break
        else:
            print('Wrong credentials')
            count=count+1
        if(count==3):
            print('Bye')
            break

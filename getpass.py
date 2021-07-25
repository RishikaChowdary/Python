import getpass,sys
try:
    pwd=getpass.getpass(prompt='Enter password:',stream=sys.stderr)
    print('You Entered:',pwd)
except Exception as e:
    print('Error:',e)

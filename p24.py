#exception handling using try except and finally
a=10
b=0
try:
    print('DB connected...')
    print('Working on DB')
    c=a/b
    print('c=',c)
except:
    print('Error occurs...')
finally:
    print('Closing of DB')

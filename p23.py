#exception handling using try and except
a=int(input('enter a:'))
b=int(input('enter b:'))
print('Calculation starts..')
list1=[39,34]
try:
    c=a/b
    print('Calculation ends...')
    print('c=',c)
    print(list1[4])
except ZeroDivisionError:
    print('Error Occurs...')
    print('Bye!')
except IndexError:
    print('Index Error')
print('End of program')

#dictionary
dt={}
print('program to demonstrate dictionary')
l=int(input('enter length:'))
for i in range(l):
      key,value=input('enter dictionary value(k:v)').split(':')
      dt[key]=value
key_list=list(dt.keys())
for key in key_list:
      print(dt[key],end=' ')
print('\r')
print('End of program')

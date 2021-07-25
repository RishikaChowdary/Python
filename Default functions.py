#default functions
num=[10,20,30,40]
def Max():
    max=num[0]
    for i in range(len(num)):
        if(num[i]>max):
            max=num[i]
    print('max=',max)
def Armstrong():
    n=int(input('enter number'))
    arm=0
    temp=n
    while(n!=0):
        rem=n%10
        arm=arm+rem*rem*rem
        n=n/10
        if(arm==temp):
           print('armstrong')
def Items():
           menu_dt={'item1':100,'item2':20}
           menu_list=[]
           for i in range(len(menu_dt)):
               menu_list=list(menu_dt.keys())
           tables=int(input('enter no of tables'))
           for i in range(tables):
               print('menu of table:',i+1)
               total=0
               menu=input('enter item:')
               if(menu in menu_list):
                 qty=int(input("how many quantity:"))
                 total=total+(menu_dt[menu]*qty)
               while(menu in menu_list):
                 menu=input('enter item')
               if(menu in menu_list):
                 qty=int(input('enter quantity'))
                 total=total+(int(menu_dt[menu])*qty)

           print("total bill",i+1,"is",total)
           


Max()
Armstrong()
Items()
    

#restuarant bills
menu_dt={'item1':100,'item2:20}
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
                 total=total+(int(menu_dt[menu])*qty

        print("total bill",i+1,"is",total)
        if(menu=='q')
            i=i+1
        else:
            print('item not available')

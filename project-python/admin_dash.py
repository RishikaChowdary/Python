import pymysql
class admin_dash:
    
        def __init__(self):
          self.menu()  
          self.name=None
          self.category=None
          self.MRP=None
          self.quantity=None
          self.company=None
          self.dateofexpiry=None
        def insert(self):
          self.name=input('enter product name:')
          self.category=input('enter product category:')
          self.MRP=input('enter price:')
          self.quantity=input('enter quantity:')
          self.company=input('enter company:')
          self.dateofexpiry=input('enter date of expiry:')
          self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
          self.cur=self.con.cursor()
          sql="insert into product(name,category,MRP,quantity,company,dateofexpiry)values(%s,%s,%s,%s,%s,%s)"
          values=[self.name,self.category,self.MRP,self.quantity,self.company,self.dateofexpiry]
          self.cur.execute(sql,values)
          self.con.commit()
          self.con.close()
          print('product added')
        def update(self):
          self.name=input('enter product name:')
          self.MRP=input('enter price:')
          self.quantity=input('enter quantity:')
          self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
          self.cur=self.con.cursor()
          sql="update product SET MRP=%s,quantity=%s where name=%s"
          values=[self.MRP,self.quantity,self.name]
          self.cur.execute(sql,values)
          self.con.commit()
          self.con.close()
          print('Updated')
        def delete(self):
          self.name=input('enter product name:')
          self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
          self.cur=self.con.cursor()
          sql="delete from product where name=%s"
          values=[self.name]
          self.cur.execute(sql,values)
          self.con.commit()
          self.con.close()
          print('Deleted')
        def showproduct(self):
          self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
          self.cur=self.con.cursor()
          print('name\tcategory\tMRP\tquantity\tcompany\tdateofexpiry')
          sql="select * from product"
          self.cur.execute(sql)
          allRow=self.cur.fetchall()
          for row in allRow:
             for column in row:
               print(column,end='\t')
             print('\r')
        def showusers(self):
          pass
        def showinvoice(self):
          pass
        def menu(self):
          while True:
               print('1.Insert a product')
               print('2.Update')
               print('3.Delete')
               print('4.show products')
               print('5.show users')
               print('6.show Invoice')
               print('7.Exit')
               choice=int(input('enter your choice'))
               if(choice==1):
                 self.insert() 
               elif(choice==2):
                 self.update()
               elif(choice==3):
                 self.delete()
               elif(choice==4):
                 self.showproduct()
               elif(choice==5):
                 pass
               elif(choice==6):
                 pass
               else:
                 break
    
        

import pymysql
class cust_dash:
    def __init__(self):
        self.menu()
        pass
    def menu(self):
      while True:
        print('1.My account')
        print('2.My cart')
        print('3.check out')
        print('4.product list')
        print('5.log out')
        ch=int(input('enter your choice:'))
        if(ch==1):
            pass
        elif(ch==2):
            pass
        elif(ch==3):
            pass
        elif(ch==4):
            self.productlist()
        elif(ch==5):
            pass
    def productlist(self):
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
    def account(self):
          self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
          self.cur=self.con.cursor()
          print

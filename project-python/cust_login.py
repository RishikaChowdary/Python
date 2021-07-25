import pymysql
class cust_login:
    def checklogin(self,username,password):
               check=True
               self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
               self.cur=self.con.cursor()
               sql="select count(id) from login where username=%s"
               values=[username]
               self.cur.execute(sql,values)
               data=cur.fetchone()
               count=int(data[0])
               if(count>0):
                   check=True
               else:
                   check=False
               return check

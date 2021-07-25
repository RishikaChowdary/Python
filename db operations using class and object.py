#database operations by using class and object
import pymysql as db
class DB_operation:
  try:
    def __init(self,sid=None,name=None,mobileno=None,email=None,allRow=None,sql=None):
       self.con=con
       self.cur=cur
    def insert(self,sid,name,mobileno,email):
        con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
        cur=con.cursor()
        sql="insert into student(id,name,mobileno,email)values(%s,%s,%s,%s)"
        values=[sid,name,mobileno,email]
        cur.execute(sql,values)
        con.commit()
        con.close()
    def update(self,sid,mobileno,email):
        con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
        cur=con.cursor()
        sql="update student SET mobileno=%s,email=%s WHERE id=%s"
        values=[mobileno,email,sid]
        cur.execute(sql,values)
        con.commit()
        con.close()
    def delete(self,sid):
        con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
        cur=con.cursor()
        sql="delete from student WHERE id=%s"
        values=[sid]
        cur.execute(sql,values)
        con.commit()
        con.close()
    def show(self):
        con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
        cur=con.cursor()
        print('s_id\tName\tMobileno\tEmail')
        sql="select * from student"
        cur.execute(sql)
        allRow=cur.fetchall()
        for row in allRow:
          for column in row:
            print(column,end='\t')
          print('\r')
  except Exception as e:
    print("Error : ",e)
obj=DB_operation()
while True:
    ch=int(input('enter your choice'))
    if(ch==1):
      sid=input('enter id:')
      name=input('enter name:')
      mobileno=input('enter mobileno:')
      email=input('enter email:')
      obj.insert(sid,name,mobileno,email)
    elif(ch==2):
      sid=input('enter id:')
      mobileno=input('enter mobileno:')
      email=input('enter email:')
      obj.update(sid,mobileno,email)
    elif(ch==3):
      sid=input('enter id:')
      obj.delete(sid)
    elif(ch==4):
      obj.show()
    else:
      break

      

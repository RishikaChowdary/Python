import pymysql
class MobileException(Exception):
    pass
class EmailException(Exception):
    pass
class UserReg:
    try:
        def __init__(self):
            self.con=None
            self.cur=None
            self.mobileno=None
            self.email=None
            self.dob=None
            self.fn=None
            self.ln=None
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='App_DB')
            self.cur=self.con.cursor()
        def createUser(self):
            self.fn=input('enter first name:')
            self.ln=input('enter last name:')
            self.mobileno=input(' enter mobileno:')
           
            self.email=input('enter email:')
            self.dob=input('enter date of birth:')
            self.fname=str(self.fn+' '+self.ln)
            sql="insert into register(FullName,Mobileno,Email,DOB,FirstName,LastName)values(%s,%s,%s,%s,%s,%s)"
            values=[self.fname,self.mobileno,self.email,self.dob,self.fn,self.ln]
            self.cur.execute(sql,values)
            self.con.commit()
            self.con.close()
        def checkmailInput(self,email):
            try:
                check=True
                count=0
                for i in email:
                   if(email=='.'):
                      count=count+1
                   if(email=='@'):
                      count=count+1
                if(count==0):
                   check=False
                   raise EmailException
                else:
                    check=True
            except:
                print('You entered invalid email')
            return check
        def checkmailDatabase(self,email):
            try:
               check=True
               count=0
               con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='App_DB')
               cur=con.cursor()
               sql="select count(user_id) from register where Email=%s"
               values=email
               cur.execute(sql,values)
               mail=cur.fetchone()
               count=int(mail[0])
               if(count==0):
                   check=True
               else:
                   check=False
                   raise EmailException
            except EmailException:
                print('Invalid email')
                return check
        def checkmobDatabase(self,mobileno):
            try:
                check=True
                count=0
                con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='App_DB')
                cur=con.cursor()
                sql="select count(user_id) from register where MobileNo=%s"
                values=mobileno
                cur.execute(sql,values)
                mb=cur.fetchone()
                count=int(mb[0])
                if(count==0):
                    check=True
                else:
                    check=False
                    raise MobileException
            except MobileException:
                print('Invalid mobileno')
                return check
            
    except Exception as e:
        print('Error:',e)
            

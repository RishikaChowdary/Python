import pymysql,getpass,sys
class cust_signup:
    def __init__(self):
        self.firstname=input('enter first name:')
        self.lastname=input('enter last name:')
        self.dob=input('enter date of birth:')
        self.email=input('enter email:')
        self.mobileno=input('enter mobileno')
        self.address=input('enter address:')
        self.fullname=self.firstname+self.lastname
        self.password=getpass.getpass(prompt='enter password:')
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
        self.cur=self.con.cursor()
        sql1="insert into signup(firstname,lastname,fullname,dob,email,mobileno,address)values(%s,%s,%s,%s,%s,%s,%s)"
        values1=[self.firstname,self.lastname,self.fullname,self.dob,self.email,self.mobileno,self.address]
        self.cur.execute(sql1,values1)
        self.con.commit()
        self.con.close()
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='project_db')
        self.cur=self.con.cursor()
        sql2="insert into login(username,password)values(%s,%s)"
        values2=[self.email,self.password]
        self.cur.execute(sql2,values2)
        self.con.commit()
        self.con.close()

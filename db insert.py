import pymysql as db
try:
    s_id,name,mobile,email=input('enter student details:').split(' ')
    con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
    cur=con.cursor()
    sql="insert into student(id,name,mobileno,email)values(%s,%s,%s,%s)"
    values=[s_id,name,mobile,email]
    cur.execute(sql,values)
    con.commit()
    con.close()
    print('1 Record Save')
except Exception as e:
    print('Error:',e)

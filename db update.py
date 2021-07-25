import pymysql as db
try:
    s_id=input('Enter emp id:')
    mobile,email=input('enter mobileno and email:').split(' ')
    con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
    cur=con.cursor()
    sql="update student SET mobileno=%s,email=%s WHERE id=%s"
    values=[mobile,email,s_id]
    cur.execute(sql,values)
    con.commit()
    con.close()
    print('1 Record updated')
except Exception as e:
    print('Error:',e)

import pymysql as db
try:
    s_id=input('Enter emp id:')
    con=db.connect(host='127.0.0.1',user='root',passwd='',db='vjit_db')
    cur=con.cursor()
    sql="delete from student WHERE id=%s"
    values=[s_id]
    cur.execute(sql,values)
    con.commit()
    con.close()
    print('1 Record deleted')
except Exception as e:
    print('Error:',e)

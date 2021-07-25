import pymysql as db
try:
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
    print('Error:',e)

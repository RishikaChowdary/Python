import pymysql
try:
    con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='VJIT_DB')
    print('Connected to database successfully')
    con.close()
    print('database disconnected')
except Exception as ex:
    print('error',ex)

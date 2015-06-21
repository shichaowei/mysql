#codinig:utf-8

import MySQLdb
conn=MySQLdb.connect(user='root',passwd='123456',host='127.0.0.1',db='Myschema')
cursor=conn.cursor()
'''
É¾³ý
i=0
while i<10:
    ins=cursor.execute("delete from commerial where wifiuser=%s",i)
    i=i+1
    print 'insert',ins
Ôö¼Ó 
i=0
while i<10:
    ins=cursor.execute('insert into commerial(wifiuser,commname) values(%s,%s)',(i,i))
    i=i+1
    print 'insert',ins
²éÑ¯     
sql = "select * from commerial"
cursor.execute(sql)                     
data = cursor.fetchall()
if data:
    for x in data:
        print x[0], x[1] 
'''    
cursor.close()
conn.commit()
conn.close()


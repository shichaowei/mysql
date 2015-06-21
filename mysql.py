#codinig:utf-8


import MySQLdb
import sys

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='Myschema')
except Exception, e:
    print e
    sys.exit()
cursor = conn.cursor()
sqluser = "insert into buswifi(wifiuser, commname) values (%s,%s)"
sqldev="insert into device(macadd,devname,devIP,commname) values (%s,%s,%s,%s)" 
sqlter = "insert into terminal(termac, terIP) values (%s,%s)"
sqlsea = "insert into search(wifiuser,devmac,termac) values (%s,%s,%s)"
user=1;dev=3001;ter=33001

try:
    while user<3001:
        cursor.execute(sqluser,(user,user))
        print user
        tempdev=dev+10
        while dev<tempdev:
            cursor.execute(sqldev,(dev,"devname","192.168.1.1",user))
            print dev
            dev=dev+1
            tempter=ter+10
            while ter<tempter:
                print ter
                cursor.execute(sqlter,(ter,ter))
                cursor.execute(sqlsea,(user,dev,ter))
                ter=ter+1
        user=user+1

except Exception, e:
    print e
    
sql = "select * from device"
cursor.execute(sql)                     
data = cursor.fetchall()
if data:
    for x in data:
        print x[0],x[1],x[2],x[3]
cursor.close()                          
conn.commit()
conn.close()                           

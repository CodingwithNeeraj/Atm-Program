import mysql.connector as ms
mysqldb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
mycurs=mysqldb.cursor()
mycurs.execute('select * from cos_data')
x=mycurs.fetchall()
for i in x:
    print(i)
# print(x)
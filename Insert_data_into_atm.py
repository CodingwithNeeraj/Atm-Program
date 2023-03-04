import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
cur=mydb.cursor()
acno=input("Enter your A/c No: ")
name=input('Enter your name: ')
cpin=int(input("Enter Card pin(4-digit): "))
if len(str(cpin))==4:
    pin=cpin
else:
    print('!!Please enter 4-digit pin.')
    cpin=int(input("Re-enter Card pin(4-digit): "))
    if len(str(cpin))==4:    # to check pin digit
        pin=cpin
    else:
        print('!! Wrong pin !!')
        
bal=int(input('Enter your Balance: '))

data=f"insert into cos_data values ('{acno}','{name}',{pin},{bal})"
cur.execute(data)
mydb.commit()
print(cur.rowcount, "record inserted.")
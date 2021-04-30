import mysql.connector
from mysql.connector import Error
from time import sleep
import temp
import ir
import lcd

db=mysql.connector.connect(host='ip',user='root',password='',database='dbname')

def check(a):
    if(a==1):
        lcd.irRange()
        print("inrange")
    else:
        lcd.irnotRange()
        print("Not in range")
        check(ir.ran())

def checkTemperature(temperature):
    if(temperature<95):
        lcd.below()
        print("Temperature is below normal")
        return temperature
    
    elif(temperature>98):
        lcd.high()
        temperature2=temp.tempfun()
        if(temperature2>98):
            lcd.highAgain()
            print("Your temperature is high and you have fever.Please Contact relevant health professional. ",temperature2)
            return temperature2
        else:
            lcd.normal()
            print("Your temperature is normal.You are permitted to enter inside",temperature)
            return temperature2        
    lcd.normal()
    print("Your temperature is normal.You are permitted to enter inside",temperature)
    return temperature
        
def insertUser(y):
    cursor=db.cursor()
    sqlt="SELECT CURRENT_TIMESTAMP();"
    cursor.execute(sqlt)
    time=cursor.fetchone()
    uid=y
    month=time[0].strftime("%b")
    table="temp_"+month        
    sql="INSERT INTO " + table + "(uid,checkin,checkout,temperature,shift)VALUES(%s,%s,%s,%s,%s);"
    cursor.execute("select tempid from "+table+" where uid='"+uid+"' and checkout='00:00:00';")
    h=cursor.fetchone()
    if(h==None):
        lcd.checkin()
        print("Check in")
        check(ir.ran())
        temperature=temp.tempfun()
        lcd.temp(temperature)
        print("Temperature: ",temperature)
        insertTemperature=checkTemperature(temperature)        
        cursor.execute(sql,(uid,time[0],"",insertTemperature,1))
        db.commit()
        print(cursor.rowcount,"Record inserted successfully")
        sleep(5)
    else:
        lcd.checkout()
        print("Check out")
        query="update "+table+" SET checkout= %s where uid = %s and checkout='00:00:00';"
        val=(time[0],uid)
        cursor.execute(query,val)
        db.commit()
        print(cursor.rowcount,"Record updated successfully")
        sleep(5)
    
def checkUser(x):
    if(db.is_connected()):
        cursor=db.cursor()
        sql="SELECT * FROM employee where email=%s"
        cursor.execute(sql,(x,))
        if(cursor.fetchall()):
            return 1    
        else:
            return 0

def selectname(x):
    cursor=db.cursor()
    sql="SELECT name FROM employee where email=%s"
    cursor.execute(sql,(x,))
    r=cursor.fetchone()
    print(r[0])
    lcd.displayname(r[0])

import py_mysql
import cv2
import pyzbar.pyzbar as pyzbar
import ultrasonicSensor
from time import sleep
import camera
import faceRecognition
import lcd
while(True):
    def capture_code():
        flag=1
        data=""
        while (flag):
            frame=camera.fra()
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                data=(obj.data).decode()
                flag=0
        return data
    if(ultrasonic.dist()<25):
        lcd.intro()
        print("Please show your qr or barcode..")
        value=capture_code()
        if(value==""):
            break
        else:
            try:
                email,uid=value.split(",")
                print("Email : ",email)
                print("uid : ",uid)
                print()
                if(py_mysql.checkUser(email)):
                    #py_mysql.selectname(email)
                    lcd.ui(uid)
                    lcd.codevalid()
                    print("Validated through code..")
                    print()
                    #sleep(5)
                    lcd.showface()
                    print("Show ur face..")
                    print()
                    value1=fr.fr1()
                    print("Value1 : ",value1)
                    if(value=="Unknown"):
                        lcd.unknown()
                        print("Unknown person...")
                        sleep(5)
                    else:
                        email1,uid1=value1.split(",")
                        if(email==email1 and uid==uid1):
                            lcd.facevalid()
                            py_mysql.selectname(email)
                            print("Validated through code and face...Welcome..")
                            py_mysql.selectname(email)
                            py_mysql.insertUser(uid)
                        else:
                            lcd.mismatch()
                            print("Qr and Person mismatch..")
                    print()
                else:
                    lcd.not_user()
                    print("You are not a registered user")
            except ValueError:
                 lcd.invalidcode()
                 print("Invalid code..")
    else:
          lcd.notinrange()
          print("Not in range..")

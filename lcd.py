#1
from RPi import GPIO
from time import sleep
from RPLCD.gpio import CharLCD
GPIO.setwarnings(False)
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23], numbering_mode=GPIO.BOARD)
lcd.write_string(u'Please show your face or QR code')
def intro():
    lcd.clear()
    lcd.write_string(u'Please show your QR or barcode')

def ui(a):
    lcd.clear()
    lcd.write_string(a)
    sleep(5)

def codevalid():
    lcd.clear()
    lcd.write_string(u'Validated through code..')


def showface():
    lcd.clear()
    lcd.write_string(u'Please show your face..')
    
def unknown():
    lcd.clear()
    lcd.write_string(u'Unknown face scanned..')

def facevalid():
    lcd.clear()
    lcd.write_string(u'Validated through code and face...Welcome..')

def mismatch():
    lcd.clear()
    lcd.write_string(u'Barcode and Face mismatch')

def not_user():
    lcd.clear()
    lcd.write_string(u'You are not a registered user')

def invalidcode():
    lcd.clear()
    lcd.write_string(u'Invalid code..')

def notinrange():
    lcd.clear()
    lcd.write_string(u'Not in range')

def irRange():
    lcd.clear()
    lcd.write_string(u'Measuring Temperature')
    print("Measuring Temperature")

def irnotRange():
    lcd.clear()
    lcd.write_string(u'Get within Temp Sensor Range')

def below():
    lcd.clear()
    lcd.write_string(u'Your temperature is below normal')

def normal():
    lcd.clear()
    lcd.write_string(u'Your Temperature is Normal')

def high():
    lcd.clear()
    lcd.write_string(u'Ur Temperature is high.Try again')

def highAgain():
    lcd.clear()
    lcd.write_string(u'Your temperature is still high')
    sleep(5)
    lcd.clear()
    lcd.write_string(u'Contact relevant people')

def checkin():
    lcd.clear()
    lcd.write_string('Checkin')

def checkout():
    lcd.clear()
    lcd.write_string('checked out....Thank You')

def displayname(a):
    lcd.clear()
    lcd.write_string(a)

def checkagain():
    lcd.clear()
    lcd.write_string(u'Show your face again')
    sleep(1)

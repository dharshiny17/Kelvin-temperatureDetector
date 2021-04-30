import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN)
def ran():
        state=GPIO.input(22)
        if state==False:
                print("Object Detected")
                return 1
        else:
                return 0



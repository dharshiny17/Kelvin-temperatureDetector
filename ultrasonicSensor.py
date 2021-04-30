import wiringpi as wpi
import time

pulse_start = 0
pulse_end = 0
wpi.wiringPiSetup()


             #39 gnd, 6 gnd
TRIG1_PIN=4   #    GPIO 4
ECHO1_PIN=5   #    GPIO 5


#PIN MODES 0-Input 1-Output
wpi.pinMode(TRIG1_PIN,1)
wpi.pinMode(ECHO1_PIN,0)

def dist():
    wpi.digitalWrite(TRIG1_PIN,0)
    time.sleep(0.000002)
    wpi.digitalWrite(TRIG1_PIN,1)
    time.sleep(0.00001)
    wpi.digitalWrite(TRIG1_PIN,0)
    pulse_start = time.time()
    pulse_end = time.time()
    while wpi.digitalRead(ECHO1_PIN)==0:
        pulse_start = time.time()
    while wpi.digitalRead(ECHO1_PIN)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end-pulse_start
    distance = (pulse_duration * 34300)/2
    return(distance)
    

#print(dist())
        
    

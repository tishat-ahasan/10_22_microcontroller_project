#!/usr/bin/python
import serial
#import syslog
import time

#The following line is for serial over GPIO
port = '/dev/ttyS0'


ard = serial.Serial(port,9600,timeout=5)

i = 0
while True:
    # Serial write section
    setTempCar1 = 63
    setTempCar2 = 37
    setTemp1 = str(setTempCar1)
    setTemp2 = str(setTempCar2)
    print ("Python value sent: ")
    print (setTemp1)
    ard.write(setTemp1)
    time.sleep(6) # with the port open, the response will be buffered
                  # so wait a bit longer for response here

    # Serial read section
    msg = ard.read(ard.inWaiting()) # read everything in the input buffer
    print ("Message from arduino: ")
    print (msg)
else:
    print ("Exiting")
exit()
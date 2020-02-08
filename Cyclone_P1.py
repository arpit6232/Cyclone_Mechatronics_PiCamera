#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pins = [29,31,33,35,37,38,40]

GPIO.setup(36, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
for pin in pins:
    GPIO.output(pin,GPIO.LOW)
print("Pin setup to low successful")

x=True
flag = 0
flag2 = 0
count = 0
while(x):
    for pin in pins:
        print(count)
        GPIO.output(pin,GPIO.HIGH)
        
        for i in range(0,150000):
            if(GPIO.input(36)==GPIO.HIGH and count==3):
                print("Presed")
                x=False
                flag = 1
                break

            if(GPIO.input(36)==GPIO.HIGH and count != 3):
                for pin in pins:
                        GPIO.output(pin,GPIO.LOW)
                x = True

        if(flag==1 and count == 3):
            print("Pressed Push Button")
            for pin in pins:
                GPIO.output(pin,GPIO.LOW)
            flag2=1
            x=False
            break
            
        GPIO.output(pin,GPIO.LOW)
        if(count<6):
            count+=1
        else:
            count=0
    
flag3=0
while(True):
    if(flag2==1):
        GPIO.output(35,GPIO.HIGH)
        time.sleep(1)
        flag3=1
        if(flag3==1):
            GPIO.output(pins,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pins,GPIO.LOW)
            time.sleep(0.5)

GPIO.cleanup()
count=-1

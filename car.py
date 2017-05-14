import RPi.GPIO as GPIO
import time

c = 0 #counter

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT) #Enabler Antriebsmotor
GPIO.setup(11,GPIO.OUT) #In1
GPIO.setup(13,GPIO.OUT) #In2

GPIO.setup(36,GPIO.OUT) #In3
GPIO.setup(38,GPIO.OUT) #In4
GPIO.setup(40,GPIO.OUT) #Enabler Lenkmotor

GPIO.output(7,GPIO.HIGH) 
GPIO.output(40,GPIO.HIGH)

def forward():
		GPIO.output(11,GPIO.LOW)
		GPIO.output(13,GPIO.HIGH)

def backward():
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(13,GPIO.LOW)

def left():
		GPIO.output(36,GPIO.HIGH)
		GPIO.output(38,GPIO.LOW)


def right():
		GPIO.output(36,GPIO.LOW)
		GPIO.output(38,GPIO.HIGH)


while c < 3:

	forward()
	time.sleep(1)
	backward()
	time.sleep(1)
	left()
	time.sleep(1)
	right()
	time.sleep(1)
	
	c += 1

GPIO.cleanup()

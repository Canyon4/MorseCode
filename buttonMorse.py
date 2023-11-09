import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
p = GPIO.PWM(19,50)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while (True):
	if (GPIO.input(26) == GPIO.HIGH):
		p.stop(0)
		
	else:
		p.start(1)

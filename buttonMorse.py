# import GPIO and time
import RPi.GPIO as GPIO
import time
# sets up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
p = GPIO.PWM(19,50)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#checks if the button is being pressed
while (True):
	if (GPIO.input(26) == GPIO.HIGH):
		p.stop(0)
# turns off buzzer if no button press
	else:
		p.start(1)

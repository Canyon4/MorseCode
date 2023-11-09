import RPi.GPIO as GPIO
import time
from pyMorseTranslator import translator

encoder = translator.Encoder()
inp = input("give input: ")
a = encoder.encode(inp).morse

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
p = GPIO.PWM(19,50)

a.split(" ")

for i in range(len(a)):

	if (a[i-1] == "."):
		p.start(1)
		time.sleep(0.5)
		p.stop(1)
		time.sleep(0.25)

	elif (a[i-1] == "-"):
		p.start(1)
		time.sleep(1)
		p.stop(1)
		time.sleep(0.25)

	elif (a[i-1] == "/"):
		time. sleep(2)

	else:
		break

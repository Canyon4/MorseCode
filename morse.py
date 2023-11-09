#imports GPIO, time, and the translator
import RPi.GPIO as GPIO
import time
from pyMorseTranslator import translator
# creates encoder, gets input from user, encodes input
encoder = translator.Encoder()
inp = input("give input: ")
a = encoder.encode(inp).morse
# sets up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
p = GPIO.PWM(19,50)
# makes string "a" into a list
a.split(" ")
# runs through "a" and checks symbol, and sends different signal to buzzer depending on the symbol.
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

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.IN)

while True:
    if GPIO.input(12) == True:
        print('in')
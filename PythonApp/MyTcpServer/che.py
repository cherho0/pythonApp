import RPi.GPIO as GPIO
import time
import threading

class che(object):
    IN1 = 11
    IN2 = 12
    IN3 = 13
    IN4 = 15

    def init(self):    
        GPIO.setmode(GPIO.BOARD)
        #GPIO.cleanup()
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)
        GPIO.setup(16,GPIO.OUT)

        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,False)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,False)
        GPIO.output(16,False)

    def qianjin(self,sleep_time):
        init()
        beep()
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        time.sleep(sleep_time)
        GPIO.cleanup()

    def cabk(self,sleep_time):
        init()
        beep()
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        time.sleep(sleep_time)
        GPIO.cleanup()

    def left(self,sleep_time):
        init()
        beep()
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,False)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        time.sleep(sleep_time)
        GPIO.cleanup()

    def right(self,sleep_time):
        init()
        beep()
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,False)
        time.sleep(sleep_time)
        GPIO.cleanup()

    def beep(self):
        try:
            t=  threading.Thread(target=be)
            t.start()
        except:
            pass
    
    
    def be(self):
        for i in range(1, 2):
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(16, GPIO.HIGH)
            time.sleep(0.5)





        
    
        

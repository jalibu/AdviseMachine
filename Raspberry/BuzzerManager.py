import RPi.GPIO as GPIO
import logging
import time
import threading
class BuzzerManager():

    def on(self, duration):
        self.active = True
        logging.info("Making noise")
        GPIO.output(self.pin, GPIO.HIGH)
        self.end = time.time() + duration
        self.thread = threading.Thread(target=self.__noiseTimer__)
        self.thread.start()
        
    def off(self):
        self.active = False
        logging.info("Be quiet")
        GPIO.output(self.pin, GPIO.LOW)
        
    def is_on(self):
        return self.active
        
    def __init__(self, pin):
        logging.info("Create Buzzer instance on " + str(pin))
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.active = False
        GPIO.output(self.pin, GPIO.LOW)
    
            
    def __noiseTimer__(self):
        while time.time() <= self.end:
            time.sleep(0.1)
        self.off()
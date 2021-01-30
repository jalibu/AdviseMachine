import RPi.GPIO as GPIO
import logging
class LedButton():

    def on(self):
        self.active = True
        logging.info("Setting LedButton: ON")
        GPIO.output(self.lightPin, GPIO.HIGH)
        
    def off(self):
        self.active = False
        logging.info("Setting LedButton: OFF")
        GPIO.output(self.lightPin, GPIO.LOW)
        
    def is_on(self):
        return self.active
        
    def __init__(self, lightPin, pushPin, onClickFunction):
        logging.info("Create LedButton instance with lightPin " + str(lightPin) + ", pushPin " + str(pushPin) + ", onClickFunction " + str(onClickFunction))
        ## Setup LED Button
        GPIO.setup(pushPin,GPIO.IN)
        GPIO.add_event_detect(pushPin,GPIO.FALLING,callback=self.__handleClickEvent__,bouncetime=200)
        GPIO.setup(lightPin, GPIO.OUT)

        self.lightPin = lightPin
        self.active = False
        self.onClickFunction = onClickFunction
        
    def __handleClickEvent__(self, pin):
        self.onClickFunction()
        
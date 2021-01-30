#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading
import logging
import RPi.GPIO as GPIO

class CoinManager(object):
    def __init__(self, pin):
        logging.info('Create CoinCounter instance')
        self.cash = 0
        self.last_pulse = None
        self.pulses = 0
        self.running = False
        # Setup coin interrupt channel
        GPIO.setup(pin,GPIO.IN)
        GPIO.add_event_detect(pin,GPIO.FALLING,callback=self.__coinEventHandler__)
        return
    
    def get_cash(self):
        return self.cash / 10.0
        
    def reset(self):
        self.cash = 0
        
    def __coinEventHandler__(self, pin):
        self.pulses += 1
        self.last_pulse = time.time()
        if(self.running == False):
            self.running = True
            self.thread = threading.Thread(target=self.__cashCollector__)
            self.thread.start()
        
    def is_processing(self):
        return self.running
            
    def __cashCollector__(self):
        while self.running:
            if(self.last_pulse != None and time.time() - self.last_pulse > 0.2):
                logging.info('Collecting ' + str(self.pulses / 10.0) + " to total of " + str(self.cash / 10.0))
                self.cash = self.cash + self.pulses
                self.pulses = 0
                self.last_pulse = None
                self.running = False
            time.sleep(0.1)
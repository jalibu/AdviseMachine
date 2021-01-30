#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading
import logging
from Adafruit_CharLCD import Adafruit_CharLCD

class LcdManager(object):
    def __init__(self):
        logging.info('Create LcdManager instance')
        self.running = False
        self.line1 = ''
        self.line2 = ''
        self.screen = Adafruit_CharLCD()
        self.spinner_state = 0
        return
    
    def get_process_spinner(self):
        if self.spinner_state == 0:
            self.spinner_state += 1
            return '.   '
        elif self.spinner_state == 1:
            self.spinner_state += 1
            return '..  '
        else:
            self.spinner_state = 0
            return '... '

    def set_line1(self, text):
        self.line1 = text
        message = self.line1
        message += ' ' * (16 - len(self.line1))
        self.screen.message(message)
        last_line1 = self.line1
    
    def set_line2(self, text):
        self.line2 = text
        message = self.line2
        message += ' ' * (16 - len(self.line2))
        self.screen.message("\n" + message)
        last_line2 = self.line2
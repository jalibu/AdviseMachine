#!/usr/bin/python
# -*- coding: utf-8 -*-

from Adafruit_Thermal import *
import Image
import logging

class PrinterManager(object):
    def __init__(self):
        self.printer = printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
        return
    
    def feed(self, count):
        self.printer.feed(count)
    
    def print_str(self, message, **kwargs):
        logging.info("Sending message to Printer: " + message)
        
        # Are there special Options?
        if(kwargs and kwargs.get('justify')):
            if(kwargs.get('justify') in ['C', 'R', 'L']):
                self.printer.justify(kwargs['justify'])
            else:
                logging.warning("Warning: Illegal value for justify option: " + kwargs.get('justify'))
                
        if(kwargs and kwargs.get('size')):
            if(kwargs.get('size') in ['S', 'M', 'L']):
                logging.info("Size text: " + kwargs.get('size'))
                self.printer.setSize(kwargs.get('size'))
            else:
                logging.warning("Warning: Illegal value for size option: " + kwargs['size'])
                
        if(kwargs and kwargs.get('lineHeight')):
            if(24 <= kwargs.get('lineHeight') <= 64):
                logging.info("Size text: " + str(kwargs.get('lineHeight')))
                self.printer.setLineHeight(kwargs.get('lineHeight'))
            else:
                logging.warning("Warning: Illegal value for lineHeight option (min 24, max 64): " + str(kwargs['lineHeight']))
                
        if(kwargs and kwargs.get('bold')):
            logging.info("Make text bold")
            self.printer.boldOn()
            
        # Print it
        self.printer.println(self.prepare_message(message))
        
        # Reset values
        self.printer.justify('L')
        #self.printer.setSize('S')
        self.printer.boldOff()
        self.printer.setLineHeight(32)
        
    def print_img(self, path, **kwargs):
        img = Image.open(path)
        if(kwargs.get('width')):
            basewidth = kwargs.get('width')
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        
        self.printer.printImage(img, True)
    
    def prepare_message(self, messageRaw):
        words_list = messageRaw.split()
        lineLength = 0
        message = ''
        for word in words_list:
            if(lineLength == 0):
                message = message + word
                lineLength = lineLength + len(word)
            elif(lineLength + len(word) + 1 < 29):
                message = message + ' ' + word
                lineLength = lineLength + len(word)
            else:
                message = message + '\n' + word
                lineLength = len(word)
    
        message = message.decode('utf-8').encode('utf-8')
        message_unicode = unicode(message, "utf-8" )
        return message_unicode.encode('cp437')
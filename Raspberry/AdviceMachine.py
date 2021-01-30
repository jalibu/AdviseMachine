# -*- coding: utf-8 -*-
#!/usr/bin/python

from LcdManager import LcdManager
from CoinManager import CoinManager
from LedButton import LedButton
from HintsManager import HintsManager
from PrinterManager import PrinterManager
from BuzzerManager import BuzzerManager
import time
import logging
import signal
import RPi.GPIO as GPIO
import sys
import Utils

PIN_LED_LIGHT = 17
PIN_LED_BUTTON = 3
PIN_COIN = 23
PIN_BUZZER = 25
PRICE = 0.5

coinManager = None
ledButton = None
lcdManager = None
hintsManager = None
printerManager = None
lastPrint = None
buzzerManager = None

# main function
def main():
    global lcdManager
    global ledButton
    global coinManager
    global hintsManager
    global printerManager
    global lastPrint
    global buzzerManager
    
    logging.basicConfig(level=logging.INFO)
    logging.info('Start the engines...')
    
    lcdManager = LcdManager()
    lcdManager.set_line1("Pfadi Weisheiten")

    coinManager = CoinManager(PIN_COIN)
    ledButton = LedButton(PIN_LED_LIGHT, PIN_LED_BUTTON, handleClick)
    hintsManager = HintsManager()
    printerManager = PrinterManager()
    buzzerManager = BuzzerManager(PIN_BUZZER)
    lastPrint = None
    ledButton.off()
    
    # Add signal handler
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        if coinManager.is_processing():
            lcdManager.set_line2('Cash ' + lcdManager.get_process_spinner() + ' EUR')
        elif coinManager.get_cash() > 0:
            lcdManager.set_line2('Cash {0:.2f} EUR'.format(coinManager.get_cash()))
        else:
            lcdManager.set_line2("Ab {0:.2f} EUR".format(PRICE))
            
        if(coinManager.get_cash() >= PRICE and not ledButton.is_on()):
            buzzerManager.on(0.3)
            ledButton.on()
        time.sleep(0.2)
        
    lcdManager.stop()
    logging.info('Finished')
    
def handleClick():
    pushTime = 0
    while 1:
        if(GPIO.input(PIN_LED_BUTTON) == 0):
            pushTime = pushTime + 1
            time.sleep(1)
        else:
            break;
        
    if(coinManager.get_cash() >= PRICE):
        ledButton.off()
        buzzerManager.on(0.2)
        cashBuffer = coinManager.get_cash()
        coinManager.reset()
        print_msg(hintsManager.get_hint(), cashBuffer)
        lcdManager.set_line1("Druck gestartet.")
        lcdManager.set_line2("Bitte warten!")
        time.sleep(8)
        
def print_msg(msg, cash):
    global lastPrint
    global coinManager
    if(lastPrint == None or time.time() - lastPrint > 10):
        lastPrint = time.time()
        imgPath = Utils.get_script_path() + 'images/pfadi.png'
        printerManager.print_img(imgPath)
        printerManager.print_str("Jeder Pfadfinder weiß:", bold=True, lineHeight=36)
        printerManager.feed(1)
        #printerManager.print_str('_______________________________')
        printerManager.print_str(msg)
        printerManager.print_str('_______________________________')
        printerManager.feed(1)
        printerManager.print_str('Die Haßlocher Pfadfinder bedanken sich herzlich für deine Spende über {0:.2f} Euro.'.format(cash))
        printerManager.feed(1)
        printerManager.print_str('Mehr Infos über uns auf:\nwww.vcp-hassloch.de')
        printerManager.feed(1)
        #printerManager.print_str('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
        #printerManager.feed(2)
        #printerManager.print_str('* * *  G U T S C H E I N  * * *')
        #printerManager.feed(1)
        #printerManager.print_str('Für 0,50 EUR beim Kauf eines Kinderpunschs oder Glühweins am Stand der Pfadfinder.')
        printerManager.feed(3)
    
def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

if __name__=="__main__":
    main()

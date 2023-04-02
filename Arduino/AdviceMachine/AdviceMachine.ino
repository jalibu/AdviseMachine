// (c) Jalibu 2023
// https://github.com/jalibu

// Include Libraries
#include "Wire.h"
#include "LiquidCrystal_I2C.h"
#include "Adafruit_Thermal.h"
#include "SoftwareSerial.h"
#include "pitches.h"
#include "LogoRepaircafe.h"

// Setup pins
#define BUZZER_PIN 6
#define BUTTON_INPUT_PIN 4
#define BUTTON_LED_PIN 8
#define COIN_IMPULSE_PIN 0 // Interrupt 0 = PIN 2
#define PRINTER_TX_PIN 12 // Arduino transmit  YELLOW WIRE  labeled RX on printer
#define PRINTER_RX_PIN 10 // Arduino receive   GREEN WIRE   labeled TX on printer

// Other settings
#define PRICE 1.00

LiquidCrystal_I2C lcd(0x27, 16, 2);
SoftwareSerial mySerial(PRINTER_RX_PIN, PRINTER_TX_PIN);
Adafruit_Thermal printer(&mySerial);

volatile long lastCoinImpulse = 0;
volatile int numberOfImpulses = 0;
volatile float cash = 0.00;
volatile long printStarted = 0;

void setup() {
  Serial.begin(9600);
  Serial.println(F("Start setup phase..."));

  mySerial.begin(19200);  // Initialize SoftwareSerial
  printer.begin();

  pinMode(BUTTON_INPUT_PIN, INPUT);
  pinMode(BUTTON_LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  lcd.init();
  lcd.clear();
  lcd.backlight();
  lcd.begin(16, 2);
  attachInterrupt(COIN_IMPULSE_PIN, handleCoinImpulse, RISING);
  
  Serial.println(F("Finished setup phase..."));
}

void printMessage() {
  printStarted = millis();
  updateLcd();
  printer.printBitmap(320, 102, logo);
  printer.feed(2);
  printer.print("Wir bedanken uns fuer deine\nSpende von " + String(cash) + " EUR.");
  printer.feed(2);
  printer.printBitmap(240, 240, qrcode);
  printer.feed(2);
}

void handleCoinImpulse() {
  lastCoinImpulse = millis();
  numberOfImpulses++;
  Serial.println("Received pulse..");
}


void handleCash() {
  if (lastCoinImpulse != 0 && millis() - lastCoinImpulse >= 200) {
    playCoinSound();
    volatile float earnedCredits = 0.0;
    Serial.println("Impulse finished with: " + String(numberOfImpulses));
    if (numberOfImpulses == 1) {
      earnedCredits = 0.1;
    } else if (numberOfImpulses ==  2) {
      earnedCredits = 0.2;
    }  else if (numberOfImpulses == 3) {
      earnedCredits = 0.5;
    }  else if (numberOfImpulses == 4) {
      earnedCredits = 1.0;
    }  else if ( numberOfImpulses == 5) {
      earnedCredits = 2.0;
    }   else {
      Serial.println("Unknown number of impulses: " + String(numberOfImpulses));

    }
    Serial.println("Adding " + String(earnedCredits) + " to cash. Old: " + String(cash) + ", New: " + String(cash + earnedCredits));
    cash = cash + earnedCredits;
    numberOfImpulses = 0;
    lastCoinImpulse = 0;
  }
}

void switchLed(boolean switchOn) {
  if (switchOn) {
    digitalWrite(BUTTON_LED_PIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  } else {
    digitalWrite(BUTTON_LED_PIN, LOW);   // turn the LED off
  }
}

void playCoinSound() {
  tone(BUZZER_PIN, NOTE_B5, 100);
  delay(100);
  tone(BUZZER_PIN, NOTE_E6, 850);
  delay(400);
  noTone(BUZZER_PIN);
}

void handleButton() {
  if (cash >= PRICE) {
    switchLed(true);
    if (digitalRead(BUTTON_INPUT_PIN) == HIGH) {
      Serial.println("Pressed the button");
      switchLed(false);
      printMessage();
      cash = 0.0;
    }
  } else {
    switchLed(false);
  }
}

void updateLcd() {
  if (printStarted != 0 && millis() - printStarted <= 5000) {
    lcd.setCursor(0, 0);
    lcd.print("Wird gedruckt.   ");
    lcd.setCursor(0, 1);
    lcd.print("Bitte warten...   ");
  } else if (cash == 0.0) {
    lcd.setCursor(0, 0);
    lcd.print("Repair-Cafe     ");
    lcd.setCursor(0, 1);
    lcd.print("    Bedank-O-Mat");
  } else {
    lcd.setCursor(0, 1);
    lcd.print("Cash: " + String(cash) + " EUR  ");
  }
}

void loop() {
  handleCash();
  handleButton();
  updateLcd();
  delay(10);
}

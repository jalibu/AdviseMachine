
// Include Libraries
#include "Wire.h"
#include "Adafruit_LiquidCrystal.h"
#include "Adafruit_Thermal.h"
#include "SoftwareSerial.h"
#include "sprueche.h"
#include "pfadi.h"
#include "pitches.h"  // must include open source pitches.h found online in libraries folder

// Setup pins
#define BUTTON_PIN 7
#define BUZZER_PIN 8
#define BUTTON_LED_PIN 9
#define COIN_IMPULSE_PIN 0 // Interrupt 0 = PIN 2
#define PRICE 0.10
#define NOTE_SUSTAIN 100

#define LCD_PINS 12,11,5,4,3,6
Adafruit_LiquidCrystal lcd(LCD_PINS);

#define PRINTER_TX_PIN 13 // Arduino transmit  YELLOW WIRE  labeled RX on printer
#define PRINTER_RX_PIN 10 // Arduino receive   GREEN WIRE   labeled TX on printer
  SoftwareSerial mySerial(PRINTER_RX_PIN, PRINTER_TX_PIN);
  Adafruit_Thermal printer(&mySerial);     // Pass addr to printer constructor

volatile long lastCoinImpulse = 0;
volatile int numberOfImpulses = 0;
volatile float cash = 0.00;    

volatile long lastCheckPaper = 0;

volatile long printStarted = 0;

void setup() {
  Serial.begin(9600); 

  Serial.println(F("Start setup phase..."));

Serial.println(F("Initialize printer"));
mySerial.begin(19200);  // Initialize SoftwareSerial
printer.begin();
printer.setCharset(CHARSET_GERMANY);


  Serial.println(F("Set BUTTON_PIN"));
  pinMode(BUTTON_PIN, INPUT);
Serial.println(F("Set BUTTON_LED_PIN"));
    pinMode(BUTTON_LED_PIN, OUTPUT);
    
    Serial.println(F("Set BUZZER_PIN"));
  pinMode(BUZZER_PIN, OUTPUT);

  Serial.println(F("Setup LCD with 16 cols in 2 rows"));
  lcd.begin(16, 2);

  attachInterrupt(COIN_IMPULSE_PIN, handleCoinImpulse, RISING); 
  Serial.println(F("Finished setup phase..."));  
}

void checkPaper(boolean force){
  if(force || lastCheckPaper == 0 || millis() - lastCheckPaper >= 300000){
    Serial.println("Has Paper? " + String(printer.hasPaper()));
    lastCheckPaper = millis();
  }
}

void printMessage(){
  printStarted = millis();
  updateLcd();
  //printer.println(String(cash));
  String spruch = getSpruch();
  Serial.println("Spruch: " + spruch);
  //printer.println(spruch);
  printer.printBitmap(280, 205+, pfadi);
}

void handleCoinImpulse(){
lastCoinImpulse = millis();
numberOfImpulses++;
Serial.println("Received pulse..");
}

void handleCash(){
  
    if(lastCoinImpulse != 0 && millis() - lastCoinImpulse >= 200){
      playCoinSound();
      volatile float earnedCredits = 0.0;
    Serial.println("Impulse finished with: " + String(numberOfImpulses));
    if(numberOfImpulses == 1){
      earnedCredits = 0.1;
    } else if(numberOfImpulses ==  2){
      earnedCredits = 0.2;
     }  else if(numberOfImpulses == 5){
      earnedCredits = 0.5;
     }  else if(numberOfImpulses == 10){
      earnedCredits = 1.0;
     }  else if( numberOfImpulses ==20){
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

void switchLed(boolean switchOn){
  if(switchOn){
    digitalWrite(BUTTON_LED_PIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  } else {
    digitalWrite(BUTTON_LED_PIN, LOW);   // turn the LED off
  }
}

void playCoinSound(){
   tone(BUZZER_PIN,NOTE_B5,100);
  delay(100);
  tone(BUZZER_PIN,NOTE_E6,850);
  delay(400);
  noTone(BUZZER_PIN);
}

void playPrintSound(){
  int melody[] = {
  NOTE_C4, NOTE_F4, NOTE_C4, NOTE_F3, NOTE_C4, NOTE_F4, NOTE_C4,
  NOTE_C4, NOTE_F4, NOTE_C4, NOTE_F4,
  NOTE_A4, NOTE_G4, NOTE_F4, NOTE_E4, NOTE_D4, NOTE_CS4,
  NOTE_C4, NOTE_F4, NOTE_C4, NOTE_F3, NOTE_C4, NOTE_F4, NOTE_C4,
  NOTE_F4, NOTE_D4, NOTE_C4, NOTE_AS3,
  NOTE_A3, NOTE_G3, NOTE_F3};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  4, 4, 4, 4, 4, 4, 2,
  4, 4, 4, 4,
  3, 8, 8, 8, 8, 8,
  4, 4, 4, 4, 4, 4, 2,
  3, 8, 4, 4,
  4, 4, 4 , 0};
  for (int thisNote = 0; noteDurations[thisNote] != 0; thisNote++) {
    int noteDuration = 2000/noteDurations[thisNote];
    tone(BUZZER_PIN, melody[thisNote],noteDuration * 0.9);
  delay(noteDuration);
  Serial.println("SND");
  }
  noTone(BUZZER_PIN);
}

void handleButton(){
  if(cash >= PRICE){
  switchLed(true);
  if(digitalRead(BUTTON_PIN) == HIGH){
    Serial.println("Pressed the button");
    switchLed(false);
    printMessage();
    cash = 0.0;
    playPrintSound();
    } 
  } else {
    switchLed(false);
  }
}

void updateLcd(){
  if(printStarted != 0 && millis() - printStarted <= 5000){
        lcd.setCursor(0,0);
    lcd.print("Wird gedruckt.   ");
    lcd.setCursor(0,1);
    lcd.print("Bitte warten...   ");
  } else if(cash == 0.0){
    lcd.setCursor(0,0);
    lcd.print("Pfadi Weisheiten");
    lcd.setCursor(0,1);
    lcd.print("Ab " + String(PRICE) + " EUR     ");
  } else {
    lcd.setCursor(0,1);
    lcd.print("Cash: " + String(cash) + " EUR");
  }
}

void loop() {
handleCash();

handleButton();
updateLcd();
checkPaper(false);
delay(10);
}

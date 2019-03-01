import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
GPIO.setwarnings(False)

# Configure the LCD
lcd = CharLCD(pin_rs = 19, pin_rw = None, pin_e = 16, pins_data = [21,18,23,24],
              numbering_mode = GPIO.BOARD, cols=16, rows=2, dotsize=8)
#lcd = CharLCD(pin_rs = 10, pin_rw = None, pin_e = 23, pins_data = [9,24,11,8], numbering_mode = GPIO.BCM)

while(True):
    lcd.clear()
    lcd.write_string("Marco Campos' \nOffice")
    time.sleep(1)
    lcd.write_string("Skype Status: ")
    time.sleep(1)

lcd.close()
GPIO.cleanup()

import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

# Configure the LCD
#lcd = CharLCD(pin_rs = 19, pin_rw = None, pin_e = 16, pins_data = [21,18,23,24], numbering_mode = GPIO.BOARD)
lcd = CharLCD(pin_rs = 10, pin_rw = None, pin_e = 23, pins_data = [9,24,11,8], numbering_mode = GPIO.BCM)

number = 0

# Main loop
while(True):
# Increment the number and then print it to the LCD number = number + 1
    lcd.clear()
    lcd.write_string("hi")
    time.sleep(1)

lcd.close()
GPIO.cleanup()
import RPi.GPIO as GPIO
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# lcd_rs = digitalio.DigitalInOut(board.D26)
# lcd_en = digitalio.DigitalInOut(board.D19)
# lcd_d7 = digitalio.DigitalInOut(board.D27)
# lcd_d6 = digitalio.DigitalInOut(board.D22)
# lcd_d5 = digitalio.DigitalInOut(board.D24)
# lcd_d4 = digitalio.DigitalInOut(board.D25)

lcd_rs = 26
lcd_en = 19
lcd_d7 = 27
lcd_d6 = 22
lcd_d5 = 24
lcd_d4 = 25

GPIO.setup(lcd_rs, GPIO.OUT)
GPIO.setup(lcd_en, GPIO.OUT)
GPIO.setup(lcd_d7, GPIO.OUT)
GPIO.setup(lcd_d6, GPIO.OUT)
GPIO.setup(lcd_d5, GPIO.OUT)
GPIO.setup(lcd_d4, GPIO.OUT)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

lcd.message = "Hello\nCircuitPython!"
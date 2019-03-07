import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
import requests, json
from pprint import pprint
import harvesine as hv
import fetch_weather as fw

GPIO.setwarnings(False)

# Configure the LCD
cols = 16
rows = 2
lcd = CharLCD(pin_rs = 19, pin_rw = None, pin_e = 16, pins_data = [21,18,23,24],
              numbering_mode = GPIO.BOARD, cols=cols, rows=rows, dotsize=8)
#lcd = CharLCD(pin_rs = 10, pin_rw = None, pin_e = 23, pins_data = [9,24,11,8], numbering_mode = GPIO.BCM)

api_key = "19c2e8d2c714c0c7423d8126fe94224f"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
city_name = 'boston'
units = 'imperial'

complete_url = base_url + city_name + "&units=" + units + "&appid=" + api_key
response = requests.get(complete_url)
x = response.json()

wait_time = 3
temperature = int(round(fw.fetch_weather(x)))
day_status = hv.day_status(temperature)

message01 = "This is Marco's"
message11 = "room" 
pos01 = hv.center_cursor(message01, cols)
pos11 = hv.center_cursor(message11, cols)

message02 = str("It is so " + day_status)
message12 = str("in " + city_name.capitalize() + " today")
pos02 = hv.center_cursor(message02, cols)
pos12 = hv.center_cursor(message12, cols)

message03 = "We are at"
message13 = str(str(temperature)+" degrees F")
pos03 = hv.center_cursor(message03, cols)
pos13 = hv.center_cursor(message13, cols)

while(True):
    lcd.clear()
    lcd.cursor_pos = (0, pos01)
    lcd.write_string(message01)
    lcd.cursor_pos = (1, pos11)
    lcd.write_string(message11)
    time.sleep(wait_time)
    lcd.clear()
    lcd.cursor_pos = (0, pos02)
    lcd.write_string("It is so " + day_status)
    lcd.cursor_pos = (1, pos12)
    lcd.write_string("in " + city_name.capitalize() + " today")
    time.sleep(wait_time)
    lcd.clear()
    lcd.cursor_pos = (0, pos03)
    lcd.write_string(message03)
    lcd.cursor_pos = (1, pos13)
    lcd.write_string(str(temperature) + " degrees F")
    time.sleep(wait_time)

lcd.close()
GPIO.cleanup()

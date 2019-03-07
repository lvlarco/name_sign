import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
import requests, json
from pprint import pprint
import harvesine as hv
import fetch_weather as fw

GPIO.setwarnings(False)

# Configure the LCD
lcd = CharLCD(pin_rs = 19, pin_rw = None, pin_e = 16, pins_data = [21,18,23,24],
              numbering_mode = GPIO.BOARD, cols=16, rows=2, dotsize=8)
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

while(True):
    lcd.clear()
   # lcd.cursor_pos = (0,5)
    lcd.write_string("This is Marco's\n room")
    time.sleep(wait_time)
    lcd.clear()
    lcd.write_string("It is so " + day_status + "\r\nin " + city_name.capitalize() + " today")
    time.sleep(wait_time)
    lcd.clear()
    lcd.write_string('We are at\r\n' + str(temperature) + ' degrees F')
    time.sleep(wait_time)

lcd.close()
GPIO.cleanup()

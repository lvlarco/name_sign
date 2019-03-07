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
lcd = CharLCD(pin_rs = 10, pin_rw = None, pin_e = 23, pins_data = [9,24,11,8], numbering_mode = GPIO.BCM)

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

message1 = "This is Marco's"
pos1 = hv.center_cursor(message1, cols)
message2 = str("It is so " + day_status)
pos2 = hv.center_cursor(message2, cols)
message3 = "We are at\n"
pos3 = hv.center_cursor(message3, cols)

while(True):
    lcd.clear()
    lcd.cursor_pos = (0, pos1)
    lcd.write_string(message1 + '\nroom')
    time.sleep(wait_time)
    lcd.clear()
    lcd.cursor_post = (0, pos2)
    lcd.write_string("It is so " + day_status + "\nin " + city_name.capitalize() + " today")
    time.sleep(wait_time)
    lcd.clear()
    lcd.cursor_post = (0, pos3)
    lcd.write_string(message3 + str(temperature) + ' degrees F')
    time.sleep(wait_time)

lcd.close()
GPIO.cleanup()

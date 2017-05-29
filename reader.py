from SimpleCV import Color,Camera,Display
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
cam = Camera()
display = Display()

def blink(): 
  GPIO.output(17, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(17, GPIO.LOW) 

def post_request(input_method, barcode):
  payload = { 'method': input_method, 'upc':  barcode }
  r = requests.post('http://localhost:3000/api', data=payload)
  print r.status_code
  

while(display.isNotDone()):

  input_method = 'add' if GPIO.input(17) else 'remove'
  img = cam.getImage()
  barcode = img.findBarcode()

  if(barcode is not None):
    barcode = barcode[0]
    result = str(barcode.data)
    print 'Barcode found:'
    print result 
    post_request(input_method, barcode)
    blink()  
    barcode = []
  print 'None'
  img.save(display)

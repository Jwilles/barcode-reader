from SimpleCV import Color,Camera,Display
import requests
import RPi.GPIO as GPIO
import time

# GPIO init 
method_pin = 17
blink_pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(method_pin, GPIO.IN)
GPIO.setup(blink_pin, GPIO.OUT)

#SimpleCV init 
cam = Camera()
display = Display()

# Blink LED 
def blink(): 
  GPIO.output(blink_pin, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(blink_pin, GPIO.LOW) 

# Post to web app with upc
def post_request(input_method, barcode):
  payload = { 'method': input_method, 'upc':  barcode }
  r = requests.post('http://localhost:3000/api', data=payload)
  print r.status_code
  

while(display.isNotDone()):
  
  # Check if method pin is high and set input method
  input_method = 'add' if GPIO.input(method_pin) else 'remove'
  
  # Grab frame from cam and check for barcode 
  img = cam.getImage()
  barcode = img.findBarcode()

  # Process barcode if found
  if(barcode is not None):
    barcode = barcode[0]
    result = str(barcode.data)
    print 'Barcode found:'
    print result 
    post_request(input_method, barcode)
    blink()  
    barcode = []
  else:
    print 'None'
  # Display frame
  img.save(display)

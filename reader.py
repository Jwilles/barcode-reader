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

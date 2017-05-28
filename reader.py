from SimpleCV import Color,Camera,Display

cam = Camera()
display = Display()

while(display.isNotDone()):

  img = cam.getImage()
  barcode = img.findBarcode()
  if(barcode is not None):
    barcode = barcode[0]
    result = str(barcode.data)
    print 'test'
    print result 
    barcode = []
  print 'None'
  img.save(display)

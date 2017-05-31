# Raspberry Pi Camera Barcode Reader 

This is a script intended to run on a Raspberry Pi as a camera-based barcode reader interfacing with a web app for grocery management. 
The reader is built using the [SimpleCV](http://simplecv.org/) framework for [OpenCV](http://opencv.org/) and the [Zbar](http://zbar.sourceforge.net/) barcode reading library. Once read, the UPC code and input method are sent to the web app using [Requests](http://docs.python-requests.org/en/master/).  



## RPi with indicator light and add/remove item selection

![Alt text](/pics/circuit-diagram.png?raw=true "RPi Circuit")
      

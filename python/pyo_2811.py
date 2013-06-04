from pyo import *
import serial
import time

teensy = serial.Serial('/dev/ttyACM0', 115200)
led_list = []
numleds = 60

s = Server(duplex=0).boot()
a = SuperSaw(freq=[100,2000], detune=0.6, bal=0.7, mul=0.5).out()
#l = Linseg([(0,20),(2,15000)], loop=True)
#a = Sine(freq=[l,1000], mul=1).out()
#l.play()

def tolist(x):
    global led_list
    for led in range(numleds):
        #red is left channel
        led_list.append(255-x[0][led][1])
        led_list.append(0)
        #green is right channel
        led_list.append(255-x[1][led][1])
    teensy.write(bytearray(led_list))
    led_list = []

spec = Spectrum(a, size=1024, function=tolist)
spec.setWidth(numleds)
spec.setHeight(255)
s.start()


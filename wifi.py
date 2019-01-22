import machine
import network
import time
lampu = machine.Pin(2, machine.Pin.OUT)
ap = 'MG'
password = 'everyoneispartofmg'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
lampu.low()
wlan.connect(ap, password)
if wlan.isconnected:
   for i in range(10):
      lampu.high()
      time.sleep(0.5)
      lampu.low()
      time.sleep(0.5)

lampu.high()

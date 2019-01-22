import machine
import network
import time
from umqtt.simple import MQTTClient
import ubinascii

topic = b"esp"
        
ap = 'MG'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
password = 'everyoneispartofmg'
server = 'm16.cloudmqtt.com'
wlan.connect(ap, password)
state = 0

def sub_cb(topic, msg):
    global state
    lampu = machine.Pin(2, machine.Pin.OUT)
    print((topic, msg))
    if msg == b"on":
       lampu.value(0)
       state = 1
    elif msg == b"off":
       lampu.value(1)
       state = 0

def main():
   client_id = b"esp8266"
   c = MQTTClient(client_id , server, port = 19998, user='zqrauhzm', password='WTWTREkXeBLb')
   c.set_callback(sub_cb)
   c.connect()
   c.subscribe(topic)

   try:
      while 1:
          c.wait_msg()
   finally:
       c.disconnect()

if __name__ == "__main__":
     main()

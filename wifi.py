import machine
import network
import time
from umqtt.simple import MQTTClient
import ubinascii

topic = b"esp"
        
#ap = 'MG'
#password = 'everyoneispartofmg'
ap = 'Almebila'
password = 'b1l@@lmes@1r@'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
server = 'm16.cloudmqtt.com'
wlan.connect(ap, password)
state = 0

def sub_cb(topic, msg):
    global state
    lampu = machine.Pin(2, machine.Pin.OUT)
    print((topic, msg))
    if msg == b"blinking":
       berkelip()
    if msg == b"on":
       lampu.value(0)
       state = 1
    elif msg == b"off":
       lampu.value(1)
       state = 0
def berkelip():
    lampu = machine.Pin(2, machine.Pin.OUT)
    for i in range(10):
	lampu.high()
	time.sleep(0.5)
	lampu.low()
	time.sleep(0.5)
        lampu.high()

def main():
   client_id = b"esp8266"
   c = MQTTClient(client_id , server, port = 19998, user='zqrauhzm', password='WTWTREkXeBLb')
   c.set_callback(sub_cb)
   c.connect()
   c.subscribe(topic)
   c.publish(b"rec", str(wlan.ifconfig()))
   c.publish(b"status", "TERHUBUNG")
   c.publish(b"statusindi", "rgb(49,195,0)")
   try:
      while 1:
          c.wait_msg()
   finally:
       c.disconnect()

if __name__ == "__main__":
     main()

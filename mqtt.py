import network
from umqtt.simple import MQTTClient
import machine
lampu = machine.Pin(2, machine.Pin.IN)
topic = b"esp"
clientid = "esp1"
server = "m16.cloudmqtt.com"
port = "19998"
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.connect('Almebila', 'b1l@@lmes@1r@') # connect to an AP
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses
if wlan.isconnected():
   lampu.value(0)
c = MQTTClient(clientid, server, port, user='zqrauhzm', password='WTWTREkXeBLb')
c.connect()
c.subscribe(topic)
print("Connected to %s, subscribed to %s topic" % (server, topic))

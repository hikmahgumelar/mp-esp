import network
import machine

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

lampu = machine.Pin(2, machine.Pin.OUT)
sta_if.active(True)
sta_if.connect('Almebila','b1l@@lmes@1r@')
if sta_if.isconnected():
   lampu.value(1)
   sta_if.ifconfig

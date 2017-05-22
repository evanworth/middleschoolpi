from gpiozero import LED
from time import sleep
from signal import pause

led yellow = LED(10)
ledgreen = LED(11)
ledred = LED(9)

while True:
    ledred.on()
    ledyellow.on()
    ledgreen.on()
    sleep(1)
    ledred.off()
    ledyellow.off()
    ledgreen.off()
    sleep(1)

import board
import busio
import digitalio
import time

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
import adafruit_rfm9x
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 868.0)
import random

while True:
    meas=random.randint(10,20)
    rfm9x.send(str(meas))
    time.sleep(5)


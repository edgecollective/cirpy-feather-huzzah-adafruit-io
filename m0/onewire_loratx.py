import board
import busio
import digitalio
import time
from adafruit_onewire.bus import OneWireBus

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
import adafruit_rfm9x
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 868.0)

ow_bus=OneWireBus(board.D5)
devices=ow_bus.scan()
import adafruit_ds18x20
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])

while True:
    temp=ds18b20.temperature
    rfm9x.send(str(temp))
    time.sleep(5)

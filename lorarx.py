import board
import busio
import digitalio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.GPIO15)
reset = digitalio.DigitalInOut(board.GPIO2)
import adafruit_rfm9x
#rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 868.0)
#rfm9x.send('Hello world!')
while True:
    packet = rfm9x.receive()
    packet_text = str(packet, 'ascii')
    print('Received (ASCII): {0}'.format(packet_text))
    rssi = rfm9x.rssi
    print('Received signal strength: {0} dB'.format(rssi))

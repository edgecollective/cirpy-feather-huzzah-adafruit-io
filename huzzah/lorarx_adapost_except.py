import board
import busio
import digitalio
import urequests

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.GPIO0)
reset = digitalio.DigitalInOut(board.GPIO2)
import adafruit_rfm9x
#rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 868.0)
#rfm9x.send('Hello world!')

headers={'Content-Type': 'application/json','X-AIO-Key':'3515b3ecee734780927d7f4ab1654917'}
url='https://io.adafruit.com/api/v2/donblair/feeds/goof-test/data.json'
#json=dict(foo='13.2')
#json=dict(foo='13.2)

def post(json):
    r=urequests.post(url,json=json,headers=headers)
    return r
    
def listen():
    while True:
        packet = rfm9x.receive(timeout=5.0)
        if packet is None:
            print("Listening ...")
        else:
            packet_text = str(packet, 'ascii').strip()
            print('Received (ASCII): {0}'.format(packet_text))
            rssi = rfm9x.rssi
            print('Received signal strength: {0} dB'.format(rssi))
            print('Sending to adafruit.io ...')
            json=dict(value=packet_text)
            try:
                post(json)
            except Exception as exc:
                print ('feck it!')
            

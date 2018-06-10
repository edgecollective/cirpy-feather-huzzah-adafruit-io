import urequests

headers={'Content-Type': 'application/json','X-AIO-Key':'3515b3ecee734780927d7f4ab1654917'}
url='https://io.adafruit.com/api/v2/donblair/feeds/goof-test/data.json'
#json=dict(foo='13.2')

def post(json):
    r=urequests.post(url,headers=headers,json=json)
    return r


#!/bin/sh

curl -H 'X-AIO-Key: 3515b3ecee734780927d7f4ab1654917' -H 'Content-Type: application/json' -X POST https://io.adafruit.com/api/v2/donblair/feeds/goof-test/data.json -d'{"value": 17}'

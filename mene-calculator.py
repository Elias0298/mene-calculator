from decimal import *
import urllib.request, json

## Decimals && Variables ##
getcontext().prec = 3
url = 'https://s3.amazonaws.com/dolartoday/data.json'
mene = 1/100000000

## API ##
with urllib.request.urlopen(url) as api:
    data = json.loads(api.read().decode())
    usd_bolivar = (data['USD']['transferencia'])
    price_petro = (data['MISC']['petroleo'])
    price_petro = float(price_petro.replace(',','.'))

## mene => usd => bolivar ##
mene_to_usd = price_petro * mene
mene_to_bolivar = Decimal(mene_to_usd) * Decimal(usd_bolivar)

print("Un mene es igual a: {} bsf o ${}".format(mene_to_bolivar, mene_to_usd))

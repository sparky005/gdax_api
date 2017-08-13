from gdax_api import Client

client = Client()
print(client.get_product_ticker('BTC-USD'))

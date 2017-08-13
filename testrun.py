from gdax_api import PublicClient

client = PublicClient()
print(client.get_product_ticker('BTC-USD'))

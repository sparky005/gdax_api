from gdax_api import Client

client = Client()
print(client.get_product_order_book('BTC-USD', 1))


"""GDAX Public client"""
import requests

class PublicClient(object):
    def __init__(self):
        self.api = 'https://api.gdax.com'
        pass

    def get_products(self):
        r = requests.get(self.api + '/products')
        return r.json()

    def get_product_order_book(self, product, level):
        r = requests.get(self.api + '/products/' + product + '/book', data={'level': level})
        return r.json()

    def get_product_ticker(self, product):
        r = requests.get("{}/products/{}/ticker".format(self.api, product))
        return r.json()

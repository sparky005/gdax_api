"""GDAX Public client"""
import requests

class PublicClient(object):
    def __init__(self):
        self.api = 'https://api.gdax.com'
        pass

    def get_products(self):
        r = requests.get('{}/products'.format(self.api))
        return r.json()

    def get_product_order_book(self, product, level=1):
        r = requests.get('{}/products/{}/book'.format(self.api, product), data={'level': level})
        return r.json()

    def get_product_ticker(self, product):
        r = requests.get("{}/products/{}/ticker".format(self.api, product))
        return r.json()

    def get_trades(self, product):
        r = requests.get("{}/products/{}/trades".format(self.api, product))
        return r.json()

    def get_historic_rates(self, product, start=None, end=None, granularity=None):
        r = requests.get("{}/products/{}/candles".format(self.api, product),
                        data={'start': start, 'end': end,
                            'granularity': granularity})
        return r.json()

    def get_stats(self, product):
        r = requests.get("{}/products/{}/stats".format(self.api, product))
        return r.json()

    def get_currencies(self):
        r = requests.get("{}/currencies".format(self.api))
        return r.json()

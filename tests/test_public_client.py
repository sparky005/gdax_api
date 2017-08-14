import pytest
from gdax_api import PublicClient
import vcr 
###################################
# Actual tests:
# ok now we're actually testing
###################################

class TestPublicClient(object):

    @vcr.use_cassette('tests/cassettes/products.yml')
    def test_get_products(self, client, product_keys):
        """Test API call to get available products"""
        response = client.get_products()
    
        assert isinstance(response, list), "Response should be a list"
        assert isinstance(response[0], dict), "First element should be a dict"
        assert set(product_keys).issubset(response[0].keys()), "Product dict should contain the following keys: {}".format(product_keys)
    
    
    @vcr.use_cassette('tests/cassettes/product_order_book.yml')
    def test_get_product_order_book(self, client, product, product_order_book_keys):
        """Test API call to get orders for single product"""
        response = client.get_product_order_book(product, 3)
    
        assert isinstance(response, dict), "Order book should be a dict"
        assert set(product_order_book_keys).issubset(response.keys()), "Order book dict should contain the following keys: {}".format(product_order_book_keys)
        assert isinstance(response['sequence'], int), "Sequence must be in"
        assert isinstance(response['bids'], list), "Bids should be a list"
        assert isinstance(response['asks'], list), "Asks should be a list"
    
    
    @vcr.use_cassette('tests/cassettes/product_ticker.yml')
    def test_get_product_ticker(self, client, product, product_ticker_keys):
        """Test API call to product ticker"""
        response = client.get_product_ticker(product)
        assert isinstance(response, dict), "Product ticker should be dict"
        assert set(product_ticker_keys).issubset(response.keys()), "Product ticker should contain the following keys: {}".format(product_ticker_keys)
    
    
    @vcr.use_cassette('tests/cassettes/trades.yml')
    def test_get_trades(self, client, product, trade_keys):
        """List latest trades for a product"""
        response = client.get_trades(product)
        assert isinstance(response, list), "Trades should be list"
        assert isinstance(response[0], dict), "Trades should be list of dicts"
        assert set(trade_keys).issubset(response[0].keys()), "Trade dict should contain the following keys: {}".format(trade_keys)
    
    
    @vcr.use_cassette('tests/cassettes/historic_rates.yml')
    def test_get_historic_rates(self, client, product):
        """Test API call to get historic rates as OHLC candles"""
        response = client.get_historic_rates(product)
        assert isinstance(response, list), "Response should be a list of candles"
        assert isinstance(response[0], list), "Candle itself should be list of info"
        assert len(response[0]) == 6, "Candles should be len 6"
        assert isinstance(response[0][0], int), "First entry should be trade ID"
    
    
    @vcr.use_cassette('tests/cassettes/stats.yml')
    def test_get_stats(self, client, product, stats_keys):
        """Test API call to get 24 hour stats"""
        response = client.get_stats(product)
        assert isinstance(response, dict), "Stats response should be dict"
        assert set(stats_keys).issubset(response.keys()), "Stats should contain the stats keys: {}".format(stats_keys)
    
    
    @vcr.use_cassette('tests/cassettes/currencies.yml')
    def test_get_currencies(self, client, currency_keys):
        """Test API call to get all currencies"""
        response = client.get_currencies()
    
        assert isinstance(response, list), "Currency response should be list"
        assert isinstance(response[0], dict), "List entries should be dicts"
        assert set(currency_keys).issubset(response[0].keys()), "Currency dict should contain the following keys: {}".format(currency_keys)
    
    @vcr.use_cassette('tests/cassettes/time.yml')
    def test_get_time(self, client):
        """Test API call to get current server time"""
        response = client.get_time()
    
        assert isinstance(response, dict), "Response should be a dict"
        assert set(['iso', 'epoch']).issubset(response.keys()), "Response should contain the following keys: {}".format(['iso', 'epoch'])

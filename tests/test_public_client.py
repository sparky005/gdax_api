from pytest import fixture, mark, skip
from gdax_api import PublicClient
import vcr 
##################################
# Fixtures:
# Fixtures that will be used across
# all tests
##################################


@fixture
def product():
    return 'BTC-USD'

@fixture
def client():
    """
    Initialize an API client so we don't have to
    initliaze a new one for each function
    """

    client = PublicClient()
    return client


###################################
# Test data:
# All methods herein produce test
# validation data (ie keys in dicts)
###################################


def product_keys():
    # returns test data
    return ['id', 'base_currency', 'quote_currency',
            'base_min_size', 'base_max_size', 'quote_increment']

def product_order_book_keys():
    # returns test data
    return ['sequence', 'bids', 'asks']

def product_ticker_keys():
    # returns test data
    return ['trade_id', 'price', 'size', 'bid', 'ask', 'volume', 'time']

def trade_keys():
    # returns test data
    return ['time', 'trade_id', 'price', 'size', 'side']

def stats_keys():
    # returns test data
    return ['open', 'high', 'low', 'volume']

def currency_keys():
    # returns test data
    return ['id', 'name', 'min_size']


###################################
# Actual tests:
# ok now we're actually testing
###################################


@vcr.use_cassette('tests/cassettes/products.yml')
def test_get_products(client):
    """Test API call to get available products"""
    response = client.get_products()

    assert isinstance(response, list), "Response should be a list"
    assert isinstance(response[0], dict), "First element should be a dict"
    assert set(product_keys()).issubset(response[0].keys()), "Product dict should contain the following keys: {}".format(product_keys())


@vcr.use_cassette('tests/cassettes/product_order_book.yml')
@mark.parametrize("product,level",[
                                ('BTC-USD', 1),
                                ('BTC-USD', 2),
                                (product(), 3)])
def test_get_product_order_book(client, product, level):
    """Test API call to get orders for single product"""
    response = client.get_product_order_book(product, level)

    assert isinstance(response, dict), "Order book should be a dict"
    assert set(product_order_book_keys()).issubset(response.keys()), "Order book dict should contain the following keys: {}".format(product_order_book_keys())
    assert isinstance(response['sequence'], int), "Sequence must be in"
    assert isinstance(response['bids'], list), "Bids should be a list"
    assert isinstance(response['asks'], list), "Asks should be a list"
    if level == 1:
        skip("L1")
        assert len(response['bids']) == 50, "l2 should return 50 bids"
        assert len(response['asks']) == 50, "l2 should return 50 asks"
    if level == 1 or level == 2:
        skip("L1 or L2")
        assert len(response['bids']) > 50, "l2 should return > 50 bids"
        assert len(response['asks']) > 50, "l2 should return > 50 asks"


@vcr.use_cassette('tests/cassettes/product_ticker.yml')
def test_get_product_ticker(client, product):
    """Test API call to product ticker"""
    response = client.get_product_ticker(product)
    assert isinstance(response, dict), "Product ticker should be dict"
    assert set(product_ticker_keys()).issubset(response.keys()), "Product ticker should contain the following keys: {}".format(product_ticker_keys())


@vcr.use_cassette('tests/cassettes/trades.yml')
def test_get_trades(client, product):
    """List latest trades for a product"""
    response = client.get_trades(product)
    assert isinstance(response, list), "Trades should be list"
    assert isinstance(response[0], dict), "Trades should be list of dicts"
    assert set(trade_keys()).issubset(response[0].keys()), "Trade dict should contain the following keys: {}".format(trade_keys())


@vcr.use_cassette('tests/cassettes/historic_rates')
def test_get_historic_rates(client, product):
    """Test API call to get historic rates as OHLC candles"""
    response = client.get_historic_rates(product)
    assert isinstance(response, list), "Response should be a list of candles"
    assert isinstance(response[0], list), "Candle itself should be list of info"
    assert len(response[0]) == 6, "Candles should be len 6"
    assert isinstance(response[0][0], int), "First entry should be trade ID"


@vcr.use_cassette('tests/cassettes/stats')
def test_get_stats(client, product):
    """Test API call to get 24 hour stats"""
    response = client.get_stats(product)
    assert isinstance(response, dict), "Stats response should be dict"
    assert set(stats_keys()).issubset(response.keys()), "Stats should contain the stats keys: {}".format(stats_keys())


@vcr.use_cassette('tests/cassettes/currencies')
def test_get_currencies(client):
    """Test API call to get all currencies"""
    response = client.get_currencies()

    assert isinstance(response, list), "Currency response should be list"
    assert isinstance(response[0], dict), "List entries should be dicts"
    assert set(currency_keys()).issubset(response[0].keys()), "Currency dict should contain the following keys: {}".format(currency_keys())

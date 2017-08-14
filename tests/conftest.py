import pytest
from gdax_api import PublicClient
##################################
# Fixtures:
# Fixtures that will be used across
# all tests
##################################


@pytest.fixture
def product():
    return 'BTC-USD'

@pytest.fixture
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


@pytest.fixture
def product_keys():
    # returns test data
    return ['id', 'base_currency', 'quote_currency',
            'base_min_size', 'base_max_size', 'quote_increment']

@pytest.fixture
def product_order_book_keys():
    # returns test data
    return ['sequence', 'bids', 'asks']

@pytest.fixture
def product_ticker_keys():
    # returns test data
    return ['trade_id', 'price', 'size', 'bid', 'ask', 'volume', 'time']

@pytest.fixture
def trade_keys():
    # returns test data
    return ['time', 'trade_id', 'price', 'size', 'side']

@pytest.fixture
def stats_keys():
    # returns test data
    return ['open', 'high', 'low', 'volume']

@pytest.fixture
def currency_keys():
    # returns test data
    return ['id', 'name', 'min_size']


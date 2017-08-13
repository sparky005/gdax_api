from pytest import fixture, mark, skip
from gdax_api import Client
import vcr

@fixture
def product():
    return 'BTC-USD'

def product_keys():
    # returns test data
    return ['id', 'base_currency', 'quote_currency',
            'base_min_size', 'base_max_size', 'quote_increment']

@fixture
def product_order_book_keys():
    # returns test data
    return ['sequence', 'bids', 'asks']


@vcr.use_cassette('tests/cassettes/products.yml')
def test_get_products():
    """Test API call to get available products"""
    client = Client()
    response = client.get_products()

    assert isinstance(response, list), "Response should be a list"
    assert isinstance(response[0], dict), "First element should be a dict"
    assert set(product_keys()).issubset(response[0].keys()), "Keys should be in response"


@vcr.use_cassette('tests/cassettes/product_order_book.yml')
@mark.parametrize("product,level",[
                                ('BTC-USD', 1),
                                ('BTC-USD', 2),
                                (product(), 3)])
def test_get_product_order_book(product, level):
    """Test API call to get orders for single product"""
    client = Client()
    response = client.get_product_order_book(product, level)

    assert isinstance(response, dict), "Order book should be a dict"
    assert set(product_order_book_keys()).issubset(response.keys()), "Should contain three keys"
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


def test_get_product_ticker(product):
    client = Client()
    response = client.get_product_ticker(product)
    assert isinstance(response, dict)


from conftest import *
from tools.rest_client import  RestApiClient, Assertions, Pprint

def test_tc_1():
    result = RestApiClient.get('/api/unknown/')    
    Assertions.assert_json(result, "page", 1, "asdasdasdasdas",)
    Pprint.round_trip(result)
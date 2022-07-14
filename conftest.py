from urllib import request
import pytest
from Clients.Rest import RestApiClient


""" 
Фикстура вызова клиента для запросов к Rest API, 
- Принимиает в себя аргумент base_address 
"""
@pytest.fixture
def rest_request():
    return RestApiClient(base_address="")

from conftest import *
from data import Base_url
from Clients.Rest import RestApiResponse
from jsonschema import validate
from Tests.restapi.Schema import schema


def test_tc_1(rest_request):
    response = rest_request.get(f"{Base_url['url']}/api/unknown")
    result = RestApiResponse(response)
    result.assert_status_code(200)
    result.pprint_response()
    validate(response.json(), schema)

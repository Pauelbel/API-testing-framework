import requests
from data import rest_api_data
from requests import Response
import json
import textwrap

""" 
Клиент для запросов к Rest API
"""
class RestApiClient():

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None ):
        return RestApiClient._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None ):
        return RestApiClient._send(url, data, headers, cookies, 'POST')


    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        
        url = f"{rest_api_data['url']}{url}"

        if headers is None:
            headers = {}

        if cookies is None:
            cookies = {}
        
        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)

        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)

        else:
            raise Exception(f'Неизестный HTTP метод  <{method}>')
        return response

""" 
Класс для вывода отформатированного принта
"""
class Pprint:
    @staticmethod
    def round_trip(response: Response):
            if response.headers['Content-Type'] == "text/plain;charset=utf-8":
                resp = response.text
            else:
                resp = json.dumps(response.json(), indent=4,
                                  sort_keys=True, ensure_ascii=False)

            def format_headers(d): return '\n'.join(f'{k}: {v}' for k, v in d.items())
            return print(textwrap.dedent('''
                ------------------- Request --------------------
                {req.method} {req.url}
                {reqhdrs}
                --------------------- Body ---------------------
                {req.body}
                ------------------- Response -------------------
                {res.status_code} {res.reason} {res.url}
                {reshdrs}
                --------------------- Data ---------------------
                {resp}
            ''').format(
                req=response.request,
                res=response,
                resp=resp,
                reqhdrs=format_headers(response.request.headers),
                reshdrs=format_headers(response.headers),
            ))
""" 
Класс для обработки ассеротов в тестах
"""
class Assertions:
    @staticmethod
    def assert_json(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в Json формате. ответ --> {response.text}"
        assert response_as_dict[name] == expected_value, error_message
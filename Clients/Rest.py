import requests
import json
import textwrap

""" 
Клиент для запросов к Rest API
"""
class RestApiClient():
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=headers)

""" 
Класс Для обработки ответа от REST API 
Включает в Себя функции:
- validate - Проверка валидации схемы ответа (подключается в тестах)
- assert_status_code - проверить код ответа (подключается в тестах)
- pprint_response - отформатированный консольный вывод (подключается в тестах)
""" 
class RestApiResponse:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(self.response_json)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, f"Код ответа ---> {self.response_status}, ожидается ---> {status_code}"
        else:
            assert self.response_status == status_code, f"Код ответа ---> {self.response_status}, ожидается ---> {status_code}"
        return self

    def pprint_response(self):
        if self.response.headers['Content-Type'] == "text/plain;charset=utf-8":
            resp = self.response.text
        else:
            resp = json.dumps(self.response.json(), indent=4,
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
            req=self.response.request,
            res=self.response,
            resp=resp,
            reqhdrs=format_headers(self.response.request.headers),
            reshdrs=format_headers(self.response.headers),
        ))
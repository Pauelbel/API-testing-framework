
from zeep import Client
from zeep.plugins import Plugin
from zeep.wsse.username import UsernameToken
import textwrap
from lxml import etree
from data import soap_api_data


class SoapApiClient():
    @staticmethod
    def _wsse():
        try:
            
            client = Client(
                wsdl=soap_api_data['wsdl'],
                wsse=UsernameToken(
                    soap_api_data['wsse_login'],
                    soap_api_data['wsse_password'],),
                port_name=soap_api_data['port_name'],
                plugins=[Pprint()],)
            client.settings(wsse=False)
            #client.transport.session.verify = False
        except Exception as e:
            print(f"Не удалось подключиться (Причина-->> {e})")
        return client.service
    
    @staticmethod
    def request(method, **params):
        try:
            return SoapApiClient._wsse()[method](**params)
        except Exception as e:
            return f"Неверно соствлен запрос (Причина-->> {e})"



class Pprint(Plugin):
    
    @classmethod
    def egress(cls, envelope, http_headers, binding_options, operation):
        return print(textwrap.dedent(
        '''
        ------------------- Request --------------------
        {operation}
        {binding_options}
        {header}
        --------------------- Body ---------------------
        {body}''').format(
            operation=(operation),
            binding_options = (binding_options),
            header=(http_headers),
            body=etree.tostring(envelope, pretty_print=True, encoding="unicode"),
        ))
    
    @staticmethod  
    def ingress(envelope, http_headers, operation):
        return print(textwrap.dedent(
        '''
        ------------------- Response --------------------
        {header}
        --------------------- Data ----------------------
        {data}
        ''').format(
            header = (http_headers),
            data = etree.tostring(envelope, pretty_print=True, encoding="unicode"),
        ))



class Assertions:
    
    @staticmethod
    def assert_soap(name, expected_value, error_message):
        assert expected_value == name, f"Тест провлен --> {error_message}:\n\tОжидаемый результат --> {expected_value}\n\tФактический --> {name}"


from clients.soap_client import  SoapApiClient, Assertions, Pprint



def test_soap():
        result = SoapApiClient.request("NumberToDollars", dNum=5)
        Assertions.assert_soap(result, "five dollars","Сообщение об ошибке")

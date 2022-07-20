## Структура фрейморка

***

### Clients

> Включает в себя Клиенты для осуществления запросов и обработки полученных ответов

### Tests
> Включает в себя наборы тестов разделенных на группы:
> 1. restapi   - тесты запросов/ответов к RestApi
> 2. soapapi   - тесты запросов/ответов к SoapApi
> 3. websocket - тесты запросов/ответов через websocket

> - схемы для проверки валидации полученных ответов


***
## Настройка и запуск 

### Установка библиотек
* ``` pip install -r requirements.txt ```
### запуск тестов
* ``` python -m pytest Tests/restapi/tc_1.py -vs ```


## Зависимости 

* pytest
* requests
* jsonschema


## Тестируемые ресурсы
Rest API - https://reqres.in/
Soap Api - http://users.bugred.ru/tasks/soap/WrapperSoapServer.php?wsdl

import requests

class ValorDoDolar():   #Classe para retornar o valor do dólar a partir da api

    def __init__(self):     # Declaração do valor caso a API se encontre inacessível.
        self.valorapi = -1

    def consulta(self):
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" #URL da API
        retorno = requests.get(url)
        if (retorno.status_code==200):
            jsonparsed = retorno.json()
            print(jsonparsed)
            self.valorapi = jsonparsed['USDBRL']['ask'] #Informação que será obtida da API
        else:
            self.valorapi = -1 # Resultado caso a API se encontre inacessível.
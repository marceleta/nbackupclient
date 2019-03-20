import json

class Configuracao:

    def __init__(self):
        self._arquivo = open('config.json','r')
        self._json = json.load(self._arquivo)
        self._host = self._json['host']
        self._porta = self._json['porta']


    def get_host(self):
        return self._host

    def get_porta(self):
        return self._porta
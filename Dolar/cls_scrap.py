import requests
from bs4 import BeautifulSoup

### Clases ###


class Request():
    """
    Clase que permite realizar peticiones a una URL.
    """

    def __init__(self, url):
        """
        Metodo constructor que inicializa la clase y
        declara variables de instancia.
        """

        self.url = url


class Scrap(Request):
    """
    Clase hija de Request que permite realizar el scraping de una URL.
    """

    def __init__(self,url):
        """
        Metodo constructor que inicializa la clase y
        declara variables de instancia.
        """

        super().__init__(url)
        self.request = self.llamado_pagina()
        self.formato_scrap()

    def llamado_pagina(self,):
        """
        Metodo que permite realizar el llamado a una URL.
        """

        return requests.get(self.url)

    def formato_scrap(self, formato="html.parser"):
        """
        Metodo que permite dar el formato para realizar el scaping.
        """

        self.soup = BeautifulSoup(self.request.text, formato)
        return self.soup

    def scrapeo(self, etiqueta_html, clase):
        """
        Metodo que permite realizar el scraping.
        """

        return self.soup.find_all(etiqueta_html, class_=clase)

    def mostrar(self, *args):
        """
        Metodo que permite mostrar los resultados del scraping.
        """

        for x in args:
            print('\t', '\t', f'{x[0]}', '\n',
                  f'Compra: {x[1]} - Venta: {x[2]}', '\n',)

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
  
    def __init__(self,):
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
      
    
    def formato_scrap(self,formato= "html.parser"):
        """
        Metodo que permite dar el formato para realizar el scaping.
        """     
        
        self.soup = BeautifulSoup(self.request.text, formato)
        return self.soup
        
       
    def scrapeo(self, etiqueta_html, clase):
        """
        Metodo que permite realizar el scraping.
        """
      
        return self.soup.find_all(etiqueta_html, class_= clase)
  
    def mostrar(self,*args):
        """
        Metodo que permite mostrar los resultados del scraping.
        """

        for x in args:
            print('\t', '\t', f'{x[0]}', '\n', f'Compra: {x[1]} - Venta: {x[2]}', '\n',)

  
if __name__ == '__main__':

    # instancia de clases 
    url = "https://dolarhoy.com/"
    
    scrap = Request(url)
    
    soup = Scrap()

    # busqueda especifica
    busqueda = soup.scrapeo("a", "title")
    compra = soup.scrapeo(
                    "div",
                    "tile is-parent is-9 cotizacion is-vertical"
                    )
    
    filtro = []
    
    # separo y añado a la lista
    for x in busqueda:
      filtro.append(str(x.text))
    
    # borrro las repeticiones
    seteado = filtro[1:]
    lista_titulos = list(seteado)
    
    valor = compra[0]
    
    # busqueda de los valores
    bb = soup.scrapeo("div", "val")
    
    lista_valores = []
    
    # obtengo los valores y agrego a la lista
    for x in bb:
      lista_valores.append(x.text)
    
    lista_2 = lista_valores[2:]
      
    # creo las variables
    blue = [(lista_titulos[0]), (lista_2[0]), (lista_2[1])]
    oficial = [(lista_titulos[1]), (lista_2[2]), (lista_2[3])]
    mep = [(lista_titulos[2]), (lista_2[4]), (lista_2[5])]
    ccl = [(lista_titulos[3]), (lista_2[6]), (lista_2[7])]
    cripto = [(lista_titulos[4]), (lista_2[8]), (lista_2[9])]
    tarjeta = [(lista_titulos[5]), (lista_2[2]), (lista_2[10])]
    
    precios = [blue, oficial, mep, ccl, cripto, tarjeta]
    
    # itero la lista y muestro en pantalla
    soup.mostrar(*precios)

import requests
from bs4 import BeautifulSoup

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

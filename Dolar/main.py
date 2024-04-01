from cls_scrap import Request, Scrap
import cls_pd
import cls_mtp

if __name__ == '__main__':

  # instancia de clases
  url = "https://dolarhoy.com/"

  scrap = Request(url)

  soup = Scrap(url)

  # busqueda especifica
  busqueda = soup.scrapeo("a", "title")
  compra = soup.scrapeo("div", "tile is-parent is-9 cotizacion is-vertical")

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
  precios_2 = [
      blue[1:], oficial[1:], mep[1:], ccl[1:], cripto[1:], tarjeta[1:]
  ]

  indice = [blue[0], oficial[0], mep[0], ccl[0], cripto[0], tarjeta[0]]

  texto = ['Compra', 'Venta']

  # Instancio la clase para pandas
  table = cls_pd.DataFrame(precios_2)
  tabla = table.create_DataFrame(indice, texto)
  print(tabla)

  # Instancio la clase para graficar
  grafico = cls_mtp.Graphics()

  grafico.plot(texto,
               blue[1:],
               line_color='Blue',
               line_type='--',
               marker_type='o',
               title='Dolares',
               label_name='Blue')

  grafico.plot(texto,
               mep[1:],
               line_color='Green',
               line_type='--',
               marker_type='o',
               label_name='Mep')

  grafico.plot(texto,
               cripto[1:],
               line_color='Red',
               line_type='--',
               marker_type='o',
               label_name='Cripto')

  grafico.plot(texto,
               ccl[1:],
               line_color='Black',
               line_type='--',
               marker_type='o',
               label_name='CCL')



  grafico.savefig('Dolares')
  grafico.show()

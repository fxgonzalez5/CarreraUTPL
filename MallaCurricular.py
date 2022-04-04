import scrapy
import pandas as pd

class QuotesSpider(scrapy.Spider):
    name = "myspider"
    lista = [] #Creo una lista global

    def start_requests(self):
        files = [
            'file:///C:/Users/Francisco/Documents/Programación/Projects_Pythom/Carreras-UTPL/Paginas/Arquitectura_UTPL.html',
            'file:///C:/Users/Francisco/Documents/Programación/Projects_Pythom/Carreras-UTPL/Paginas/Computación_UTPL.html',
            'file:///C:/Users/Francisco/Documents/Programación/Projects_Pythom/Carreras-UTPL/Paginas/IngenieríaCivil_UTPL.html',
            'file:///C:/Users/Francisco/Documents/Programación/Projects_Pythom/Carreras-UTPL/Paginas/TecnologíasInformación_UTPL.html',
        ]
        for file in files:
            yield scrapy.Request(url=file, callback=self.parse)

    def parse(self, response):
        nombreArch = 'Materias_de_las_Carreras_UTPL.csv' # Nombre del archivo
        carrera = response.xpath("//h2/text()").get() # Nombre de la carrera
        ciclos = response.xpath("//div[@class='btn-semestre']/text()").getall() # Ciclos de cada carrera
        uls = response.xpath("//div[@class='link1 whitebg']/ul") # Lista de materias por ciclo
        for ul in range (len(uls)):
            ciclo = ciclos[ul].replace("/n", "").strip() # Almacena el ciclo correspondiente
            lis = uls[ul].xpath("li") # Almacena las materias correspondientes al ciclo
            for li in lis:
                if li.xpath("strong") != []: # Evalúa si hay textos en negrita
                    if li.xpath("text()") != []: # Evalúa si hay texto normal
                        negrita = li.xpath("strong/text()").get() # Almacena el texto en negrita
                        normal = li.xpath("text()").get() # Almacena el texto normal
                        materia = negrita + normal # Concatena las dos candenas antes almacenadas
                    else: # Si no hay texto normal pero si en negrita...
                        materia = li.xpath("strong/text()").get() # Almacena el texto en negrita
                else: # Si no hay texto en negrita...
                    materia = li.xpath("text()").get() # Almacena el texto normal

                # Almacena en una lista, diccionarios que contengan los datos almacenados en las variables
                self.lista.append({'Carrera':carrera, 'Ciclo':ciclo, 'Materia':materia})

            data = pd.DataFrame.from_dict(self.lista) # Convierte la lista en un dataframe
            data.to_csv(nombreArch) # Exporta el dataframe en un archivo CSV
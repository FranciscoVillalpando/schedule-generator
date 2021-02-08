import scrapy

class OfertaSpider(scrapy.Spider):
    name = 'Oferta'

    def start_requests(self):
        return [scrapy.FormRequest("http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta",
                                   formdata={'ciclop': '202110', 'cup': 'A'},
                                   callback=self.primera_pagina)]

    def primera_pagina(self, response):

        #only first root table is useful
        #first two rows are headers
        for row in response.xpath("//body/table[1]").xpath("tr")[2:]:
            fields = row.xpath("td")
            nrc = fields[0].xpath("text()").get()
            clave = fields[1].xpath("a/text()").get()
            materia = fields[2].xpath("a/text()").get()
            sec = fields[3].xpath("text()").get()
            cr = fields[4].xpath("text()").get()
            cup = fields[5].xpath("text()").get()
            dis = fields[6].xpath("text()").get()
            tabla_horario = fields[7].xpath("text()").get()
            profesor = fields[8].xpath("text()").get()
            yield {
                "nrc": nrc,
                "clave": clave,
                "materia": materia,
                "sec": sec,
                "cr": cr,
                "cup": cup,
                "dis": dis,
                "tabla_horario" : tabla_horario,
                "profesor": profesor
                }
        
         
#from datetime import datetime
import requests

def run():
    lista = ['argentina','brazil','chile','colombia','ecuador','guyana','paraguay','peru','suriname','uruguay','venezuela','trinidad and tobago']
    print ("Ingrese el periodo Desde: ")
    print("Ingrese el año:")
    anio = input()
    print("Ingrese el mes:")
    mes = input()
    print("Ingrese el dia:")
    dia = input()
    fechaDesde = anio+"-"+mes+"-"+dia
    print ("Ingrese el periodo Hasta: ")
    print("Ingrese el año:")
    anio = input()
    print("Ingrese el mes:")
    mes = input()
    print("Ingrese el dia:")
    dia = input()
    fechaHasta = anio+"-"+mes+"-"+dia
    for x in lista:
        casesDeaths(x,fechaDesde,fechaHasta)


def casesDeaths(data,fechaD,fechaH):
    api_link = f'https://api.covid19api.com/country/{data}/status/deaths?from={fechaD}T00:00:00Z&to={fechaH}T00:00:00Z'
    print (api_link)
    response = requests.get(api_link)
    respuesta = response.json()
    for item in respuesta:
        case = item.get("Cases")
    print(case)
        # if cases:   
        #  print(cases)


#URL= 'https://api.covid19api.com/country/argentina/status/deaths?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z'
#api_link = "https://api.covid19api.com/live/country/south-africa/status/confirmed"

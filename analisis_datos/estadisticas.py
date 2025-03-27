# estadisticas.py
def promedio(datos):
    media = sum(datos) / len(datos)
    return media

def mediana(datos):
    #mediana
    #paso 1: ordenar valores ascendentemente
    datos = sorted(datos)
    #paso 2: determinar si la cantidad de numeros en la lista es par o impar
    mitad = len(datos) // 2
    if len(datos) % 2 == 0:
        mediana = (datos[mitad - 1] + datos[mitad])/2
    else:
        mediana = datos[mitad]   
    return mediana
    #pass #pendiente programar calculo de mediana estadistica

# Proyecto: Clase 10 - Fundamentos de Python
# Estudiante: Josue Solano Redondo
# Fecha de Inicio: 26/03/2025
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

#from analisis_datos.carga_datos import generar_lista_comprar
#from analisis_datos.estadisticas import promedio
from analisis_datos import *

lista_compra = generar_lista_comprar()
print(lista_compra)
precios = [precio for nombre,precio in lista_compra]
print(precios)
print(promedio(precios))
print(mediana(precios))
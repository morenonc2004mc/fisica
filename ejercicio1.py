#En las olimpiadas de invierno el tiempo que realizan los participantes en la competencia de velocidad en pista se mide en minutos
#segundos y centecimas la distancia que recorre se expresa en minutos

dis = int(input("Ingrese la distancia recorrida en metros: "))
min = int(input("Ingrese la cantidad en minutos: "))
seg = int(input("Ingrese la cantidad de seundos: "))
cen = int(input("Ingrese la cantidad de centecimas: "))

tse = (min*60) + seg + (cen/100)
vms = dis/tse
vkm = (vms*3600)/1000

print("La cantidad es de",vkm,"km/h")
#Una persona mueve una silla con un lazo a una distancia de 15m este lazo forma un angulo de 40grados con respecto a la horizontal del piso
#si la tencion que presenta el lazo es de 6 N ¿ Cual es el trabajo realizado ? 

d = int(input("Ingrese la distancia en metros: "))
f = int(input("ingrese la fuerza en newtons: "))
a = float(input("Ingrese los angulos: "))
a1 = math.radians(a)
s1=(math.cos(a1))
print("El trabajo es: W=",f*d*s1)

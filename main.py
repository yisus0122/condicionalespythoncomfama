#PERRO NEGRO

nombreCliente=input("Cual es su nombre? ")
paisCliente=input("Cual es su pais de origen? ")
cantidadPersonas=int(input("cuantas personas van a reservar? "))
añoNacimientoCliente=int(input("en que año nacio? "))


#calcular la edad del cliente
añoActual=2024
edadCliente=añoActual-añoNacimientoCliente

#CLASIFICAR, PREGUNTAR, DECIDIR
if edadCliente >= 18:
    print("Usted es mayor de edad")
else:
    print("oe")
print("usted es menor de edad")
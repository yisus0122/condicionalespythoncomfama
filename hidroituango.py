#condiciones multiples

sensorNivelAgua=int(input("Digite el nivel de agua de la represa: "))

print(f"El nivel de agua es: {sensorNivelAgua}")

if sensorNivelAgua>0 and sensorNivelAgua<=150:
    print("muy poca agua las puertas estan cerradas")
elif sensorNivelAgua>150 and sensorNivelAgua<=400:
    print("operando normalmente")
elif sensorNivelAgua>400 and sensorNivelAgua<=420:
    print("mucho cuidado revise el nivel de agua")
elif sensorNivelAgua>420:
    print("Este parche se calento  corre......")
else:
    print("revise el sensor, medida no valida")
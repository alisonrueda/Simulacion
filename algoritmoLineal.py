xn = int(input("Ingrese la semilla: "))
a = int(input("Ingrese la constante multiplicativa: "))
c = int(input("Ingrese la constante aditiva: "))
m = int(input("Ingrese el modulo: "))

for i in range(10):
    xn1 = (a * xn + c) % m
    r = xn1 / (m - 1)
    
    print(f"Iteración {i+1}:")
    print(f"xn1 (valor generado) = {xn1}")
    print(f"r (valor normalizado) = {r}\n")
    
    xn = xn1 

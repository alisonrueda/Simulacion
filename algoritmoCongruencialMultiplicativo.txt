while True:
    xn = int(input("Ingrese la semilla (número impar y positivo): "))
    if xn > 0 and xn % 2 != 0:  # Verificar si es positivo e impar
        break
    else:
        print("La semilla debe ser un número positivo e impar. Intente nuevamente.")

# Entradas del usuario
a = int(input("Ingrese la constante multiplicativa: "))
m = int(input("Ingrese el modulo: "))

# Generación de 10 números aleatorios
for i in range(10):
    xn1 = (a * xn) % m  # Algoritmo congruencial multiplicativo
    r = xn1 / (m - 1)  # Normalización
    
    # Mostrar los resultados
    print(f"Iteración {i+1}:")
    print(f"xn1 (valor generado) = {xn1}")
    print(f"r (valor normalizado) = {r}\n")
    
    xn = xn1  # Actualizar el valor de xn para la siguiente iteración

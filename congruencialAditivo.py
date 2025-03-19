def congruencial_aditivo(m, semillas, cantidad):
    numeros = semillas[:]
    for i in range(len(semillas), cantidad + len(semillas)):
        nuevo = (numeros[i - len(semillas)] + numeros[i - len(semillas) + 1]) % m
        numeros.append(nuevo)
    
    aleatorios = [x / (m - 1) for x in numeros[len(semillas):]]
    return numeros[len(semillas):], aleatorios

m = 100
semillas = [65, 89, 98, 3, 69]  # Valores iniciales
cantidad = 7  # Cantidad de números aleatorios a generar

numeros_generados, aleatorios = congruencial_aditivo(m, semillas, cantidad)

print("Números generados:", numeros_generados)
print("Números pseudoaleatorios:", aleatorios)

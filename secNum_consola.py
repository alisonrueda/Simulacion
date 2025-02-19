import random

def secuencia():
    min = int(input("Ingrese el número mínimo del rango: "))
    max = int(input("Ingrese el número máximo del rango: "))
    print("Su rango de números aleatorios es de ", min, " a ", max)
    cant = int(input("Ingrese la cantidad de números a generar: "))
    sec= []
    for i in range(cant):
        numero= random.randint(min, max)
        sec.append(numero)
    print("Números generados:")
    print(*sec)
    return sec
    
def promedio(lista):
    return round(sum(lista)/len(lista), 2)

print("Primera secuencia")
sec1= secuencia()

print("")
print("Segunda secuencia")
sec2= secuencia()

print("")
print("Promedio de la primera secuencia: ", promedio(sec1))
print("Promedio de la segunda secuencia: ", promedio(sec2))
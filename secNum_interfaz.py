import random
import tkinter as tk
from tkinter import messagebox

# Función para generar la secuencia de números
def secuencia(min, max, cant):
    sec = []
    for i in range(cant):
        numero = random.randint(min, max)
        sec.append(numero)
    return sec

# Función para calcular el promedio
def promedio(lista):
    return round(sum(lista) / len(lista), 2)

# Función para manejar el evento de generación
def generar_secuencias():
    try:
        # Obtener datos para la primera secuencia
        min1 = int(entry_min1.get())
        max1 = int(entry_max1.get())
        cant1 = int(entry_cant1.get())
        
        # Obtener datos para la segunda secuencia
        min2 = int(entry_min2.get())
        max2 = int(entry_max2.get())
        cant2 = int(entry_cant2.get())
        
        # Validar que los valores mínimos sean menores que los máximos
        if min1 >= max1 or min2 >= max2:
            messagebox.showerror("Error", "El número mínimo debe ser menor que el máximo.")
            return

        # Generar las secuencias
        sec1 = secuencia(min1, max1, cant1)
        sec2 = secuencia(min2, max2, cant2)
        
        # Mostrar los resultados
        result_sec1.config(text=f"Secuencia 1: {sec1}")
        result_sec2.config(text=f"Secuencia 2: {sec2}")
        result_prom1.config(text=f"Promedio Secuencia 1: {promedio(sec1)}")
        result_prom2.config(text=f"Promedio Secuencia 2: {promedio(sec2)}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese solo números enteros.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Secuencias Aleatorias")
root.geometry("600x400")

# Crear un frame para contener la Secuencia 1 (izquierda) y la Secuencia 2 (derecha)
frame = tk.Frame(root)
frame.pack(pady=20)

# Frame izquierdo para la Secuencia 1
frame_left = tk.Frame(frame)
frame_left.grid(row=0, column=0, padx=20)

# Frame derecho para la Secuencia 2
frame_right = tk.Frame(frame)
frame_right.grid(row=0, column=1, padx=20)

# Etiquetas y campos para la primera secuencia (izquierda)
label_min1 = tk.Label(frame_left, text="Número mínimo del rango (Secuencia 1):")
label_min1.grid(row=0, column=0, pady=5)
entry_min1 = tk.Entry(frame_left)
entry_min1.grid(row=1, column=0, pady=5)

label_max1 = tk.Label(frame_left, text="Número máximo del rango (Secuencia 1):")
label_max1.grid(row=2, column=0, pady=5)
entry_max1 = tk.Entry(frame_left)
entry_max1.grid(row=3, column=0, pady=5)

label_cant1 = tk.Label(frame_left, text="Cantidad de números a generar (Secuencia 1):")
label_cant1.grid(row=4, column=0, pady=5)
entry_cant1 = tk.Entry(frame_left)
entry_cant1.grid(row=5, column=0, pady=5)

# Etiquetas y campos para la segunda secuencia (derecha)
label_min2 = tk.Label(frame_right, text="Número mínimo del rango (Secuencia 2):")
label_min2.grid(row=0, column=0, pady=5)
entry_min2 = tk.Entry(frame_right)
entry_min2.grid(row=1, column=0, pady=5)

label_max2 = tk.Label(frame_right, text="Número máximo del rango (Secuencia 2):")
label_max2.grid(row=2, column=0, pady=5)
entry_max2 = tk.Entry(frame_right)
entry_max2.grid(row=3, column=0, pady=5)

label_cant2 = tk.Label(frame_right, text="Cantidad de números a generar (Secuencia 2):")
label_cant2.grid(row=4, column=0, pady=5)
entry_cant2 = tk.Entry(frame_right)
entry_cant2.grid(row=5, column=0, pady=5)

# Botón para generar las secuencias
button_generate = tk.Button(root, text="Generar Secuencias", command=generar_secuencias)
button_generate.pack(pady=20)

# Resultados
result_sec1 = tk.Label(root, text="Secuencia 1:")
result_sec1.pack(pady=5)

result_sec2 = tk.Label(root, text="Secuencia 2:")
result_sec2.pack(pady=5)

result_prom1 = tk.Label(root, text="Promedio Secuencia 1:")
result_prom1.pack(pady=5)

result_prom2 = tk.Label(root, text="Promedio Secuencia 2:")
result_prom2.pack(pady=5)

# Ejecutar la ventana
root.mainloop()

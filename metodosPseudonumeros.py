import tkinter as tk
from tkinter import ttk

#disculpe lo hice con deepseek 
# Función para el método de Cuadrados Medios
def cuadrados_medios():
    # Limpiar la ventana actual
    for widget in root.winfo_children():
        widget.destroy()
    
    # Título del algoritmo
    title_label = tk.Label(root, text="Algoritmo de Cuadrados Medios", font=("Arial", 16))
    title_label.pack(pady=10)
    
    # Etiqueta para la semilla
    label = tk.Label(root, text="Ingresa un número de 4 dígitos como semilla inicial:")
    label.pack(pady=10)
    
    # Entrada para la semilla
    semilla_entry = tk.Entry(root)
    semilla_entry.pack(pady=5)
    semilla_entry.insert(0, "1234") 
    
    # Crear una tabla para mostrar los resultados
    table = ttk.Treeview(root, columns=("Y", "X", "R"), show="headings")
    table.heading("Y", text="Y (Cuadrado)")
    table.heading("X", text="X (Centro)")
    table.heading("R", text="R (Resultado)")
    table.pack(padx=10, pady=10)

    # Función para procesar la semilla y calcular los valores
    def mostrar_resultados():
        # Obtener la semilla desde el campo de texto
        semilla = semilla_entry.get()
        
        # Validar que sea un número de 4 dígitos
        if not semilla.isdigit() or len(semilla) != 4:
            error_label.config(text="¡Error! Debes ingresar un número de exactamente 4 dígitos.", fg="red")
            return
        else:
            error_label.config(text="")  # Limpiar mensaje de error
            semilla = int(semilla)
        
        # Limpiar la tabla antes de llenarla con los nuevos resultados
        for item in table.get_children():
            table.delete(item)
        
        # Calcular los siguientes 10 valores
        for i in range(10):
            # Calcular el cuadrado de la semilla
            cuadrado = semilla ** 2
            
            # Extraer los 4 dígitos del centro
            cuadrado_str = str(cuadrado).zfill(8)  # Completar con ceros a la izquierda si es necesario
            medio = cuadrado_str[2:6]  # Los 4 dígitos del medio
            
            # Convertir el valor medio a un número entre 0 y 9999
            r = f"0.{medio}"
            
            # Insertar los valores en la tabla
            table.insert("", "end", values=(cuadrado_str, medio, r))
            
            # Establecer la nueva semilla
            semilla = int(medio)

    # Botón para calcular y mostrar los resultados
    calculate_button = tk.Button(root, text="Generar Tabla", command=mostrar_resultados)
    calculate_button.pack(pady=10)
    
    # Etiqueta para mostrar errores
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=5)
    
    # Botón para volver al menú principal
    back_button = tk.Button(root, text="Volver al Menú", command=crear_menu)
    back_button.pack(pady=10)

# Función para el método de Productos Medios
def productos_medios():
    # Limpiar la ventana actual
    for widget in root.winfo_children():
        widget.destroy()
    
    # Título del algoritmo
    title_label = tk.Label(root, text="Algoritmo de Productos Medios", font=("Arial", 16))
    title_label.pack(pady=10)
    
    # Etiqueta para las semillas
    label = tk.Label(root, text="Ingresa dos números de 4 dígitos como semillas iniciales:")
    label.pack(pady=10)
    
    # Entradas para las dos semillas
    semilla1_entry = tk.Entry(root)
    semilla1_entry.pack(pady=5)
    semilla1_entry.insert(0, "1711")  # Valor por defecto
    semilla2_entry = tk.Entry(root)
    semilla2_entry.pack(pady=5)
    semilla2_entry.insert(0, "2703")  # Valor por defecto
    
    # Crear una tabla para mostrar los resultados
    table = ttk.Treeview(root, columns=("Y", "X", "R"), show="headings")
    table.heading("Y", text="Y (Producto)")
    table.heading("X", text="X (Centro)")
    table.heading("R", text="R (Resultado)")
    table.pack(padx=10, pady=10)

    # Función para procesar las semillas y calcular los valores
    def mostrar_resultados():
        # Obtener las semillas desde los campos de texto
        semilla1 = semilla1_entry.get()
        semilla2 = semilla2_entry.get()
        
        # Validar que sean números de 4 dígitos
        if not semilla1.isdigit() or len(semilla1) != 4 or not semilla2.isdigit() or len(semilla2) != 4:
            error_label.config(text="¡Error! Debes ingresar dos números de exactamente 4 dígitos.", fg="red")
            return
        else:
            error_label.config(text="")  # Limpiar mensaje de error
            semilla1 = int(semilla1)
            semilla2 = int(semilla2)
        
        # Limpiar la tabla antes de llenarla con los nuevos resultados
        for item in table.get_children():
            table.delete(item)
        
        # Calcular los siguientes 10 valores usando el método de productos medios
        for i in range(10):
            # Crear el producto de las dos semillas
            producto = semilla1 * semilla2
            
            # Extraer los 4 dígitos del centro del producto
            producto_str = str(producto).zfill(8)  # Completar con ceros a la izquierda si es necesario
            medio = producto_str[2:6]  # Los 4 dígitos del medio
            
            # Convertir el valor medio a un número entre 0 y 9999
            r = f"0.{medio}"
            
            # Insertar los valores en la tabla
            table.insert("", "end", values=(producto_str, medio, r))
            
            # Establecer las nuevas semillas
            semilla1 = int(medio)
            semilla2 = semilla1 + 1  # Usar semilla1 + 1 como la nueva segunda semilla

    # Botón para calcular y mostrar los resultados
    calculate_button = tk.Button(root, text="Generar Tabla", command=mostrar_resultados)
    calculate_button.pack(pady=10)
    
    # Etiqueta para mostrar errores
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=5)
    
    # Botón para volver al menú principal
    back_button = tk.Button(root, text="Volver al Menú", command=crear_menu)
    back_button.pack(pady=10)

# Función para el método del Multiplicador Constante
def multiplicador_constante():
    # Limpiar la ventana actual
    for widget in root.winfo_children():
        widget.destroy()
    
    # Título del algoritmo
    title_label = tk.Label(root, text="Algoritmo del Multiplicador Constante", font=("Arial", 16))
    title_label.pack(pady=10)
    
    # Etiqueta explicativa para la semilla y el multiplicador
    label = tk.Label(root, text="Ingresa la semilla y el multiplicador constante:")
    label.pack(pady=10)
    
    # Etiqueta y campo de texto para la semilla
    semilla_label = tk.Label(root, text="Semilla (Número de 4 dígitos):")
    semilla_label.pack(pady=5)
    semilla_entry = tk.Entry(root)
    semilla_entry.pack(pady=5)
    semilla_entry.insert(0, "6161")  # Valor por defecto
    
    # Etiqueta y campo de texto para el multiplicador constante
    constante_label = tk.Label(root, text="Multiplicador constante (Número de 4 dígitos):")
    constante_label.pack(pady=5)
    constante_entry = tk.Entry(root)
    constante_entry.pack(pady=5)
    constante_entry.insert(0, "7555")  # Valor por defecto
    
    # Crear una tabla para mostrar los resultados
    table = ttk.Treeview(root, columns=("Y", "X", "R"), show="headings")
    table.heading("Y", text="Y (Producto)")
    table.heading("X", text="X (Centro)")
    table.heading("R", text="R (Resultado)")
    table.pack(padx=10, pady=10)

    # Función para procesar la semilla, el multiplicador y calcular los valores
    def mostrar_resultados():
        # Obtener la semilla y el multiplicador desde los campos de texto
        semilla = semilla_entry.get()
        constante = constante_entry.get()
        
        # Validar que sean números de 4 dígitos
        if not semilla.isdigit() or len(semilla) != 4 or not constante.isdigit() or len(constante) != 4:
            error_label.config(text="¡Error! Debes ingresar números de exactamente 4 dígitos.", fg="red")
            return
        else:
            error_label.config(text="")  # Limpiar mensaje de error
            semilla = int(semilla)
            constante = int(constante)
        
        # Limpiar la tabla antes de llenarla con los nuevos resultados
        for item in table.get_children():
            table.delete(item)
        
        # Calcular los siguientes 10 valores usando el método del multiplicador constante
        for i in range(10):
            # Multiplicar la semilla por el constante
            producto = semilla * constante
            
            # Extraer los 4 dígitos del centro del producto
            producto_str = str(producto).zfill(8)  # Completar con ceros a la izquierda si es necesario
            medio = producto_str[2:6]  # Los 4 dígitos del medio
            
            # Convertir el valor medio a un número entre 0 y 9999
            r = f"0.{medio}"
            
            # Insertar los valores en la tabla
            table.insert("", "end", values=(producto_str, medio, r))
            
            # Establecer la nueva semilla
            semilla = int(medio)

    # Botón para calcular y mostrar los resultados
    calculate_button = tk.Button(root, text="Generar Tabla", command=mostrar_resultados)
    calculate_button.pack(pady=10)
    
    # Etiqueta para mostrar errores
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=5)
    
    # Botón para volver al menú principal
    back_button = tk.Button(root, text="Volver al Menú", command=crear_menu)
    back_button.pack(pady=10)

# Función para crear el menú principal
def crear_menu():
    # Limpiar la ventana actual
    for widget in root.winfo_children():
        widget.destroy()
    
    # Título del menú
    title_label = tk.Label(root, text="Generación de números pseudo aleatorios", font=("Arial", 16))
    title_label.pack(pady=20)
    
    # Botón para el método de Cuadrados Medios
    btn_cuadrados_medios = tk.Button(root, text="Cuadrados Medios", command=cuadrados_medios, width=20)
    btn_cuadrados_medios.pack(pady=10)
    
    # Botón para el método de Productos Medios
    btn_productos_medios = tk.Button(root, text="Productos Medios", command=productos_medios, width=20)
    btn_productos_medios.pack(pady=10)
    
    # Botón para el método del Multiplicador Constante
    btn_multiplicador_constante = tk.Button(root, text="Multiplicador Constante", command=multiplicador_constante, width=20)
    btn_multiplicador_constante.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Generación de números pseudo aleatorios")
root.geometry("600x600")  # Tamaño fijo para la ventana
root.resizable(False, False)  # Deshabilitar la redimensión de la ventana

# Llamar a la función para crear el menú principal
crear_menu()

# Iniciar la interfaz gráfica
root.mainloop()
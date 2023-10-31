import tkinter as tk
import random
import mysql.connector
import re 

# Conectarse a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fr123anco",
    database="preguntados"
)
cursor = db.cursor()


# Función para cargar una pregunta aleatoria desde la base de datos
def cargar_pregunta():
    cursor.execute("SELECT * FROM preguntas ORDER BY RAND() LIMIT 1")
    datos_pregunta = cursor.fetchone()
    etiqueta_pregunta.config(text=datos_pregunta[1])
    opciones = [datos_pregunta[2], datos_pregunta[3], datos_pregunta[4], datos_pregunta[5]]
    random.shuffle(opciones)
    boton_opcion1.config(text=opciones[0], state=tk.NORMAL)
    boton_opcion2.config(text=opciones[1], state=tk.NORMAL)
    boton_opcion3.config(text=opciones[2], state=tk.NORMAL)
    boton_opcion4.config(text=opciones[3], state=tk.NORMAL)
    respuesta_correcta.set(datos_pregunta[2])
    etiqueta_resultado.config(text="")
    respuesta_correcta_label.config(text="")
    boton_siguiente.config(state=tk.DISABLED)  # Deshabilitar el botón "Siguiente" al cargar una nueva pregunta



# Función para validar el campo de nombre
def validar_nombre():
    nombre = entrada_nombre.get()
    if nombre.isalpha():
        etiqueta_resultado.config(text="El nombre solo debe contener letras.")
        boton_comenzar.config(state=tk.NORMAL)  # Habilitar el botón "Comenzar" si el nombre es válido
    else:
        etiqueta_resultado.config(text="El nombre solo debe contener letras.")
        boton_comenzar.config(state=tk.DISABLED) 
        
        
# Función para verificar la respuesta y mostrar la respuesta correcta en caso de ser incorrecta
def verificar_respuesta(respuesta):
    if respuesta == respuesta_correcta.get():
        mensaje_respuesta.config(text="¡Correcto!", fg="green")
    else:
        mensaje_respuesta.config(text=f"Incorrecto. La respuesta correcta es: {respuesta_correcta.get()}", fg="red")
    boton_siguiente.config(state=tk.NORMAL)  # Habilitar el botón "Siguiente" después de responder


# Función para avanzar a la siguiente pregunta
def siguiente_pregunta():
    respuesta_correcta_label.config(text="")
    cargar_pregunta()
    etiqueta_resultado.config(text="")
    boton_siguiente.config(state=tk.DISABLED)  # Deshabilitar el botón "Siguiente" al cargar una nueva pregunta

def comenzar_juego():
    nombre = entrada_nombre.get()
    instagram = entrada_instagram.get()

    if not nombre.isalpha():
        etiqueta_resultado.config(text="El nombre solo debe contener letras.")
    else:
        etiqueta_nombre.config(text=f"Nombre: {nombre}")
        etiqueta_instagram.config(text=f"Instagram: {instagram}")
        entrada_nombre.pack_forget()
        entrada_instagram.pack_forget()
        boton_comenzar.pack_forget()
        cargar_pregunta()
        etiqueta_pregunta.pack()
        boton_opcion1.pack()
        boton_opcion2.pack()
        boton_opcion3.pack()
        boton_opcion4.pack()
        mensaje_respuesta.pack()
        boton_siguiente.pack()

# Función para validar el campo de nombre
def validar_nombre():
    nombre = entrada_nombre.get()
    if nombre.isalpha():
        comenzar_juego()
    else:
        etiqueta_resultado.config(text="El nombre solo debe contener letras.")

# Función para validar campos de entrada
def validar_campos(P):
    nombre = entrada_nombre.get()
    instagram = entrada_instagram.get()
    if nombre and instagram:
        boton_comenzar.config(state=tk.NORMAL)
    else:
        boton_comenzar.config(state=tk.DISABLED)
    return True

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Juego de Trivia")
raiz.geometry("800x600") 
# Configurar la geometría para que la ventana sea estática y ocupe toda la pantalla
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()
raiz.geometry(f"{ancho_pantalla}x{alto_pantalla}")


# Configurar colores
color_fondo = "light blue"
color_letras = "black"
color_widget = "white"


# Configurar los elementos de la interfaz inicial
etiqueta_nombre = tk.Label(raiz, text="Nombre:", bg=color_fondo, fg=color_letras)
etiqueta_instagram = tk.Label(raiz, text="Instagram:", bg=color_fondo, fg=color_letras)
entrada_nombre = tk.Entry(raiz, bg=color_widget, fg=color_letras)
entrada_instagram = tk.Entry(raiz, bg=color_widget, fg=color_letras)
boton_comenzar = tk.Button(raiz, text="Comenzar a Jugar", command=comenzar_juego, state=tk.DISABLED, bg=color_fondo, fg=color_letras)
etiqueta_resultado = tk.Label(raiz, text="", bg=color_fondo, fg=color_letras)

# Agregar validación a los campos de entrada
entrada_nombre.insert(0, "")
entrada_instagram.insert(0, "")
entrada_nombre.config(validate="key", validatecommand=(raiz.register(validar_campos), "%P"))
entrada_instagram.config(validate="key", validatecommand=(raiz.register(validar_campos), "%P"))
# Crear un marco para las respuestas
marco_respuestas = tk.Frame(raiz, bg="lightblue")  # Fondo azul claro
marco_respuestas.pack(expand=True, fill="both")

# Configurar las respuestas
respuesta1 = tk.Button(marco_respuestas, text="Respuesta 1", width=20, height=5)
respuesta2 = tk.Button(marco_respuestas, text="Respuesta 2", width=20, height=5)
respuesta3 = tk.Button(marco_respuestas, text="Respuesta 3", width=20, height=5)
respuesta4 = tk.Button(marco_respuestas, text="Respuesta 4", width=20, height=5)

# Organizar las respuestas en una disposición de cuadrado
respuesta1.grid(row=0, column=0, padx=10, pady=10)
respuesta2.grid(row=0, column=1, padx=10, pady=10)
respuesta3.grid(row=1, column=0, padx=10, pady=10)
respuesta4.grid(row=1, column=1, padx=10, pady=10)

# Colocar los elementos iniciales en la ventana
etiqueta_nombre.pack()
etiqueta_resultado.pack()  # Muestra el mensaje de validación aquí
entrada_nombre.pack()
etiqueta_instagram.pack()
entrada_instagram.pack()
boton_comenzar.pack()
boton_comenzar.config(state=tk.DISABLED)

# Crear y configurar los elementos de la interfaz del juego
etiqueta_pregunta = tk.Label(raiz, text="", wraplength=400)
boton_opcion1 = tk.Button(raiz, text="", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion1.cget("text")))
boton_opcion2 = tk.Button(raiz, text="", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion2.cget("text")))
boton_opcion3 = tk.Button(raiz, text="", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion3.cget("text")))
boton_opcion4 = tk.Button(raiz, text="", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion4.cget("text")))
boton_siguiente = tk.Button(raiz, text="Siguiente", state=tk.DISABLED, command=siguiente_pregunta)
respuesta_correcta_label = tk.Label(raiz, text="", fg="green")
etiqueta_resultado = tk.Label(raiz, text="")

# Asociar la función de validación con la entrada de nombre
validar_nombre_vcmd = raiz.register(validar_nombre)
# Configurar la validación en la entrada de nombre
entrada_nombre.config(validate="key", validatecommand=(raiz.register(validar_nombre), "%P"))
# Etiqueta para mostrar el mensaje de respuesta
mensaje_respuesta = tk.Label(raiz, text="", fg="green")

# Configurar el fondo de la ventana
raiz.configure(bg=color_fondo)



# Variable para almacenar la respuesta correcta
respuesta_correcta = tk.StringVar()

# Iniciar el bucle principal de tkinter
raiz.mainloop()

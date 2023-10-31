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

# Función para comenzar el juego y ocultar los elementos iniciales
def comenzar_juego():
    nombre = entrada_nombre.get()
    instagram = entrada_instagram.get()
    etiqueta_nombre.config(text=f"Nombre: {nombre}")
    etiqueta_instagram.config(text=f"Instagram: {instagram}")
    entrada_nombre.pack_forget()  # Ocultar el campo de entrada de nombre
    entrada_instagram.pack_forget()  # Ocultar el campo de entrada de Instagram
    boton_comenzar.pack_forget()  # Ocultar el botón "Comenzar"
    cargar_pregunta()
    etiqueta_pregunta.pack()
    mensaje_respuesta.pack()  # Mostrar la etiqueta de pregunta
    boton_opcion1.pack()  # Mostrar los botones de respuesta
    boton_opcion2.pack()
    boton_opcion3.pack()
    boton_opcion4.pack()
    boton_siguiente.pack()  # Mostrar el botón "Siguiente"



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
raiz.configure(bg="lightblue")  # Fondo azul claro

# Configurar colores
color_fondo = "light blue"
color_letras = "black"
color_widget = "white"

# Crear y configurar los elementos de la interfaz inicial
etiqueta_nombre = tk.Label(raiz, text="Nombre:", bg=color_fondo, fg=color_letras)
etiqueta_instagram = tk.Label(raiz, text="Instagram:", bg=color_fondo, fg=color_letras)
entrada_nombre = tk.Entry(raiz, bg=color_widget, fg=color_letras)
entrada_instagram = tk.Entry(raiz, bg=color_widget, fg=color_letras)
boton_comenzar = tk.Button(raiz, text="Comenzar a Jugar", command=comenzar_juego, state=tk.DISABLED, bg=color_fondo, fg=color_letras)
etiqueta_resultado = tk.Label(raiz, text="", bg=color_fondo, fg=color_letras)

# Organizar los elementos en la ventana
etiqueta_nombre.pack()
entrada_nombre.pack()
etiqueta_instagram.pack()
entrada_instagram.pack()
boton_comenzar.pack()


# Agregar validación a los campos de entrada
entrada_nombre.insert(0, "")
entrada_instagram.insert(0, "")
entrada_nombre.config(validate="key", validatecommand=(raiz.register(validar_campos), "%P"))
entrada_instagram.config(validate="key", validatecommand=(raiz.register(validar_campos), "%P"))
# Crear un marco para las respuestas
marco_respuestas = tk.Frame(raiz, bg="lightblue")
marco_respuestas.pack(expand=True, fill="both")

# Crear un marco para la pregunta
frame_pregunta = tk.Frame(raiz, bg="lightblue")
frame_pregunta.pack(expand=True, fill="both")


# Crear dos marcos para las opciones, uno para las dos primeras y otro para las dos últimas
frame_opciones_1 = tk.Frame(marco_respuestas, bg="lightblue")
frame_opciones_2 = tk.Frame(marco_respuestas, bg="lightblue")
frame_opciones_1.pack(side="left", expand=True, fill="both")
frame_opciones_2.pack(side="left", expand=True, fill="both")

# Configurar las respuestas
boton_opcion1 = tk.Button(frame_opciones_1, text="Respuesta 1", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion1.cget("text")))
boton_opcion2 = tk.Button(frame_opciones_1, text="Respuesta 2", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion2.cget("text")))
boton_opcion3 = tk.Button(frame_opciones_2, text="Respuesta 3", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion3.cget("text")))
boton_opcion4 = tk.Button(frame_opciones_2, text="Respuesta 4", state=tk.DISABLED, command=lambda: verificar_respuesta(boton_opcion4.cget("text")))
respuesta_correcta_label = tk.Label(raiz, text="", fg="green")
boton_siguiente = tk.Button(raiz, text="Siguiente", state=tk.DISABLED, command=siguiente_pregunta)

# Colocar los botones en los marcos de las opciones
boton_opcion1.pack(side="top", fill="both", expand=True)
boton_opcion2.pack(side="top", fill="both", expand=True)
boton_opcion3.pack(side="top", fill="both", expand=True)
boton_opcion4.pack(side="top", fill="both", expand=True)


# Configurar la etiqueta de la pregunta
etiqueta_pregunta = tk.Label(raiz, text="", wraplength=400)
etiqueta_pregunta.pack()


# Colocar los botones en los contenedores de opciones
boton_opcion1.pack(side="top", fill="both", expand=True)
boton_opcion2.pack(side="top", fill="both", expand=True)
boton_opcion3.pack(side="top", fill="both", expand=True)
boton_opcion4.pack(side="top", fill="both", expand=True)

# Etiqueta para mostrar el mensaje de respuesta
mensaje_respuesta = tk.Label(raiz, text="", fg="green")
mensaje_respuesta.pack()

# Botón Siguiente
boton_siguiente = tk.Button(raiz, text="Siguiente", state=tk.DISABLED, command=siguiente_pregunta)
boton_siguiente.pack()


# Variable para almacenar la respuesta correcta
respuesta_correcta = tk.StringVar()

# Iniciar el bucle principal de tkinter
raiz.mainloop()
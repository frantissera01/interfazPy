from tkinter import ttk
from tkinter import *
import mysql.connector
import time
import random

# Conectarse a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fr123anco",
    database="preguntados"
)
cursor = db.cursor()



global preguntas
cursor.execute("Select * from Preguntas")
preguntas = cursor.fetchall()

global preguntas_random
cursor.execute("Select * from Preguntas")
preguntas_random = cursor.fetchall()

random.shuffle(preguntas_random)

global puntaje
puntaje = 0

global tiempo
tiempo = 0

global tree

def empezar(numero, ventana_anterior, respuesta_anterior):
    global puntaje
    global tiempo
    global tree

    if numero > 15:
        tiempo = (time.time() - tiempo)
        minutos, segundos = divmod(tiempo, 60)
        datos_usuario = [nombre_entry.get(),  puntaje, f"{int(minutos)} : {int(segundos)}", instagram_entry.get()]
        print(datos_usuario)
        cursor.execute("INSERT INTO usuarios (nombre, puntaje, tiempo, instagram) VALUES (%s, %s, %s, %s)", (datos_usuario[0], datos_usuario[2], datos_usuario[3], datos_usuario[1]))
        db.commit()
        actualizar_tree()
        pass
    else:
        respuestas_random = []
        for i in range(0, 4):
            respuestas_random.append(preguntas_random[numero][2 + i])
        random.shuffle(respuestas_random)

        ventana_pregunta = Toplevel(root)
        ventana_pregunta.attributes("-fullscreen", True)
        ventana_pregunta.configure(bg="light blue")

        pregunta_titulo = Label(ventana_pregunta, text=preguntas_random[numero][1], bg="light blue", fg="black")
        pregunta_titulo.pack(pady=100)

         
        respuesta_1 = Button(ventana_pregunta, text=respuestas_random[0], command=lambda resp=respuestas_random[0]: empezar(numero + 1, ventana_pregunta, resp), width=100, height=2, bg="white", fg="black")
        respuesta_1.pack(pady=10)

        respuesta_2 = Button(ventana_pregunta, text=respuestas_random[1], command=lambda resp=respuestas_random[1]: empezar(numero + 1, ventana_pregunta, resp), width=100, height=2, bg="white", fg="black")
        respuesta_2.pack(pady=10)

        respuesta_3 = Button(ventana_pregunta, text=respuestas_random[2], command=lambda r=respuestas_random[2]: empezar(numero + 1, ventana_pregunta, r), width=100, height=2, bg="white", fg="black")
        respuesta_3.pack(pady=10)


        respuesta_4 = Button(ventana_pregunta, text=respuestas_random[3], command=lambda resp=respuestas_random[3]: empezar(numero + 1, ventana_pregunta, resp), width=100, height=2, bg="white", fg="black")
        respuesta_4.pack(pady=10)



    if ventana_anterior != 0:
        if respuesta_anterior == preguntas_random[numero-1][2]:
            puntos += 100
        ventana_anterior.destroy()
    else:
        puntos = 0
        tiempo = time.time()

def actualizar_tree():
    global tree
    tree.delete(*tree.get_children())
    cursor.execute("select nombre, puntaje, tiempo, instagram from usuarios order by puntaje DESC")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

root = Tk()
root.configure(bg="light blue")

titulo = Label(root, text="PREGUNTADOS ISAUI", bg="light blue", fg="black")
titulo.pack(pady=100)

nombre_label = Label(root, text="Nombre", bg="light blue", fg="black")
nombre_label.pack(pady=10)

nombre_entry = Entry(root)
nombre_entry.pack(pady=0)

instagram_label = Label(root, text="Instagram", bg="light blue", fg="black")
instagram_label.pack(pady=10)

instagram_entry = Entry(root)
instagram_entry.pack(pady=0)

boton_jugar = Button(root, text="Empezar", command=lambda: empezar(0, 0, 0), bg="white", fg="black")
boton_jugar.pack(pady=50)

tree = ttk.Treeview(root, columns=("Nombre", "Puntaje", "Tiempo", "Instagram"))
tree.pack()

tree.heading("#1", text="Nombre")
tree.heading("#2", text="Puntaje")
tree.heading("#3", text="Tiempo")
tree.heading("#4", text="Instagram")

tree.column("#0", width=0, stretch=NO)

actualizar_tree()

root.resizable(0, 0)
root.attributes("-fullscreen", True)
root.mainloop()

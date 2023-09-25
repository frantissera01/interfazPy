import tkinter as tk
from tkinter import ttk
import mysql.connector

# DNI Validation Function (Replace with your actual logic)
def validar_dni(dni):
    # Implement your DNI validation logic here
    # For example, you can check if the DNI is numeric and has the correct length
    return dni.isdigit() and len(dni) == 8

def cargar_datos():
    tree.delete(*tree.get_children())  
    cursor = conexion.cursor()
    # Add WHERE clause to filter students with id_estado_alumno = 1 (REGULARES)
    cursor.execute("SELECT Alumnos.Nombre, Alumnos.Apellido, Carreras.Nombre FROM Alumnos JOIN Carreras ON Alumnos.IDCarrera = Carreras.ID WHERE Alumnos.id_estado_alumno = 1")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fr123anco",
    database="ESCUELA"
)

root = tk.Tk()
root.title("Consulta de Alumnos")

tree = ttk.Treeview(root, columns=("Nombre", "Apellido", "Carrera"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Apellido")
tree.heading("#3", text="Carrera")
tree.column("#0", width=0, stretch=tk.NO) 
tree.pack(padx=10, pady=10)

cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

root.mainloop()

conexion.close()

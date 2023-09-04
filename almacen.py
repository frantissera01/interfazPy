import mysql.connector
import tkinter as tk
from tkinter import ttk

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'almacen'
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Conexión a MySQL exitosa!")

   

except mysql.connector.Error as err:
    print(f"Error de conexión a MySQL: {err}")


def cargar_datos():
    tree.delete(*tree.get_children()) 
    cursor = conn.cursor()
    cursor.execute("SELECT producto.nombre, categoria.nombre, marca.nombre, producto.stock, producto.precio FROM producto JOIN categoria ON producto.id_categoria = categoria.codcategoria JOIN marca ON marca.codcategoria=producto.id_marca")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

root = tk.Tk()
root.title("Consulta de productos")

tree = ttk.Treeview(root, columns=("Nombre", "categoria", "marca", "stock", "precio"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="categoria")
tree.heading("#3", text="marca")
tree.heading("#4", text="stock")
tree.heading("#5", text="precio")
tree.column("#0", width=0, stretch=tk.NO)  
tree.pack(padx=10, pady=10)


cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

root.mainloop()

conn.close()
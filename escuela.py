import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(host="localhost", user="root", password="fr123anco", database="ESCUELA")

# Función para validar el formato de un DNI (opcional)
def validar_dni():
    dni= dni_entry.get()
    if "." in dni:
        dni=dni.replace(".","")
    if len(dni)!=8:
        messagebox.showerror("El numero documento debe contener 8 digitos. ")
    else:
        try:
            int(dni)
            return (dni)
        except:
            messagebox.showerror("El numero documento no admite letras")
  
# Función para cargar las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras():
   cursor=conexion.cursor()
   cursor.execute("SELECT IDCARRERA, NOMBRE FROM Carreras ORDER BY NOMBRE")
   carreras=cursor.fetchall()
   carrera_combobox['values'] = [row [1] for row in carreras ]
   print(carreras)
   return carreras

# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_alumno = condicion_combobox.get()  # Obtener el estado del ComboBox

    if nombre and apellido and dni and carrera_nombre and estado_alumno:
        # Obtener el ID de la carrera seleccionada
        carreras = cargar_carreras()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break

        cursor = conexion.cursor()
        # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el estado del alumno
        cursor.execute("INSERT INTO Alumnos (Nombre, Apellido, DNI, IDCarrera, Condicion) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, carrera_id, estado_alumno))
        conexion.commit()
        cargar_datos()  # Actualizar la vista
        # Limpiar los campos después de insertar
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
        condicion_combobox.set("")  # Limpiar la selección del ComboBox
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT Alumnos.NOMBRE, Alumnos.APELLIDO, Alumnos.DNI, Carreras.NOMBRE, estadoalumno.NOMBRE FROM Alumnos JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN estadoalumno ON Alumnos.IDESTADOALUMNO = estadoalumno.IDESTADOALUMNO WHERE Alumnos.IDEstadoAlumno=1 ")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Función para cargar el estado de un alumno (Regular, Libre o Promocional)
def cargar_estado_alumno(alumno_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT Condicion FROM Alumnos WHERE ID = %s", (alumno_id,))
    estado_alumno = cursor.fetchone()
    return estado_alumno[0] if estado_alumno else None

# Función para modificar el estado de un alumno
def modificar_alumno():
    selected_item = tree.selection()  # Obtener el elemento seleccionado en el Treeview
    if not selected_item:
        mostrar_alerta("Por favor, seleccione un alumno para modificar.")
        return

    alumno_id = selected_item[0]
    estado_actual = cargar_estado_alumno(alumno_id)

    if estado_actual is None:
        mostrar_alerta("No se pudo obtener el estado actual del alumno.")
        return

    # Cambiar el estado del alumno a 'Libre' si es 'Regular' o 'Regular' si es 'Libre'
    nuevo_estado = 'Libre' if estado_actual == 'Regular' else 'Regular'

    cursor = conexion.cursor()
    cursor.execute("UPDATE Alumnos SET Condicion = %s WHERE ID = %s", (nuevo_estado, alumno_id))
    conexion.commit()
    cargar_datos()  # Actualizar la vista
    mostrar_alerta(f"El estado del alumno ha sido modificado a {nuevo_estado}.")

# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

# Crear ventana
root = tk.Tk()
root.title("ABM de Alumnos - Escuela")

# Crear un frame con un borde visible para el formulario de inscripción
formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.pack(padx=10, pady=10)

# Título del formulario
titulo_label = tk.Label(formulario_frame, text="Formulario de Alumnos", font=("Helvetica", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada para nombre, apellido y DNI con el mismo ancho que el ComboBox
nombre_label = tk.Label(formulario_frame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para la carrera
carrera_label=tk.Label(formulario_frame, text="Carrera: ")
carrera_label.grid(row=4, column=0)
carrera_combobox= ttk.Combobox(formulario_frame, state="readonly")
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para la condición del alumno
condicion_label = tk.Label(formulario_frame, text="Condición:")
condicion_label.grid(row=5, column=0)
condicion_combobox = ttk.Combobox(formulario_frame, state="readonly")  # Configurar el ComboBox como de solo lectura
condicion_combobox.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")
condicion_combobox['values'] = ["Libre", "Regular", "Promocional"]

# Botón para guardar un nuevo registro de alumno
guardar_button = tk.Button(formulario_frame, text="Guardar", command=guardar_alumno)
guardar_button.grid(row=6, columnspan=2, pady=10, sticky="ew")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("Nombre", "Apellido", "Carrera", "Estado"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Apellido")
tree.heading("#3", text="Carrera")
tree.heading("#4", text="Estado")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.pack(padx=10, pady=10)

# Botón para cargar datos
cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

# Botón para modificar el estado de un alumno
modificar_button = tk.Button(root, text="Modificar Estado", command=modificar_alumno)
modificar_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()

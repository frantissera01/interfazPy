import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

conexion = mysql.connector.connect(host="localhost", user="root", password="fr123anco", database="ESCUELA")

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT Alumnos.ID, Alumnos.NOMBRE, Alumnos.APELLIDO, Carreras.NOMBRE, Alumnos.Condicion FROM Alumnos JOIN Carreras ON Alumnos.IDCarrera = Carreras.ID")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
        
# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    tk.messagebox.showwarning("Alerta", mensaje)
    
# ...

# Variable global para almacenar el ID del registro seleccionado
registro_seleccionado_id = None
estado_combobox_enabled = False  # Variable para habilitar/deshabilitar el ComboBox de estado

# Función para seleccionar un registro en el Treeview
def seleccionar_registro(event):
    global registro_seleccionado_id, estado_combobox_enabled
    item = tree.selection()[0]
    registro_seleccionado_id = item
    valores = tree.item(item, "values")
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("")
    estado_combobox.set("")
    nombre_entry.insert(0, valores[1])
    apellido_entry.insert(0, valores[2])
    dni_entry.insert(0, valores[0])
    carrera_combobox.set(valores[3])
    estado_combobox.set(valores[4])
    estado_combobox_enabled = True  # Habilitar el ComboBox de estado


# Función para guardar cambios en un registro existente
def guardar_cambios():
    global registro_seleccionado_id
    if registro_seleccionado_id:
        nombre = nombre_entry.get().upper()
        apellido = apellido_entry.get().upper()
        dni = dni_entry.get()
        carrera_nombre = carrera_combobox.get()
        estado_alumno_nombre = estado_combobox.get()

        if nombre and apellido and dni and carrera_nombre and estado_alumno_nombre:
            # Validar el formato del DNI
            if not validar_dni(dni):
                mostrar_alerta("El DNI debe contener 8 dígitos numéricos.")
                return

            # Obtener el ID de la carrera seleccionada
            carreras = cargar_carreras()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == carrera_nombre:
                    carrera_id = carrera[0]
                    break

            cursor = conexion.cursor()
            # Actualizar el registro en la tabla Alumnos con el ID de carrera y el estado del alumno
            cursor.execute("UPDATE Alumnos SET NOMBRE = %s, APELLIDO = %s, DNI = %s, IDCarrera = %s, Condicion = %s WHERE ID = %s", (nombre, apellido, dni, carrera_id, estado_alumno_nombre, registro_seleccionado_id))
            conexion.commit()
            cargar_datos()  # Actualizar la vista
            # Limpiar los campos después de actualizar
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  # Limpiar la selección del ComboBox
            estado_combobox.set("")   # Limpiar la selección del ComboBox de estado
            estado_combobox_enabled = False  # Deshabilitar el ComboBox de estado
            # Restablecer la variable de registro seleccionado
            registro_seleccionado_id = None
        else:
            mostrar_alerta("Los campos son obligatorios. Debe completarlos.")
    else:
        mostrar_alerta("Seleccione un registro para modificar.")
        
# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_alumno_nombre = estado_combobox.get()

    if nombre and apellido and dni and carrera_nombre and estado_alumno_nombre:
        # Validar el formato del DNI
        if not validar_dni(dni):
            mostrar_alerta("El DNI debe contener 8 dígitos numéricos.")
            return

        # Obtener el ID de la carrera seleccionada
        carreras = cargar_carreras()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break

        # Obtener el ID del estado del alumno seleccionado
        estados = cargar_estadoAlumno()
        estado_alumno_id = None
        for estado in estados:
            if estado[0] == estado_alumno_nombre:
                estado_alumno_id = estado[1]
                break

        cursor = conexion.cursor()
        # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el ID de estado del alumno
        cursor.execute("INSERT INTO Alumnos (NOMBRE, APELLIDO, DNI, IDCarrera, Condicion) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, carrera_id, estado_alumno_id))
        conexion.commit()
        cargar_datos()  # Actualizar la vista
        # Limpiar los campos después de insertar
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
        estado_combobox.set("")   # Limpiar la selección del ComboBox de estado
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")

# Función para obtener las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("SELECT IDCARRERA, NOMBRE FROM Carreras ORDER BY NOMBRE")
    carreras = cursor.fetchall()
    carrera_combobox['values'] = [row[1] for row in carreras]
    return carreras  # Devolver también la lista de carreras con sus IDs


# Función para cargar los estados de los alumnos en el ComboBox
def cargar_estadoAlumno():
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT Condicion FROM Alumnos")
    estados = cursor.fetchall()
    estado_combobox['values'] = [row[0] for row in estados]
    return estados

# Función para validar el formato del DNI
def validar_dni(dni):
    # Verificar si el DNI tiene exactamente 8 dígitos
    return dni.isdigit() and len(dni) == 8

# Crear ventana
root = tk.Tk()
root.title("Consulta de Alumnos")

# Crear un frame con un borde visible para el formulario de inscripción
formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.pack(padx=10, pady=10)

# Título del formulario
titulo_label = tk.Label(formulario_frame, text="Formulario Inscripción", font=("Helvetica", 14))
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
carrera_label = tk.Label(formulario_frame, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame, state="readonly")
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")


# Combo box para el estado del alumno
estado_label = tk.Label(formulario_frame, text="Estado del Alumno:")
estado_label.grid(row=5, column=0)
estado_combobox = ttk.Combobox(formulario_frame, state="readonly")
estado_combobox.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Botón para guardar un nuevo registro de alumno
guardar_button = tk.Button(formulario_frame, text="Guardar", command=guardar_alumno)
guardar_button.grid(row=6, columnspan=2, pady=10, sticky="ew")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("DNI", "Nombre", "Apellido", "Carrera", "Condicion"))
tree.heading("#1", text="DNI")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Apellido")
tree.heading("#4", text="Carrera")
tree.heading("#5", text="Condicion")
tree.column("#0", width=0, stretch=tk.NO)
tree.pack(padx=10, pady=10)

# Crear un frame para los botones
botones_frame = tk.Frame(root)
botones_frame.pack()

# Botón para cargar datos
cargar_button = tk.Button(botones_frame, text="Cargar Datos", command=cargar_datos)
cargar_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Botón para seleccionar un registro y cargarlo en el formulario
modificar_button = tk.Button(botones_frame, text="Modificar", command=seleccionar_registro)
modificar_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Botón para guardar cambios en un registro seleccionado
guardar_cambios_button = tk.Button(botones_frame, text="Guardar Cambios", command=guardar_cambios)
guardar_cambios_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Ejecutar la aplicación
root.mainloop()


# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()

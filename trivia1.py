import tkinter as tk
import random
import time
import mysql.connector
from tkinter import messagebox
import tkinter as ttk


# Conectar a la base de datos MySQL (reemplaza con tus propios datos)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fr123anco",
    database="preguntados"
)
cursor = conn.cursor()


# Crear tablas y agregar preguntas (código de creación de tablas e inserción de preguntas)

class PreguntadosGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Preguntados Game")

        # Configurar el tamaño fijo de la ventana
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.user_name = tk.StringVar()
        self.instagram = tk.StringVar()

        name_label = tk.Label(root, text="Nombre:", font=("Times New Roman", 14))
        name_label.pack()

        name_entry = tk.Entry(root, textvariable=self.user_name, font=("Times New Roman", 12))
        name_entry.pack()

        instagram_label = tk.Label(root, text="Instagram:", font=("Times New Roman", 14))
        instagram_label.pack()

        instagram_entry = tk.Entry(root, textvariable=self.instagram, font=("Times New Roman", 12))
        instagram_entry.pack()

        start_button = tk.Button(root, text="Jugar", command=self.start_game, font=("Times New Roman", 14))
        start_button.pack()

    def start_game(self):
        user_name = self.user_name.get()
        user_instagram = self.instagram.get()

        if user_name and user_instagram:
            self.root.destroy()  # Cerrar la ventana de inicio
            # Crear una nueva ventana para el juego principal
            game_window = tk.Toplevel()
            game = GameWindow(game_window, user_name, user_instagram)
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

class PreguntadosGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Preguntados Game")

        # Configurar el tamaño fijo de la ventana
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.user_name = tk.StringVar()
        self.instagram = tk.StringVar()

        name_label = tk.Label(root, text="Nombre:", font=("Times New Roman", 14))
        name_label.pack()

        name_entry = tk.Entry(root, textvariable=self.user_name, font=("Times New Roman", 12))
        name_entry.pack()

        instagram_label = tk.Label(root, text="Instagram:", font=("Times New Roman", 14))
        instagram_label.pack()

        instagram_entry = tk.Entry(root, textvariable=self.instagram, font=("Times New Roman", 12))
        instagram_entry.pack()

        start_button = tk.Button(root, text="Jugar", command=self.start_game, font=("Times New Roman", 14))
        start_button.pack()

    def start_game(self):
        user_name = self.user_name.get()
        user_instagram = self.instagram.get()

        if user_name and user_instagram:
            self.root.destroy()  # Cerrar la ventana de inicio
            # Crear una nueva ventana para el juego principal
            game_window = tk.Toplevel()
            game = GameWindow(game_window, user_name, user_instagram)
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

class GameWindow:
    def __init__(self, root, user_name, user_instagram):
        self.root = root
        self.root.title("Preguntados Game")
        self.user_name = user_name
        self.user_instagram = user_instagram
        self.score = 0
        self.current_question = 0
        self.start_time = time.time()

        # Configurar colores y estilo
        self.background_color = 'lightblue'
        self.text_color = 'white'

        self.root.configure(bg=self.background_color)

        self.questions = []

        cursor.execute('SELECT * FROM preguntas')
        for row in cursor.fetchall():
            self.questions.append(row)

        self.question_label = tk.Label(root, text="", font=("Times New Roman", 18), bg=self.background_color, fg=self.text_color)
        self.question_label.pack()

        self.answer_var = tk.StringVar()
        self.answer_var.set(-1)

        options = tk.StringVar(value=("Opción 1", "Opción 2", "Opción 3"))
        self.spinbox = tk.Spinbox(root, values=options, textvariable=self.answer_var, bg=self.background_color)
        self.spinbox.pack()

        self.check_button = tk.Button(root, text="Comprobar", command=self.check_answer, bg=self.background_color)
        self.check_button.pack()

        self.next_button = tk.Button(root, text="Siguiente Pregunta", command=self.next_question, state=tk.DISABLED, bg=self.background_color)
        self.next_button.pack()

        # Crear una ventana interior para la lista de participantes
        participants_frame = tk.Frame(root, bg=self.background_color)
        participants_frame.pack(fill="both", expand=True)

        # Añadir un Canvas con un Scrollbar vertical
        self.canvas = tk.Canvas(participants_frame, bg=self.background_color)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(participants_frame, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas, bg=self.background_color)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Configurar el Scrollbar para desplazar la lista
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.create_participants_list()

        self.update_question()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.inner_frame, width=event.width)

    def create_participants_list(self):
        # Crear un Treeview para mostrar la lista de participantes
        self.tree = ttk.Treeview(self.inner_frame, columns=("Puntaje", "Tiempo"), height=10)
        self.tree.heading("#1", text="Puntaje")
        self.tree.heading("#2", text="Tiempo")
        self.tree.column("#1", width=100)
        self.tree.column("#2", width=100)
        self.tree.pack()

    def update_participants_list(self, data):
        # Limpiar la lista
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Agregar los datos de los participantes
        for row in data:
            self.tree.insert("", "end", values=row)

    def update_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data[1])
            self.question_label.config(bg=self.background_color, fg=self.text_color)
            options = [question_data[2], question_data[3], question_data[4]]
            random.shuffle(options)
            self.spinbox.config(values=options, bg=self.background_color, fg=self.text_color)
        else:
            self.question_label.config(text="Juego Terminado. Puntaje: {}".format(self.score), bg=self.background_color, fg=self.text_color)
            self.spinbox.config(state=tk.DISABLED)
            self.check_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)
            self.insert_user_data()
            self.show_participants()
            conn.close()

    def check_answer(self):
        selected_index = int(self.answer_var.get())
        if selected_index == -1:
            messagebox.showerror("Error", "Por favor, selecciona una respuesta antes de continuar.")
            return

        question_data = self.questions[self.current_question]
        if selected_index == question_data[5]:
            self.score += 100
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.answer_var.set(-1)
        self.next_button.config(state=tk.DISABLED)
        self.update_question()

    def insert_user_data(self):
        nombre = self.user_name
        instagram = self.user_instagram
        tiempo_respondido = int(time.time() - self.start_time)

        cursor.execute('INSERT INTO usuarios (nombre, instagram, puntaje, tiempo_respondido) VALUES (%s, %s, %s, %s)',
                       (nombre, instagram, self.score, tiempo_respondido))
        conn.commit()

    def show_participants(self):
        cursor.execute('SELECT nombre, puntaje, tiempo_respondido FROM usuarios ORDER BY tiempo_respondido ASC')
        data = cursor.fetchall()
        self.update_participants_list(data)


if __name__ == "__main__":
    root = tk.Tk()
    game = PreguntadosGame(root)
    root.mainloop()
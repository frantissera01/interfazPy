import tkinter as tk
from math import factorial
import decimal
import random

##ejercicio 1.1
"""class ContCreciente:
    def __init__(self, root):
        self.root = root
        self.root.title("ContCreciente")

        self.contador = 0

        self.label = tk.Label(root, text="Contador")
        self.label.pack()

        self.valor_contador = tk.StringVar()
        self.valor_contador.set(str(self.contador))
        self.lineEdit = tk.Entry(root, textvariable=self.valor_contador, state="readonly")
        self.lineEdit.pack()

        self.boton_mas = tk.Button(root, text="+", command=self.incrementar_contador)
        self.boton_mas.pack()

    def incrementar_contador(self):
        self.contador += 1
        self.valor_contador.set(str(self.contador))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContCreciente(root)
    root.mainloop()"""
    
    
##ejercicio 1.2
"""class Decreciente:
    def __init__(self, root):
        self.root = root
        self.root.title("ConDecreciente")

        
        self.contador =88

        self.label = tk.Label(root, text="Contador")
        self.label.pack()

        self.valor_contador = tk.StringVar()
        self.valor_contador.set(str(self.contador))
        self.lineEdit = tk.Entry(root, textvariable=self.valor_contador, state="readonly")
        self.lineEdit.pack()

    
        self.boton_menos=tk.Button(root, text="-", command=self.decreciente_contador)
        self.boton_menos.pack()
   
    def decreciente_contador(self):
        self.contador-= 1 
        self.valor_contador.set(str(self.contador))
        
   
if __name__ == "__main__":
    root = tk.Tk()
    app = Decreciente(root)
    root.mainloop()"""
    
##ejercicio 1.3

"""
class Factorial:
    def __init__(self, root):
        self.root = root
        self.root.title("Factorial App")

        self.n = 1

        self.n_label = tk.Label(root, text="n:")
        self.factorial_label = tk.Label(root, text="Factorial (n):")
        self.n_lineedit = tk.Entry(root)
        self.n_lineedit.insert(0, str(self.n))
        self.n_lineedit.config(state="readonly")
        self.factorial_lineedit = tk.Entry(root)
        self.factorial_lineedit.config(state="readonly")
        self.next_button = tk.Button(root, text="Siguiente", command=self.calculate_factorial)

        self.n_label.pack()
        self.n_lineedit.pack()
        self.factorial_label.pack()
        self.factorial_lineedit.pack()
        self.next_button.pack()

    def calculate_factorial(self):
        self.n += 1
        self.n_lineedit.config(state="normal")
        self.n_lineedit.delete(0, tk.END)
        self.n_lineedit.insert(0, str(self.n))
        self.n_lineedit.config(state="readonly")

        result = factorial(self.n)
        self.factorial_lineedit.config(state="normal")
        self.factorial_lineedit.delete(0, tk.END)
        self.factorial_lineedit.insert(0, str(result))
        self.factorial_lineedit.config(state="readonly")

def main():
    root = tk.Tk()
    app = Factorial(root)
    root.mainloop()

if __name__ == "__main__":
    main()"""
    
##ejercicio 1.4


"""""
class Contador1:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")

        self.counter_value = 0

        self.counter_label = tk.Label(root, text="Contador")
        self.counter_lineedit = tk.Entry(root)
        self.counter_lineedit.insert(0, str(self.counter_value))
        self.counter_lineedit.config(state="readonly")

        self.count_up_button = tk.Button(root, text="Count Up", command=self.count_up)
        self.count_down_button = tk.Button(root, text="Count Down", command=self.count_down)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)

        self.counter_label.pack()
        self.counter_lineedit.pack()
        self.count_up_button.pack()
        self.count_down_button.pack()
        self.reset_button.pack()

    def update_counter_display(self):
        self.counter_lineedit.config(state="normal")
        self.counter_lineedit.delete(0, tk.END)
        self.counter_lineedit.insert(0, str(self.counter_value))
        self.counter_lineedit.config(state="readonly")

    def count_up(self):
        self.counter_value += 1
        self.update_counter_display()

    def count_down(self):
        self.counter_value -= 1
        self.update_counter_display()

    def reset(self):
        self.counter_value = 0
        self.update_counter_display()

def main():
    root = tk.Tk()
    app = Contador1(root)
    root.mainloop()

if __name__ == "__main__":
    main()"""

#ejercicio 2.1 
"""""
class Calculadora1:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.first_num_label = tk.Label(root, text="Primer número")
        self.second_num_label = tk.Label(root, text="Segundo número")
        self.result_label = tk.Label(root, text="Resultado")

        self.first_num_entry = tk.Entry(root)
        self.second_num_entry = tk.Entry(root)
        self.result_entry = tk.Entry(root)
        self.result_entry.config(state="readonly")

        self.add_button = tk.Button(root, text="+", command=self.add)
        self.subtract_button = tk.Button(root, text="-", command=self.subtract)
        self.multiply_button = tk.Button(root, text="*", command=self.multiply)
        self.divide_button = tk.Button(root, text="/", command=self.divide)
        self.modulo_button = tk.Button(root, text="%", command=self.modulo)
        self.clear_button = tk.Button(root, text="CLEAR", command=self.clear)

        self.first_num_label.grid(row=0, column=0, padx=10, pady=5)
        self.first_num_entry.grid(row=0, column=1, padx=10, pady=5)
        self.second_num_label.grid(row=1, column=0, padx=10, pady=5)
        self.second_num_entry.grid(row=1, column=1, padx=10, pady=5)
        self.result_label.grid(row=2, column=0, padx=10, pady=5)
        self.result_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button.grid(row=3, column=0, padx=10, pady=5)
        self.subtract_button.grid(row=3, column=1, padx=10, pady=5)
        self.multiply_button.grid(row=4, column=0, padx=10, pady=5)
        self.divide_button.grid(row=4, column=1, padx=10, pady=5)
        self.modulo_button.grid(row=5, column=0, padx=10, pady=5)
        self.clear_button.grid(row=5, column=1, padx=10, pady=5)

    def clear(self):
        self.first_num_entry.delete(0, tk.END)
        self.second_num_entry.delete(0, tk.END)
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.config(state="readonly")

    def update_result(self, value):
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, value)
        self.result_entry.config(state="readonly")

    def show_error(self):
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, "Error")
        self.result_entry.config(state="readonly")

    def perform_operation(self, operation):
        try:
            first_num = float(self.first_num_entry.get())
            second_num = float(self.second_num_entry.get())
            if operation == "+":
                result = first_num + second_num
            elif operation == "-":
                result = first_num - second_num
            elif operation == "*":
                result = first_num * second_num
            elif operation == "/":
                if second_num != 0:
                    result = first_num / second_num
                else:
                    self.clear()
                    return
            elif operation == "%":
                if second_num != 0:
                    result = first_num % second_num
                else:
                    self.clear()
                    return
            self.update_result(result)
        except ValueError:
            self.show_error()

    def add(self):
        self.perform_operation("+")

    def subtract(self):
        self.perform_operation("-")

    def multiply(self):
        self.perform_operation("*")

    def divide(self):
        self.perform_operation("/")

    def modulo(self):
        self.perform_operation("%")

def main():
    root = tk.Tk()
    app = Calculadora1(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    """
    
#ejercicio 2.2
"""""
class Pelis:
    def __init__(self, root):
        self.root = root
        self.root.title("Películas")

        self.movie_label = tk.Label(root, text="Escribe el título de una película")
        self.movies_label = tk.Label(root, text="Películas")

        self.movie_entry = tk.Entry(root)
        self.movies_listbox = tk.Listbox(root)

        self.add_button = tk.Button(root, text="Añadir", command=self.add_movie)

        self.movie_label.pack(padx=10, pady=5)
        self.movie_entry.pack(padx=10, pady=5)
        self.add_button.pack(padx=10, pady=5)
        self.movies_label.pack(padx=10, pady=5)
        self.movies_listbox.pack(padx=10, pady=5)

    def add_movie(self):
        movie_name = self.movie_entry.get()
        if movie_name:
            self.movies_listbox.insert(tk.END, movie_name)
            self.movie_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = Pelis(root)
    root.mainloop()

if __name__ == "__main__":
    main()"""

#ejercicio 2.3 

"""""
class NumeroRandom:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de números")

        self.num1_label = tk.Label(root, text="Número 1")
        self.num2_label = tk.Label(root, text="Número 2")
        self.generated_label = tk.Label(root, text="Número Generado")

        self.num1_spinbox = tk.Spinbox(root, from_=1, to=100)
        self.num2_spinbox = tk.Spinbox(root, from_=1, to=100)
        self.generated_entry = tk.Entry(root)
        self.generated_entry.config(state="readonly")

        self.generate_button = tk.Button(root, text="Generar", command=self.generate_number)

        self.num1_label.pack(padx=10, pady=5)
        self.num1_spinbox.pack(padx=10, pady=5)
        self.num2_label.pack(padx=10, pady=5)
        self.num2_spinbox.pack(padx=10, pady=5)
        self.generate_button.pack(padx=10, pady=5)
        self.generated_label.pack(padx=10, pady=5)
        self.generated_entry.pack(padx=10, pady=5)

    def generate_number(self):
        num1 = int(self.num1_spinbox.get())
        num2 = int(self.num2_spinbox.get())
        if num1 <= num2:
            generated_num = random.randint(num1, num2)
            self.generated_entry.config(state="normal")
            self.generated_entry.delete(0, tk.END)
            self.generated_entry.insert(0, str(generated_num))
            self.generated_entry.config(state="readonly")

def main():
    root = tk.Tk()
    app = NumeroRandom(root)
    root.mainloop()

if __name__ == "__main__":
    main()"""""

#ejercicio 2.4

"""
class Calculadora2:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora 2")

        self.value1_label = tk.Label(root, text="Valor 1")
        self.value2_label = tk.Label(root, text="Valor 2")
        self.result_label = tk.Label(root, text="Resultado")
        self.operation_label = tk.Label(root, text="Operaciones")

        self.value1_entry = tk.Entry(root)
        self.value2_entry = tk.Entry(root)
        self.result_entry = tk.Entry(root)
        self.result_entry.config(state="readonly")

        self.operation_var = tk.StringVar(value="Sumar")
        self.sum_radio = tk.Radiobutton(root, text="Sumar", variable=self.operation_var, value="Sumar")
        self.subtract_radio = tk.Radiobutton(root, text="Restar", variable=self.operation_var, value="Restar")
        self.multiply_radio = tk.Radiobutton(root, text="Multiplicar", variable=self.operation_var, value="Multiplicar")
        self.divide_radio = tk.Radiobutton(root, text="Dividir", variable=self.operation_var, value="Dividir")

        self.calculate_button = tk.Button(root, text="Calcular", command=self.calculate)

        self.value1_label.grid(row=0, column=0, padx=10, pady=5)
        self.value1_entry.grid(row=0, column=1, padx=10, pady=5)
        self.value2_label.grid(row=1, column=0, padx=10, pady=5)
        self.value2_entry.grid(row=1, column=1, padx=10, pady=5)
        self.result_label.grid(row=2, column=0, padx=10, pady=5)
        self.result_entry.grid(row=2, column=1, padx=10, pady=5)
        self.operation_label.grid(row=3, column=0, padx=10, pady=5)
        self.sum_radio.grid(row=3, column=1, padx=10, pady=5)
        self.subtract_radio.grid(row=4, column=1, padx=10, pady=5)
        self.multiply_radio.grid(row=5, column=1, padx=10, pady=5)
        self.divide_radio.grid(row=6, column=1, padx=10, pady=5)
        self.calculate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def calculate(self):
        try:
            value1 = float(self.value1_entry.get())
            value2 = float(self.value2_entry.get())
            operation = self.operation_var.get()

            if operation == "Sumar":
                result = value1 + value2
            elif operation == "Restar":
                result = value1 - value2
            elif operation == "Multiplicar":
                result = value1 * value2
            elif operation == "Dividir":
                if value2 != 0:
                    result = value1 / value2
                else:
                    self.result_entry.config(state="normal")
                    self.result_entry.delete(0, tk.END)
                    self.result_entry.insert(0, "Error: División por cero")
                    self.result_entry.config(state="readonly")
                    return

            self.result_entry.config(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
            self.result_entry.config(state="readonly")
        except ValueError:
            self.result_entry.config(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Error: Valores no válidos")
            self.result_entry.config(state="readonly")

def main():
    root = tk.Tk()
    app = Calculadora2(root)
    root.mainloop()

if __name__ == "__main__":
    main()"""


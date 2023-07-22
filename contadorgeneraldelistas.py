import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import string

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.agregar_menu()
        self.scrolledtext1 = st.ScrolledText(self.ventana1, width=80, height=20)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Abrir archivo", command=self.abrir)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

    def salir(self):
        sys.exit()

    def abrir(self):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo", filetypes=(("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch != '':
            archi1 = open(nombrearch, "r", encoding="utf-8")
            contenido = archi1.read()
            archi1.close()

            # Contar número de líneas que contiene el archivo
            num_lineas = contenido.count('\n') + 1

            # Contar número de palabras que contiene el archivo
            palabras = contenido.split()
            num_palabras = len(palabras)

            # Guardar palabras, números y signos en listas separadas
            lista_palabras = []
            lista_numeros = []
            lista_signos = []

            for palabra in palabras:
                palabra_limpia = palabra.strip(string.punctuation)
                if palabra_limpia.isdigit():
                    lista_numeros.append(palabra_limpia)
                elif palabra_limpia:
                    lista_palabras.append(palabra_limpia)
            
            for signo in contenido:
                if signo in string.punctuation:
                    lista_signos.append(signo)

            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)

            # Mostrar mensajes con palabras, números y signos
            self.mostrar_mensaje_palabras(lista_palabras)
            self.mostrar_mensaje_signos(lista_signos)
            self.mostrar_mensaje_numeros(lista_numeros)

            # Mostrar el resultado del cálculo
            mensaje = f"Número de líneas: {num_lineas}\nNúmero de palabras: {num_palabras}\n"
            mensaje += f"Número de palabras encontradas: {len(lista_palabras)}\n"
            mensaje += f"Número de números encontrados: {len(lista_numeros)}\n"
            mensaje += f"Número de signos encontrados: {len(lista_signos)}"
            mb.showinfo("Información", mensaje)

    def mostrar_mensaje_palabras(self, lista_palabras):
        palabras_str = "\n".join(lista_palabras)
        mb.showinfo("Palabras encontradas", palabras_str)

    def mostrar_mensaje_signos(self, lista_signos):
        signos_str = " ".join(lista_signos)
        mb.showinfo("Signos encontrados", signos_str)

    def mostrar_mensaje_numeros(self, lista_numeros):
        numeros_str = " ".join(lista_numeros)
        mb.showinfo("Números encontrados", numeros_str)


aplicacion1 = Aplicacion()


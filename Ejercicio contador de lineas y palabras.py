import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
#Este codigo usa la libreria Tk para agregar una interfaz grafica al codigo y poder visualizar lo que se esta compilando y poder abrir el archivo
#por medio de una lista despegable
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

            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

            # Mostrar el resultado del calculo
            mensaje = f"Número de líneas: {num_lineas}\nNúmero de palabras: {num_palabras}"
            mb.showinfo("Información", mensaje)


aplicacion1 = Aplicacion()

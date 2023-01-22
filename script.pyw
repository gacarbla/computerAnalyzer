from asyncio.windows_events import NULL
from copyreg import constructor
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import IntVar
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from subprocess import check_output
import math
from turtle import width

ventana1=tk.Tk()
ventana1.resizable(0, 0)
menubar = tk.Menu(ventana1)
ventana1.config(menu=menubar)

iev = IntVar()
irv = IntVar()
hrv = IntVar()
pev = IntVar()

def salir():
        sys.exit()

def info():
        mb.showerror("Error", "Este módulo no está disponible")

def ayuda():
        mb.showerror("Error", "Este módulo no está disponible")

def debug():
        mb.showerror("Error", "Este módulo no está disponible")

def nuevo():
    ir = irv.get()
    hr = hrv.get()
    pe = pev.get()
    ie = iev.get()
    if ((ir==1) or (hr==1) or (pe==1) or (ie==1)):
        nombrearch=fd.asksaveasfilename(initialdir = "/", defaultextension=".lhf", title = "Guardar nuevo",filetypes = (("Archivo de registro protegido","*.lhf"),("Archivo de registro","*.dhf"),("Archivos de texto","*.txt")))
        comando2 = "ipconfig /all"
        comando1 = "systeminfo"
        comando3 = "wmic product get name, version"
        comando4 = "ipconfig /displaydns"
        if nombrearch!='':
            comando1r = ""
            comando2r = ""
            comando3r = ""
            comando4r = ""
            if (ie==1 or ir==1):
                mb.showwarning("ADVERTENCIA", "El programa no responderá por unos instantes, por favor no cierre ninguna venta durante el proceso.")
            if (ie==1):
                comando1r = "INFORMACIÓN GENERAL DEL ORDENADOR:{0}\n\n\n\n\n\n".format(check_output(comando1, shell=True))
                comando1r = comando1r.replace("\\n", "\n").replace("\\r", "").replace("b'", "").replace("\\xa0", "á").replace("\\xa1", "í").replace("\\xa2", "ó").replace("\\xa4", "ñ")
            if (ir==1):
                comando2r = "INFORMACIÓN DEL ADAPTADOR DE RED:{0}\n\n\n\n\n\n".format(check_output(comando2, shell=True))
                comando2r = comando2r.replace("\\n", "\n").replace("\\r", "").replace("b'", "").replace("\\xa0", "á").replace("\\xa1", "í").replace("\\xa2", "ó").replace("\\xa4", "ñ")
            if (pe==1):
                comando3r = "INFORMACIÓN DE LOS PROGRAMAS INSTALADOS:\n{0}\n\n\n\n\n\n".format(check_output(comando3, shell=True))
                comando3r = comando3r.replace("\\n", "\n").replace("\\r", "").replace("b'", "").replace("\\xa0", "á").replace("\\xa1", "í").replace("\\xa2", "ó").replace("\\xa4", "ñ")
            if (hr==1):
                comando4r = "INFORMACIÓN DEL HISTORIAL DE RED:{0}\n\n\n\n\n\n".format(check_output(comando4, shell=True))
                comando4r = comando4r.replace("\\n", "\n").replace("\\r", "").replace("b'", "").replace("\\xa0", "á").replace("\\xa1", "í").replace("\\xa2", "ó").replace("\\xa4", "ñ")
            proceso = "{0}".format("{0}{1}{2}{3}".format(comando1r, comando2r, comando3r, comando4r))
            final = ''
            if (nombrearch.endswith(".lhf")):
                values = []
                for char in proceso:
                    values.append("{0} ".format(math.floor(ord(char)*2)))
                for x in values:
                    final += "{0}".format(x)
            else:
                final = proceso
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(final)
            archi1.close()
            mb.showinfo("Información", "El nuevo archivo ha sido creado con éxito.")
    else:
        mb.showerror("Error", "No ha seleccionado ningún dato, no se puede crear un archivo vacío.")

def guardar():
    nombrearch=fd.asksaveasfilename(initialdir = "/", defaultextension=".lhf", title = "Guardar como",filetypes = (("Archivo de registro","*.dhf"),("Archivos de texto","*.txt")))
    if nombrearch!='':
        archi1=open(nombrearch, "w", encoding="utf-8")
        archi1.write(scrolledtext1.get("1.0", tk.END))
        archi1.close()
        mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

def recuperar():
    nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("Archivos de registro protegido","*.lhf"),("Archivos de registro","*.dhf")))
    if nombrearch!='':
        archi1=open(nombrearch, "r", encoding="utf-8")
        contenido=archi1.read()
        if (nombrearch.endswith(".lhf")):
            scrolledtext1.delete("1.0", tk.END)
            scrolledtext1.insert("1.0", "Desencriptando...")
            values = contenido.split(" ")
            y = 0
            for x in values:
                if(x != " ") and (x!=""):
                    values[y] = (chr(math.floor(int(x)/2)))
                    y += 1
            contenido = ''
            for x in values:
                contenido += "{0}".format(x)
        archi1.close()
        scrolledtext1.delete("1.0", tk.END)
        scrolledtext1.insert("1.0", contenido)

opciones1 = tk.Menu(menubar, tearoff=0)
opciones1.add_command(label="Guardar cambios", command=guardar)
opciones1.add_command(label="Recuperar archivo", command=recuperar)
opciones1.add_separator()
opciones1.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Archivo", menu=opciones1)

opciones2 = tk.Menu(menubar, tearoff=0)
opciones2.add_command(label="Nuevo archivo", command=nuevo)
opciones2.add_separator()
opciones2.add_checkbutton(label="Incluír información del equipo", variable=iev)
opciones2.add_checkbutton(label="Incluír información de red", variable=irv)
opciones2.add_checkbutton(label="Incluír historial de red", variable=hrv)
opciones2.add_checkbutton(label="Incluír programas del equipo", variable=pev)
menubar.add_cascade(label="Nuevo", menu=opciones2)  

opciones3 = tk.Menu(menubar, tearoff=0)
opciones3.add_command(label="Información", command=info, state="disabled")
opciones3.add_command(label="Debug", command=debug, state="disabled")
opciones3.add_separator()
opciones3.add_command(label="Ayuda", command=ayuda, state="disabled")
menubar.add_cascade(label="Ayuda", menu=opciones3)  
scrolledtext1=st.ScrolledText(ventana1, width=120, height=40)
scrolledtext1.grid(column=0,row=0, padx=15, pady=15)
ventana1.mainloop()

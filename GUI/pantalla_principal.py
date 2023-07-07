from tkinter import *
color = 'royal blue'
altura = 3
anchura = 30

class Interfaz(Frame):
    def __init__(self, ventana):
        super().__init__()
        # Inicializar la ventana con un título y colocar un frame donde almacenar los widgets
        self.ventana = ventana
        self.ventana.title("Proyecto III")
        self.frame = Frame(self.ventana, bg=color)
        self.frame.pack(side=TOP, fill=BOTH, expand=True)


        boton1 = Button(self.frame,text ="Borrar BBDD",height=altura,width=anchura)
        boton1.grid(sticky="NSWE",row=0,column=0,padx=(5, 5),pady=(5,0))
        boton2 = Button(self.frame, text="Carga Básica",height=altura,width=anchura)
        boton2.grid(sticky="NSWE",row=0, column=1,padx=(5, 5),pady=(5,0))
        boton3 = Button(self.frame, text="Ver número mensajes",height=altura,width=anchura)
        boton3.grid(sticky="NSWE",row=0, column=2,padx=(5, 10),pady=(5,0))

        self.label1 = Label(self.frame,text="Escriba el nombre de un juego y se buscará los cometarios en Metacritic",
                       height=2, font=("Helvetica", 15), bg=color)
        self.label1.grid(sticky="NSWE", row=1, column=0, columnspan=3, padx=(0, 5))

        self.campo1 = Text(self.frame,height=1,font=("Helvetica", 15),width =anchura*2)
        self.campo1.grid(sticky="NSWE", row=2, column=0, columnspan=2, padx=(10, 5),pady=(5,0))
        boton_busqueda1 = Button(self.frame,text="Buscar",height=3,width=anchura)
        boton_busqueda1.grid(sticky="NSWE",row=2, column=2,padx=(5, 5),pady=(5,0))

        self.label1 = Label(self.frame, text="Escriba un rango de fechas y una palabra, se buscará los comentarios relacionados en esa franja",
                            height=2, font=("Helvetica", 15), bg=color)
        self.label1.grid(sticky="NSWE", row=3, column=0, columnspan=3, padx=(0, 5))
ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
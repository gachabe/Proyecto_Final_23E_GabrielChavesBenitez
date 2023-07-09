from tkinter import *
from tkinter.ttk import Combobox
from GUI import mis_funciones as f

color = 'royal blue'
altura = 3
anchura =21
anchura2 = 1
cte= 100000
class Interfaz(Frame):
    def __init__(self, ventana,conexion):
        super().__init__()
        # Inicializar la ventana con un título y colocar un frame donde almacenar los widgets
        self.ventana = ventana
        self.ventana.title("Proyecto III")
        self.frame = Frame(self.ventana, bg=color)
        self.frame.pack(side=TOP, fill=BOTH, expand=True)
        self.conexion = conexion



        boton1 = Button(self.frame,text ="Borrar BBDD",height=altura,width=anchura,
                        command=lambda :f.borrar_datos(self.conexion))
        boton1.grid(sticky="NSWE",row=0,column=0,columnspan=3,padx=(5, 5),pady=(5,0))

        boton2 = Button(self.frame, text="Carga Básica",height=altura,width=anchura,
                        command=lambda: f.carga_inicial((self.conexion)))
        boton2.grid(sticky="NSWE",row=0, column=3,columnspan=3, padx=(5, 5),pady=(5,0))

        boton3 = Button(self.frame, text="Ver número mensajes",height=altura,width=anchura)
        boton3.grid(sticky="NSWE",row=0, column=6,columnspan=3,padx=(5, 5),pady=(5,0))

        self.label1 = Label(self.frame,text="Escriba el nombre de un juego \n se buscará los cometarios en Metacritic",
                       height=2, font=("Helvetica", 15), bg=color)
        self.label1.grid(sticky="NSWE", row=1, column=0, columnspan=9, padx=(0, 5))

        self.campo1 = Text(self.frame,height=1,font=("Helvetica", 15),width =anchura*2-cte)
        self.campo1.grid(sticky="NSWE", row=2, column=0, columnspan=6, padx=(10, 5),pady=(5,0))
        self.boton_busqueda1 = Button(self.frame,text="Buscar",height=1,width=anchura)
        self.boton_busqueda1.grid(sticky="NSWE",row=2, column=6,columnspan=3,padx=(5, 5),pady=(5,0))

        self.label2 = Label(self.frame, text="Escriba dos fechas y una palabra\n"
                                             " se buscará los comentarios relacionados en esa franja",
                            height=2, font=("Helvetica", 15), bg=color)
        self.label2.grid(sticky="NWE", row=3, column=0, columnspan=9, padx=(5, 10))

        self.combo_dia1 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1,32)],width=anchura2 )
        self.combo_dia1.grid(sticky="NWE",row=4,column=0,padx=(10, 0),pady=(5,5))

        self.combo_mes1 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1,13)],width=anchura2)
        self.combo_mes1.grid(sticky="NWE", row=4, column=1, padx=(0, 0), pady=(5, 5))

        self.combo_year1 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(2000, 2026)],width=anchura2)
        self.combo_year1.grid(sticky="NWE", row=4, column=2, padx=(0, 5), pady=(5, 5))

        self.combo_dia2 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1, 32)], width=anchura2)
        self.combo_dia2.grid(sticky="NWE", row=4, column=3, padx=(5, 0), pady=(5, 5))

        self.combo_mes2 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1, 13)], width=anchura2)
        self.combo_mes2.grid(sticky="NWE", row=4, column=4, padx=(0, 0), pady=(5, 5))

        self.combo_year2 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(2000, 2026)], width=anchura2)
        self.combo_year2.grid(sticky="NWE", row=4, column=5, padx=(0, 5), pady=(5, 5))


        self.campo2 = Text(self.frame, height=1, font=("Helvetica", 15), width=anchura * 2-cte)
        self.campo2.grid(sticky="NSWE", row=5, column=0, columnspan=6, padx=(10, 5), pady=(5, 0))
        self.boton_busqueda2 = Button(self.frame, text="Buscar", height=1, width=anchura)
        self.boton_busqueda2.grid(sticky="NSWE", row=5 ,column=6, columnspan=3, padx=(5, 5), pady=(5, 0))

        self.label3 = Label(self.frame, text="Escriba palabras relacionadas con un tema\n"
                                             " se buscará la red social más interesada en ese tema",
                            height=2, font=("Helvetica", 15), bg=color)
        self.label3.grid(sticky="NWE", row=6, column=0, columnspan=9, padx=(5, 10))
        self.campo3 = Text(self.frame, height=1, font=("Helvetica", 15), width=anchura * 2 - cte)
        self.campo3.grid(sticky="NSWE", row=7, column=0, columnspan=6, padx=(10, 5), pady=(5, 5))
        self.boton_busqueda3 = Button(self.frame, text="Buscar", height=1, width=anchura)
        self.boton_busqueda3.grid(sticky="NSWE", row=7, column=6, columnspan=3, padx=(5, 5), pady=(5, 5))



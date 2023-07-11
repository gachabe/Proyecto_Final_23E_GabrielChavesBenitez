from tkinter import Button, Text, Label, Frame, CENTER, Toplevel
from tkinter.ttk import Combobox
from GUI import mis_funciones as f
from pandastable import Table
from obtener_datos import consultar_datos as consulta
from procesar_mensajes import procesar_mensajes_metacritic as meta

color = 'royal blue'
altura = 3
anchura =21
anchura2 = 1
cte= 0
class Interfaz(Frame):
    def __init__(self, ventana,conexion):
        super().__init__()
        # Inicializar la ventana con un título y colocar un frame donde almacenar los widgets
        self.ventana = ventana
        self.ventana.title("Proyecto III")
        self.ventana.configure(bg=color)
        self.frame = Frame(self.ventana, bg=color)
        self.frame.pack(anchor=CENTER, expand=True)
        self.conexion = conexion



        boton1 = Button(self.frame,text ="Borrar BBDD",height=altura,width=anchura,
                        command=lambda :f.borrar_datos(self.conexion))
        boton1.grid(sticky="NSWE",row=0,column=0,columnspan=3,padx=(5, 5),pady=(5,0))

        boton2 = Button(self.frame, text="Carga Básica",height=altura,width=anchura,
                        command=lambda: f.carga_inicial((self.conexion)))
        boton2.grid(sticky="NSWE",row=0, column=3,columnspan=3, padx=(5, 5),pady=(5,0))

        boton3 = Button(self.frame, text="Ver número mensajes",height=altura,width=anchura,
                        command =lambda: self.mostrar_tabla_usuarios())
        boton3.grid(sticky="NSWE",row=0, column=6,columnspan=3,padx=(5, 5),pady=(5,0))

        self.label1 = Label(self.frame,text="Escriba el nombre de un juego y la plataforma separada por coma"
                                            " \n se buscará los comentarios en Metacritic",
                       height=2, font=("Helvetica", 15), bg=color)
        self.label1.grid(sticky="NSWE", row=1, column=0, columnspan=9, padx=(0, 5))

        self.campo1 = Text(self.frame,height=1,font=("Helvetica", 15),width =anchura*2-cte)
        self.campo1.grid(sticky="NSWE", row=2, column=0, columnspan=6, padx=(10, 5),pady=(5,0))
        self.boton_busqueda1 = Button(self.frame,text="Buscar",height=1,width=anchura,
                                command=lambda : self.cargar_juego_meta(conexion))
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
        self.boton_busqueda2 = Button(self.frame, text="Buscar", height=1, width=anchura,
                                      command= lambda : self.buscar_comentarios_fecha(self.conexion))
        self.boton_busqueda2.grid(sticky="NSWE", row=5 ,column=6, columnspan=3, padx=(5, 5), pady=(5, 0))

        self.label3 = Label(self.frame, text="Escriba palabras relacionadas con un tema\n"
                                             " se buscará la red social más interesada en ese tema",
                            height=2, font=("Helvetica", 15), bg=color)
        self.label3.grid(sticky="NWE", row=6, column=0, columnspan=9, padx=(5, 10))
        self.campo3 = Text(self.frame, height=1, font=("Helvetica", 15), width=anchura * 2 - cte)
        self.campo3.grid(sticky="NSWE", row=7, column=0, columnspan=6, padx=(10, 5), pady=(5, 5))
        self.boton_busqueda3 = Button(self.frame, text="Buscar", height=1, width=anchura,
                                      command=lambda :self.buscar_tema_red_social(conexion))
        self.boton_busqueda3.grid(sticky="NSWE", row=7, column=6, columnspan=3, padx=(5, 5), pady=(5, 5))

        self.label4 = Label(self.frame, text="Elija un rango de fechas \n "\
                                             "se mostrará la media de mensajes por red social",
                            height=2, font=("Helvetica", 15), bg=color
                            )
        self.label4.grid(sticky="NWE", row=8, column=0, columnspan=9, padx=(5, 10))
        self.combo_dia3 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1, 32)], width=anchura2)
        self.combo_dia3.grid(sticky="NWE", row=9, column=0, padx=(10, 0), pady=(5, 5))

        self.combo_mes3 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1, 13)], width=anchura2)
        self.combo_mes3.grid(sticky="NWE", row=9, column=1, padx=(0, 0), pady=(5, 5))

        self.combo_year3 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(2000, 2026)],
                                    width=anchura2)
        self.combo_year3.grid(sticky="NWE", row=9, column=2, padx=(0, 5), pady=(5, 5))

        self.combo_dia4 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1, 32)], width=anchura2)
        self.combo_dia4.grid(sticky="NWE", row=9, column=3, padx=(5, 0), pady=(5, 5))

        self.combo_mes4 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(1, 13)], width=anchura2)
        self.combo_mes4.grid(sticky="NWE", row=9, column=4, padx=(0, 0), pady=(5, 5))

        self.combo_year4 = Combobox(self.frame, state="readonly", values=[str(i) for i in range(2000, 2026)],
                                    width=anchura2)
        self.combo_year4.grid(sticky="NWE", row=9, column=5, padx=(0, 5), pady=(5, 5))

        self.boton_busqueda4 = Button(self.frame, text="Buscar", height=1, width=anchura,
                                     command=lambda: self.buscar_comentarios_red_social_media(self.conexion))
        self.boton_busqueda4.grid(sticky="NSWE", row=9, column=6, columnspan=3, padx=(5, 5), pady=(5, 5))

    def mostrar_tabla_usuarios(self):
        df = consulta.consultar_comentarios_cantidad(self.conexion)
        newWindow = Toplevel()
        newWindow.title("Nueva ventana")
        newWindow.geometry("800x800")

        self.table = Table(newWindow, dataframe=df, showtoolbar=True, showstatusbar=True)
        self.table.show()
        return
    def cargar_juego_meta(self,conexion):
        if self.campo1.get("1.0","end-1c") == "":
            newWindow = Toplevel()
            newWindow.title("ERROR")
            newWindow.geometry("300x100")
            mensaje = Label(newWindow, text= "Escribe al menos un juego y una plataforma",font=("Helvetica", 10))
            mensaje.pack(anchor=CENTER, expand=True)


        else:
            juego = self.campo1.get("1.0", "end-1c").split(",")[0]  # Al ser un tipo Text añade un espacio al final
            plataforma = self.campo1.get("1.0", "end-1c").split(",")[1].lstrip()
            try:
                print(juego)
                print(plataforma)
                meta.cargar_comentario_metacritic(conexion,juego,plataforma)


            except Exception as e:
                print("Hubo un error imprevisto:", str(e))

    def buscar_comentarios_fecha(self,conexion):

        dia1 = self.combo_dia1.get()
        mes1 = self.combo_mes1.get()
        mes1 = "0"+mes1 if len(mes1) ==1 else mes1
        year1 = self.combo_year1.get()
        fecha1 = f"{year1}-{mes1}-{dia1}"

        dia2 = self.combo_dia2.get()
        mes2 = self.combo_mes2.get()
        mes2 = "0" + mes2 if len(mes2) == 1 else mes2
        year2 = self.combo_year2.get()
        fecha2 = f"{year2}-{mes2}-{dia2}"

        palabra_clave = self.campo2.get("1.0","end-1c")
        print(f"{palabra_clave},{fecha1},{fecha2}")

        df = consulta.consultar_comentarios_fecha(conexion,palabra_clave,fecha1,fecha2)

        newWindow = Toplevel()
        newWindow.title("Usuario")
        newWindow.geometry("800x800")

        self.table = Table(newWindow, dataframe=df, showtoolbar=True, showstatusbar=True)
        self.table.show()


    def buscar_tema_red_social(self,conexion):
        if self.campo3.get('1.0',"end-1c") == "":
            newWindow = Toplevel()
            newWindow.title("ERROR")
            newWindow.geometry("300x100")
            mensaje = Label(newWindow, text="Escribe al menos una palabra", font=("Helvetica", 10))
            mensaje.pack(anchor=CENTER, expand=True)
        else:
            try:
                palabras = self.campo3.get('1.0',"end-1c").split(",")
                palabras = [palabra.lstrip() for palabra in palabras]
                palabras = tuple(palabras)
                print(palabras)
                df = consulta.consultar_tema_red_social(conexion,palabras)
                newWindow = Toplevel()
                newWindow.title("Nueva ventana")
                newWindow.geometry("800x800")

                self.table = Table(newWindow, dataframe=df, showtoolbar=True, showstatusbar=True)
                self.table.show()
            except Exception as e:
                print("Hubo un error imprevisto:", str(e))
    def buscar_comentarios_red_social_media(self,conexion):
        dia1 = self.combo_dia3.get()
        mes1 = self.combo_mes3.get()
        mes1 = "0" + mes1 if len(mes1) == 1 else mes1
        year1 = self.combo_year3.get()
        fecha1 = f"{year1}-{mes1}-{dia1}"

        dia2 = self.combo_dia4.get()
        mes2 = self.combo_mes4.get()
        mes2 = "0" + mes2 if len(mes2) == 1 else mes2
        year2 = self.combo_year4.get()
        fecha2 = f"{year2}-{mes2}-{dia2}"
        consulta.consultar_comentarios_red_social_media(conexion,fecha1,fecha2)



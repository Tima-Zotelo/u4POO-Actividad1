from tkinter import *
from tkinter import ttk, messagebox
from functools import partial


class Calculadora:
    __ventana: None
    __ipc: None

    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.geometry('535x209')
        self.__ventana.title ('Calculadora IPC')
        #self.__ventana.resizable(0,0)  
        opts = { 'padx': 5, 'pady': 5 , 'sticky': 'nswe' }
        self.itemLbl = ttk.Label (self.__ventana, text='Item')
        self.cantidadLbl = ttk.Label (self.__ventana, text='Cantidad')
        self.precioAnhoBase = ttk.Label (self.__ventana, text='Precio Año Base')
        self.precioAnhoActual = ttk.Label (self.__ventana, text='Precio Año Actual')

        self.vestimentaLbl = ttk.Label (self.__ventana, text='Vestimenta')
        self.vestimenta1 = StringVar()
        self.vestimenta2 = StringVar()
        self.vestimenta3 = StringVar()
        self.vestimentaEntry1 = ttk.Entry (self.__ventana, textvariable=self.vestimenta1)
        self.vestimentaEntry2 = ttk.Entry (self.__ventana, textvariable=self.vestimenta2)
        self.vestimentaEntry3 = ttk.Entry (self.__ventana, textvariable=self.vestimenta3)

        self.alimentosLbl = ttk.Label (self.__ventana, text='Alimentos')
        self.alimentos1 = StringVar()
        self.alimentos2 = StringVar()
        self.alimentos3 = StringVar()
        self.alimentosEntry1 = ttk.Entry (self.__ventana, textvariable=self.alimentos1)
        self.alimentosEntry2 = ttk.Entry (self.__ventana, textvariable=self.alimentos2)
        self.alimentosEntry3 = ttk.Entry (self.__ventana, textvariable=self.alimentos3)

        self.educacionLbl = ttk.Label (self.__ventana, text='Educacion')
        self.educacion1 = StringVar()
        self.educacion2 = StringVar()
        self.educacion3 = StringVar()
        self.educacionEntry1 = ttk.Entry (self.__ventana, textvariable=self.educacion1)
        self.educacionEntry2 = ttk.Entry (self.__ventana, textvariable=self.educacion2)
        self.educacionEntry3 = ttk.Entry (self.__ventana, textvariable=self.educacion3)

        self.botonCalcular = ttk.Button (self.__ventana, text='Calcular IPC', command=self.calcular)
        self.botonSalir = ttk.Button (self.__ventana, text='Salir', command=self.__ventana.destroy)
        self.ipcLbl = ttk.Label (self.__ventana, text=f'IPC % {self.__ipc}%')
        ### Grill ###

        # Fila uno
        self.itemLbl.grid (row=0, column=0, **opts)
        self.cantidadLbl.grid (row=0, column=1, **opts)
        self.precioAnhoBase.grid (row=0, column=2, **opts)
        self.precioAnhoActual.grid (row=0, column=3, **opts)

        # Fila dos
        self.vestimentaLbl.grid (row=1, column=0, **opts)
        self.vestimentaEntry1.grid (row=1, column=1, **opts)
        self.vestimentaEntry2.grid (row=1, column=2, **opts)
        self.vestimentaEntry3.grid (row=1, column=3, **opts)

        # Fila tres
        self.alimentosLbl.grid (row=2, column=0, **opts)
        self.alimentosEntry1.grid (row=2, column=1, **opts)
        self.alimentosEntry2.grid (row=2, column=2, **opts)
        self.alimentosEntry3.grid (row=2, column=3, **opts)

        # FIla cuatro
        self.educacionLbl.grid (row=3, column=0, **opts)
        self.educacionEntry1.grid (row=3, column=1, **opts)
        self.educacionEntry2.grid (row=3, column=2, **opts)
        self.educacionEntry3.grid (row=3, column=3, **opts)

        self.botonCalcular.grid (row=4, column=2, **opts)
        self.botonSalir.grid (row=4, column=3, **opts)
        self.ipcLbl.grid (row=5, column=0, **opts)

        self.botonCalcular.focus()
        self.__ventana.mainloop()

    def calcular (self):
        try: 
            vestimentaCant = float(self.vestimentaEntry1.get())
            vestimentaPBase = float(self.vestimentaEntry2.get())
            vestimentaPActual = float(self.vestimentaEntry3.get())
            
            alimentosCant = float(self.alimentosEntry1.get())
            alimentosPBase = float(self.alimentosEntry2.get())
            alimentosPActual = float(self.alimentosEntry3.get())
            
            educacionCant = float(self.educacionEntry1.get())
            educacionPBase = float(self.educacionEntry2.get())
            educacionPActual = float(self.educacionEntry3.get())

            ipcVest = (vestimentaCant * vestimentaPBase) / (alimentosCant * vestimentaPActual)
            ipcAlim = (alimentosCant * alimentosPBase) / (alimentosCant * alimentosPActual)
            ipcEdu = (educacionCant * educacionPBase) / (educacionCant * educacionPActual)

            ipc = (ipcAlim + ipcEdu + ipcVest) / 3
            self.ipcLbl['text'] = f"IPC % {ipc:.2f}%"

        except ValueError:
            messagebox.showerror(title='Error de tipó', message='Debe ingresar un valor válido')
            self.vestimenta1.set('')
            self.vestimenta2.set(2022)
            self.vestimenta3.set(2023)
            self.alimentos1.set('')
            self.alimentos2.set(2022)
            self.alimentos3.set(2023)
            self.educacion1.set('')
            self.educacion2.set(2022)
            self.educacion3.set(2023)


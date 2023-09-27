
#PASO1
import customtkinter 
from tkinter import *
from tkinter import messagebox

#PASO3
class Calculator:
    def __init__(self):
        #Para crear la ventana.
        #Ajustar la fuente de la letra
        self.app = customtkinter.CTk()
        self.app.title("Calculadora")
        self.app.geometry("250x350")
        self.app.config(bg="#000000")
        #PASO4
        self.equation = ""
        self.i = 0
        self.letra1 = ('Arial', 20, 'bold')
        self.create_widgets() #PASO5
    
    #PASO5
    def create_widgets(self):
        #Para crear la cajita de resultados
        #(La ventana donde queremos la nueva cajita,lo que queremos que este escrito, 
        #la fuente, tamaño, colorbg,borde)
        self.result_entry = customtkinter.CTkEntry(
            self.app,
            textvariable="",
            font=self.letra1,
            width=250,
            fg_color="#FFFFFF",
            border_color="#FFFFFF"
        )
        #posicionar la cajita
        self.result_entry.place(x=0,y=10)

        #PASO6
        #Crear los botones 
        #botones de las operaciones
        #Haciendo esto quiero que cuando se clickee uno limpie todo 
        self.Button1 = customtkinter.CTkButton(
            self.app,
            command=self.clear,
            text="C",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#83838B",
            hover_color="#83838B"
        )
        self.Button1.place(x=10,y=60)
        
        self.Button0 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("√"),
            text="√",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#83838B",
            hover_color="#83838B"
        )
        self.Button0.place(x=130,y=60)


        self.Button2 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("%"),
            text="%",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#83838B",
            hover_color="#83838B"
        )
        self.Button2.place(x=70,y=60)

        self.Button3 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("/"),
            text="/",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#b5520b",
            hover_color="#b5520b"
        )
        self.Button3.place(x=190,y=240)

        self.Button4 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("*"),
            text="x",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#b5520b",
            hover_color="#b5520b"
        )
        self.Button4.place(x=190,y=60)

        self.Button5 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("-"),
            text="-",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#b5520b",
            hover_color="#b5520b"
        )
        self.Button5.place(x=190,y=180)

        self.Button6 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("+"),
            text="+",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#b5520b",
            hover_color="#b5520b"
        )
        self.Button6.place(x=190,y=120)

        self.Button7 = customtkinter.CTkButton(
            self.app,
            command=self.calculate,
            text="=",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#b5520b",
            hover_color="#b5520b"
        )
        self.Button7.place(x=190,y=300)

        self.Button8 = customtkinter.CTkButton(
            self.app,
            command=lambda: self.show("."),
            text=".",
            font=self.letra1,
            width=50,
            height=2,
            fg_color="#b5520b",
            hover_color="#b5520b"
        )
        self.Button8.place(x=130,y=300)

        #PASO6.2
        #Botones numeros
        self.Button9 = customtkinter.CTkButton(
        self.app,
        command=lambda:self.show("1"),
        text="1",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button9.place(x=10,y=240)

        self.Button10 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("2"),
        text="2",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button10.place(x=70,y=240)
        
        self.Button11 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("3"),
        text="3",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button11.place(x=130,y=240)
        
        self.Button12 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("4"),
        text="4",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button12.place(x=10,y=180)
        
        self.Button13 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("5"),
        text="5",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button13.place(x=70,y=180)
        
        self.Button14 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("6"),
        text="6",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button14.place(x=130,y=180)

        self.Button15 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("7"),
        text="7",
        font=self.letra1,
        width=50,
        height=2,
       fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button15.place(x=10,y=120)
        
        self.Button16 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("8"),
        text="8",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button16.place(x=70,y=120)

        self.Button17 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("9"),
        text="9",
        font=self.letra1,
        width=50,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button17.place(x=130,y=120)
        
        self.Button18 = customtkinter.CTkButton(
        self.app,
        command=lambda: self.show("0"),
        text="0",
        font=self.letra1,
        width=110,
        height=2,
        fg_color="#2e2a27",
        hover_color="#2e2a27"
        )
        self.Button18.place(x=10,y=300)

    #PASO7.1
    def show(self, value):
        if(value=="%"):
            value="/100"
        elif(value=="√"):
            value="**0.5"
        self.equation+=value
        self.result_entry.insert(self.i,value)
        self.i=self.i+1#añado el nuevo valor a el nuevo indice
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, self.equation)

    #PASO7.2
    def clear(self):
        self.equation = ""
        self.result_entry.delete(0, END)

    #PASO7.3
    def calculate(self):
        try:
            self.result = eval(self.equation)
            self.equation = str(self.result)
            self.result_entry.delete(0, END)
            self.result_entry.insert(0, self.result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")
            self.equation = ""
            self.equation = str(self.result)
        except:
            messagebox.showerror(title="Error", message="Operación inválida")


    
        
        
#PASO2
    def mainloop(self):
        self.app.mainloop()

if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()

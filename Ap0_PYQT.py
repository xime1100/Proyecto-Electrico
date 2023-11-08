import sys  # Agrega esta línea para importar el módulo 'sys'
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox)


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar()

    def inicializar(self):
        self.setWindowTitle("Calculadora")
        self.setGeometry(0, 0, 250, 350)
        self.setStyleSheet("background-color: black;")
        self.equation = ""
        self.i = 0
        self.create_widgets()
        self.show()

    def create_widgets(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
        self.pantalla.setFixedHeight(40)
        self.pantalla.setStyleSheet("background-color: white; color: black; font-size: 16px;")

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla, 0, 0, 1, 4)  # Pantalla en la fila 0, ocupando 4 columnas

        botones = [
            "C", "%", "√", "x",
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "/",
            "0", ".", "="
        ]

        row = 1
        col = 0

        for texto in botones:
            boton = QPushButton(texto)

            if texto in ["C", "%", "√"]:
                # Cambia el color de fondo y el color de texto para "C", "%", y "√"
                boton.setStyleSheet("background-color: #83838B; border:1px solid #000; font-size:20px; border-radius:8px; color: #fff;")
                if texto == "C":
                    boton.clicked.connect(self.boton_limpiar)
                elif texto == "%":
                    boton.clicked.connect(lambda: self.boton_especial_presionado("%"))
                elif texto == "√":
                    boton.clicked.connect(lambda: self.boton_especial_presionado("√"))

            if texto in ["x", "+", "-", ".", "/"]:
                boton.setStyleSheet("background-color: #b5520b; border:1px solid #000; font-size:20px; border-radius:8px; color: #fff;")
                boton.clicked.connect(self.boton_operador_presionado)
            
            if texto in ["="]:
                boton.setStyleSheet("background-color: #b5520b; border:1px solid #000; font-size:20px; border-radius:8px; color: #fff;")
                boton.clicked.connect(self.calcular_resultado)

            if texto in ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]:
                boton.setStyleSheet("background-color: #2e2a27; border:1px solid #000; font-size:20px; border-radius:8px; color: #fff;")
                boton.clicked.connect(self.boton_numerico_presionado)



            if texto == "0":
                self.main_grid.addWidget(boton, row, col,1,2)
            else:
                self.main_grid.addWidget(boton,row,col,1,1)

            col += 2 if texto == "0" else 1

            if col > 3:
                col = 0
                row += 1

        self.setLayout(self.main_grid)
    
    def boton_especial_presionado(self, value):
        if value == "%":
            value = "/100"
        elif value == "√":
            value = "**0.5"

        self.equation += value
        self.pantalla.insertPlainText(value)

    def boton_numerico_presionado(self):
        sender = self.sender()
        texto = sender.text()
        self.equation += texto
        self.pantalla.insertPlainText(texto)


    def boton_operador_presionado(self):
        sender = self.sender()
        texto = sender.text()
        self.equation += texto
        self.pantalla.insertPlainText(texto)

    def boton_limpiar(self):
        self.equation = ""
        self.pantalla.clear()
    
    def calcular_resultado(self):

        self.equation = self.equation.replace("x","*")

        try:
            self.result = eval(self.equation)
            self.equation = str(self.result)
            self.pantalla.clear()
            self.pantalla.insertPlainText(self.equation)
        except ZeroDivisionError:
            QMessageBox.critical(self, "Error", "No se puede dividir entre cero")
            self.equation = ""
            self.pantalla.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error", "Operación inválida: " + str(e))
            self.equation = ""
            self.pantalla.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec())


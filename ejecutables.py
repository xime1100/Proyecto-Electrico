import os
import tkinter as tk
from tkinter import filedialog
import subprocess
from tkinter import messagebox

class PyInstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejecutables")

        self.script_path_label = tk.Label(self.root, text="Seleciona un archivo:")
        self.script_path_label.pack()

        self.script_path_entry = tk.Entry(self.root, width=40)
        self.script_path_entry.pack()

        self.browse_button = tk.Button(self.root, text="Seleccionar", command=self.browse_script)
        self.browse_button.pack()

        self.convert_button = tk.Button(self.root, text="Instalar", command=self.convert_script)
        self.convert_button.pack()

    def browse_script(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        self.script_path_entry.delete(0, tk.END)
        self.script_path_entry.insert(0, file_path)

    def convert_script(self):
        script_path = self.script_path_entry.get()
        if script_path:
            self.show_message("Instalando", "Pulsa ok!")

            # Determine the command to run based on the operating system
            if os.name == 'posix':  # Unix-like systems (Linux, macOS)
                command = ["pyinstaller", "--onefile", "--windowed", script_path]
            else:  # Windows
                command = ["pyinstaller", "--onefile", "--windowed", script_path]

            subprocess.run(command)

            self.show_message("Instalacion completa!", "Pulsa ok!")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PyInstallerGUI(root)
    root.mainloop()






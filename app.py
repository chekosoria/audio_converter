"""Aplicación para convertir archivos de audio a MP3"""
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pydub import AudioSegment


class AudioConverterApp:
    """Clase principal"""

    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converter")

        self.label = tk.Label(root, text="Selecciona un archivo de audio:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(
            root, text="Seleccionar archivo", command=self.select_file)
        self.select_button.pack(pady=5)

        self.name_label = tk.Label(root, text="Nombre del archivo de salida:")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.convert_button = tk.Button(
            root, text="Convertir a MP3", command=self.convert_to_mp3)
        self.convert_button.pack(pady=20)

        self.file_path = None

    def select_file(self):
        """Método para seleccionar archivos"""
        filetypes = (
            ("Audio files", "*.opus *.aac *.wav *.mp3"),
            ("All files", "*.*")
        )
        self.file_path = filedialog.askopenfilename(
            title="Seleccionar archivo", filetypes=filetypes)
        if self.file_path:
            messagebox.showinfo("Archivo seleccionado",
                                f"Archivo seleccionado: {self.file_path}")

    def convert_to_mp3(self):
        """Método para convertir a MP3"""
        if not self.file_path:
            messagebox.showwarning(
                "Advertencia", "Por favor, selecciona un archivo primero.")
            return

        output_name = self.name_entry.get()
        if not output_name:
            messagebox.showwarning(
                "Advertencia", "Por favor, ingresa un nombre para el archivo de salida.")
            return

        output_dir = "Convertidos"
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{output_name}.mp3")

        try:
            audio = AudioSegment.from_file(self.file_path)
            audio.export(output_path, format="mp3")
            messagebox.showinfo(
                "Éxito", f"Archivo convertido y guardado en: {output_path}")
        except Exception as e:
            messagebox.showerror(
                "Error", f"Error al convertir el archivo: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioConverterApp(root)
    root.mainloop()

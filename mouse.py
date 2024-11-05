import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui

# Variable global para controlar el proceso
running = False

# Función para el proceso de ejemplo con movimiento del mouse
def background_process():
    while running:
        pyautogui.move(100, 0)
        pyautogui.move(0, 100)
        pyautogui.move(-100, 0)
        pyautogui.move(0, -100)
        time.sleep(3)

# Función para iniciar el proceso
def start_process():
    global running
    if not running:
        running = True
        thread = threading.Thread(target=background_process)
        thread.daemon = True
        thread.start()
        messagebox.showinfo("Proceso", "El proceso ha iniciado y el mouse se moverá cada 3 segundos")
    else:
        messagebox.showwarning("Proceso", "El proceso ya está corriendo")

# Función para detener el proceso
def stop_process():
    global running
    if running:
        running = False
        messagebox.showinfo("Proceso", "El proceso ha sido detenido")
    else:
        messagebox.showwarning("Proceso", "El proceso ya está detenido")

# Función para cerrar la ventana y terminar el programa
def close_window():
    global running
    running = False
    root.destroy()

# Configuración de la interfaz
root = tk.Tk()
root.title("Control de Mouse Mover")
root.geometry("400x250")
root.configure(bg="#2c3e50")

# Estilos para los botones
button_style = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "#3498db",
    "fg": "white",
    "activebackground": "#2980b9",
    "activeforeground": "white",
    "relief": "flat",
    "bd": 0,
    "width": 20,
    "height": 2,
}

# Etiqueta de título
title_label = tk.Label(root, text="Control de Proceso", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=20)

# Botón para iniciar el proceso
start_button = tk.Button(root, text="Iniciar Mouse Mover", command=start_process, **button_style)
start_button.pack(pady=10)

# Botón para detener el proceso
stop_button = tk.Button(root, text="Pausar Mouse Mover", command=stop_process, **button_style)
stop_button.pack(pady=10)

# Botón para cerrar la ventana
close_button = tk.Button(root, text="Cerrar", command=close_window, **button_style)
close_button.pack(pady=10)

# Ejecuta la interfaz gráfica
root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()

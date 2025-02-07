import tkinter as tk
import random
from tkinter import font

# Generar número aleatorio
numero_secreto = random.randint(0, 100)

def verificar_numero():
    try:
        intento = int(entrada.get())
        if intento < numero_secreto:
            mensaje.set("🔴 El número es mayor ⬆")
        elif intento > numero_secreto:
            mensaje.set("🔵 El número es menor ⬇")
        else:
            mensaje.set("✅ ¡Felicidades! Has adivinado el número 🎉")
            boton_reiniciar.pack(pady=10)
    except ValueError:
        mensaje.set("⚠️ Ingresa un número válido")

def reiniciar_juego():
    global numero_secreto
    numero_secreto = random.randint(0, 100)
    mensaje.set("🎯 Intenta adivinar el número entre 0 y 100")
    entrada.delete(0, tk.END)
    boton_reiniciar.pack_forget()

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("🎮 Adivina el Número")
ventana.geometry("450x350")
ventana.configure(bg="#1E1E1E")

fuente_estilo = font.Font(family="Arial", size=12, weight="bold")

# Elementos de la interfaz
titulo = tk.Label(ventana, text="🔹 Adivina el Número 🔹", fg="#00FF00", bg="#1E1E1E", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

tk.Label(ventana, text="Introduce un número del 0 al 100:", fg="white", bg="#1E1E1E", font=fuente_estilo).pack()

entrada = tk.Entry(ventana, font=fuente_estilo, justify="center", width=10)
entrada.pack(pady=5)

boton_verificar = tk.Button(ventana, text="✔ Comprobar", command=verificar_numero, bg="#00AAFF", fg="white", font=fuente_estilo)
boton_verificar.pack(pady=5)

mensaje = tk.StringVar()
mensaje.set("🎯 Intenta adivinar el número entre 0 y 100")
etiqueta_mensaje = tk.Label(ventana, textvariable=mensaje, fg="white", bg="#1E1E1E", font=fuente_estilo)
etiqueta_mensaje.pack(pady=10)

boton_reiniciar = tk.Button(ventana, text="🔄 Reiniciar Juego", command=reiniciar_juego, bg="#FF5733", fg="white", font=fuente_estilo)

# Iniciar la ventana
ventana.mainloop()

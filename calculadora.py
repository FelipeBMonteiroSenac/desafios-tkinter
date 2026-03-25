# Author: leoamaral82hot-byte

# calculadora
import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("500x400")
# titulo
tk.Label(root, text="Calculadora", font=("Arial", 20)).pack(pady=10)
# entradas
tk.Label(root, text="Digite o primeiro valor:").pack()
entrada1 = tk.Entry(root)
entrada1.pack()

tk.Label(root, text="Digite o segundo valor:").pack()
entrada2 = tk.Entry(root)
entrada2.pack()
# resultado
resultado = tk.Label(root, text="")
resultado.pack(pady=10)


# funções
def somar():
    try:
        v1 = float(entrada1.get())
        v2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {v1 + v2}")
    except ValueError:
        resultado.config(text="Erro: digite números válidos")


def subtrair():
    try:
        v1 = float(entrada1.get())
        v2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {v1 - v2}")
    except ValueError:
        resultado.config(text="Erro: digite números válidos")


def multiplicar():
    try:
        v1 = float(entrada1.get())
        v2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {v1 * v2}")
    except ValueError:
        resultado.config(text="Erro: digite números válidos")


def dividir():
    try:
        v1 = float(entrada1.get())
        v2 = float(entrada2.get())
        if v2 == 0:
            resultado.config(text="Erro: divisão por zero")
        else:
            resultado.config(text=f"Resultado: {v1 / v2}")
    except ValueError:
        resultado.config(text="Erro: digite números válidos")


# botões
tk.Button(root, text="Somar", command=somar).pack(pady=5)
tk.Button(root, text="Subtrair", command=subtrair).pack(pady=5)
tk.Button(root, text="Multiplicar", command=multiplicar).pack(pady=5)
tk.Button(root, text="Dividir", command=dividir).pack(pady=5)

root.mainloop()

# Author: Luuuri

import tkinter as tk
import time

root = tk.Tk()
root.title("Jardim")
root.geometry("400x400")

# Sistema que gera flores em um jardim

contador_flores = 0  # Contagem inicial de flores antes de apertar o botão

"Função Mensagem Fim"


def fim():  # Mensagem final ao atingir todas as flores, depois de 2 segundos a janela se fecha
    msg_fim = tk.Message(
        root,
        text="Parabéns! 🌸\nVocê plantou 5 flores!\nSeu jardim está completo!",
        justify="center",
        font="Calibri, 14",
        relief="raised",
        fg="green",
        bg="lightgreen",
    )
    msg_fim.place(anchor="center", relx=0.5, rely=0.38, relheight=0.3, relwidth=0.45)
    msg_fim.after(3500, root.destroy)


"Função de Plantar"


def plantar():  # Gera as flores a partir da contagem de clicks
    global contador_flores
    contador_flores += 1
    if contador_flores == 1:
        flor1()
    elif contador_flores == 2:
        flor2()
    elif contador_flores == 3:
        flor3()
    elif contador_flores == 4:
        flor4()
    elif contador_flores == 5:
        flor5()
        contador_flores = 0
        fim()


"Parte Supeior"

# Céu
ceu = tk.Frame(root, bg="lightblue")
ceu.place(anchor="center", relx=0.5, rely=0.1, relheight=0.2, relwidth=1)

# Nuvens

# Nuvem 1
nuvem = tk.Frame(ceu, bg="white")
nuvem.place(anchor="center", relx=0.2, rely=0.5, relheight=0.5, relwidth=0.3)
# Nuvem 2
nuvem2 = tk.Frame(ceu, bg="white")
nuvem2.place(anchor="center", relx=0.7, rely=0.6, relheight=0.3, relwidth=0.15)

"Parte Inferior"

# Grama
grama = tk.Frame(root, bg="lightgreen")
grama.place(anchor="center", relx=0.5, rely=0.6, relheight=0.8, relwidth=1)


# Flores
def flor1():
    "graminha"
    graminha = tk.Frame(grama, bg="palegreen3")
    graminha.place(anchor="center", relx=0.5, rely=0.7, relheight=0.02, relwidth=0.06)
    "caule"
    caule = tk.Frame(grama, bg="brown")
    caule.place(anchor="center", relx=0.5, rely=0.6, relheight=0.2, relwidth=0.015)

    "flor maior"
    flor_maior = tk.Frame(root, bg="yellow")
    flor_maior.place(anchor="center", relx=0.5, rely=0.6, relheight=0.1, relwidth=0.1)
    "flor menor"
    flor_menor = tk.Frame(flor_maior, bg="orange")
    flor_menor.place(anchor="center", relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)


def flor2():
    "graminha"
    graminha = tk.Frame(grama, bg="palegreen3")
    graminha.place(anchor="center", relx=0.8, rely=0.9, relheight=0.02, relwidth=0.06)
    "caule"
    caule2 = tk.Frame(grama, bg="brown3")
    caule2.place(anchor="center", relx=0.8, rely=0.8, relheight=0.2, relwidth=0.015)
    "flor maior"
    flor_maior2 = tk.Frame(root, bg="lightpink")
    flor_maior2.place(anchor="center", relx=0.8, rely=0.75, relheight=0.1, relwidth=0.1)
    "flor menor"
    flor_menor2 = tk.Frame(flor_maior2, bg="brown1")
    flor_menor2.place(anchor="center", relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)


def flor3():
    "graminha"
    graminha = tk.Frame(grama, bg="palegreen3")
    graminha.place(anchor="center", relx=0.8, rely=0.4, relheight=0.02, relwidth=0.06)
    "caule"
    caule3 = tk.Frame(grama, bg="lightblue4")
    caule3.place(anchor="center", relx=0.8, rely=0.3, relheight=0.2, relwidth=0.015)
    "flor maior"
    flor_maior3 = tk.Frame(root, bg="lightblue")
    flor_maior3.place(anchor="center", relx=0.8, rely=0.35, relheight=0.1, relwidth=0.1)
    "flor menor"
    flor_menor3 = tk.Frame(flor_maior3, bg="white")
    flor_menor3.place(anchor="center", relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)


def flor4():
    "graminha"
    graminha = tk.Frame(grama, bg="palegreen3")
    graminha.place(anchor="center", relx=0.2, rely=0.9, relheight=0.02, relwidth=0.06)
    "caule"
    caule4 = tk.Frame(grama, bg="cyan3")
    caule4.place(anchor="center", relx=0.2, rely=0.8, relheight=0.2, relwidth=0.015)
    "flor maior"
    flor_maior4 = tk.Frame(root, bg="lightpink")
    flor_maior4.place(anchor="center", relx=0.2, rely=0.75, relheight=0.1, relwidth=0.1)
    "flor menor"
    flor_menor4 = tk.Frame(flor_maior4, bg="lightyellow")
    flor_menor4.place(anchor="center", relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)


def flor5():
    "graminha"
    graminha = tk.Frame(grama, bg="palegreen3")
    graminha.place(anchor="center", relx=0.2, rely=0.4, relheight=0.02, relwidth=0.06)
    "caule"
    caule5 = tk.Frame(grama, bg="green")
    caule5.place(anchor="center", relx=0.2, rely=0.3, relheight=0.2, relwidth=0.015)
    "flor maior"
    flor_maior5 = tk.Frame(root, bg="orange")
    flor_maior5.place(anchor="center", relx=0.2, rely=0.35, relheight=0.1, relwidth=0.1)
    "flor menor"
    flor_menor5 = tk.Frame(flor_maior5, bg="brown")
    flor_menor5.place(anchor="center", relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)


"Botão de Plantar"
botao_plantar = tk.Button(
    grama,
    text="Plante",
    bg="lightgreen",
    fg="green",
    font="Calibri, 14",
    activebackground="green",
    activeforeground="lightgreen",
    overrelief="sunken",
    relief="raised",
    command=plantar,
)
botao_plantar.place(anchor="center", relx=0.5, rely=0.2)

root.mainloop()

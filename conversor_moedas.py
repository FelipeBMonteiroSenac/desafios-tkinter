import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Conversor de Moedas")

def converter_real_para_dolar():
    moeda_origem = entry_moeda_origem.get()
    if moeda_origem:
        try:
            valor_real = float(moeda_origem)
            valor_dolar = valor_real / 5.0
            label_moeda_destino.config(text=f"{valor_dolar:.2f} USD")
        except ValueError:
            label_moeda_destino.config(text="Valor inválido. Digite um número.")
    else:
        label_moeda_destino.config(text="Digite um valor para converter.")

def converter_real_para_euro():
    moeda_origem = entry_moeda_origem.get()
    if moeda_origem:
        try:
            valor_real = float(moeda_origem)
            valor_euro = valor_real / 6.0
            label_moeda_destino.config(text=f"{valor_euro:.2f} EUR")
        except ValueError:
            label_moeda_destino.config(text="Valor inválido. Digite um número.")
    else:
        label_moeda_destino.config(text="Digite um valor para converter.")

def converter_dolar_para_real():
    moeda_origem = entry_moeda_origem.get()
    if moeda_origem:
        try:
            valor_dolar = float(moeda_origem)
            valor_real = valor_dolar * 5.0
            label_moeda_destino.config(text=f"{valor_real:.2f} BRL")
        except ValueError:
            label_moeda_destino.config(text="Valor inválido. Digite um número.")
    else:
        label_moeda_destino.config(text="Digite um valor para converter.")

def converter_dolar_para_euro():
    moeda_origem = entry_moeda_origem.get()
    if moeda_origem:
        try:
            valor_dolar = float(moeda_origem)
            valor_euro = valor_dolar * 0.85
            label_moeda_destino.config(text=f"{valor_euro:.2f} EUR")
        except ValueError:
            label_moeda_destino.config(text="Valor inválido. Digite um número.")
    else:
        label_moeda_destino.config(text="Digite um valor para converter.")

def converter_euro_para_real():
    moeda_origem = entry_moeda_origem.get()
    if moeda_origem:
        try:
            valor_euro = float(moeda_origem)
            valor_real = valor_euro * 6.0
            label_moeda_destino.config(text=f"{valor_real:.2f} BRL")
        except ValueError:
            label_moeda_destino.config(text="Valor inválido. Digite um número.")
    else:
        label_moeda_destino.config(text="Digite um valor para converter.")

def converter_euro_para_dolar():    
    moeda_origem = entry_moeda_origem.get()
    if moeda_origem:
        try:
            valor_euro = float(moeda_origem)
            valor_dolar = valor_euro * 1.18
            label_moeda_destino.config(text=f"{valor_dolar:.2f} USD")
        except ValueError:
            label_moeda_destino.config(text="Valor inválido. Digite um número.")
    else:
        label_moeda_destino.config(text="Digite um valor para converter.")


menubar = tk.Menu(root)

menu_real = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Real", menu=menu_real)
menu_real.add_command(label="Converter para Dólar", command=lambda: button_converter.config(command=converter_real_para_dolar))
menu_real.add_command(label="Converter para Euro", command=lambda: button_converter.config(command=converter_real_para_euro))

menu_dolar = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Dólar", menu=menu_dolar)
menu_dolar.add_command(label="Converter para Real", command=lambda: button_converter.config(command=converter_dolar_para_real))
menu_dolar.add_command(label="Converter para Euro", command=lambda: button_converter.config(command=converter_dolar_para_euro))

menu_euro = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Euro", menu=menu_euro)
menu_euro.add_command(label="Converter para Real", command=lambda: button_converter.config(command=converter_euro_para_real))
menu_euro.add_command(label="Converter para Dólar", command=lambda: button_converter.config(command=converter_euro_para_dolar))

frame_principal = tk.Frame(root, bg="lightblue")
frame_principal.place(relheight=0.9, relwidth=0.9, relx=0.5, rely=0.5, anchor="center")
label_titulo = tk.Label(frame_principal, text="Conversor de Moedas", font=("Helvetica", 24), bg="lightblue")
label_titulo.pack(pady=30)

label_moeda_origem = tk.Label(frame_principal, text="Moeda de Origem:", font=("Helvetica", 14), bg="lightblue")
label_moeda_origem.place(relx=0.3, rely=0.3, anchor="center")
entry_moeda_origem = tk.Entry(frame_principal, font=("Helvetica", 14))
entry_moeda_origem.place(relx=0.7, rely=0.3, anchor="center")
label_moeda_destino = tk.Label(frame_principal, text="Moeda de Destino:", font=("Helvetica", 14), bg="lightblue")
label_moeda_destino.place(relx=0.3, rely=0.5, anchor="center")
label_moeda_destino = tk.Label(frame_principal, font=("Helvetica", 14), width=20, bg="white", relief="sunken")
label_moeda_destino.place(relx=0.7, rely=0.5, anchor="center")
button_converter = tk.Button(frame_principal, text="Converter", font=("Helvetica", 14), bg="green", fg="white", command=None)
button_converter.place(relx=0.5, rely=0.7, anchor="center")

root.config(menu=menubar)
root.mainloop()

import tkinter as tk
janela = tk.Tk()
janela.title("Olá, Mundo!")
janela.geometry("250x100")
frame = tk.Frame(janela, bg="lightblue", width=250, height=100)
frame.place(x=0, y=0)
label = tk.Label(frame, text="Olá, Mundo!", bg="lightblue")
label.place(relx=0.35, rely=0)
janela.mainloop()
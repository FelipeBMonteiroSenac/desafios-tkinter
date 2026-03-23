import tkinter as tk

def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        checkbutton_tarefa = tk.Checkbutton(frame_to_do, text=tarefa, font=("Helvetica", 14), bg="lightyellow", height=2, width=20, anchor="w")
        checkbutton_tarefa.pack(pady=5)
        entry_tarefa.delete(0, tk.END)

root = tk.Tk()
root.geometry("800x600")
root.title("To-Do List")
frame_principal = tk.Frame(root, bg="lightyellow")
frame_principal.place(relheight=0.9, relwidth=0.9, relx=0.5, rely=0.5, anchor="center")
label_titulo = tk.Label(frame_principal, text="To-Do List", font=("Helvetica", 24), bg="lightyellow")
label_titulo.pack(pady=30)
entry_tarefa = tk.Entry(frame_principal, font=("Helvetica", 14))
entry_tarefa.pack(pady=10)
button_adicionar = tk.Button(frame_principal, text="Adicionar Tarefa", font=("Helvetica", 14), bg="lightblue", fg="black", command=adicionar_tarefa)
button_adicionar.pack(pady=10)
frame_to_do = tk.Frame(frame_principal, bg="lightyellow")
frame_to_do.pack(pady=20, padx=40, fill="both", expand=True)

root.mainloop()

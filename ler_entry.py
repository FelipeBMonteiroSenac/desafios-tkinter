import tkinter as tk

def submit():
    email = entry_email.get()
    senha = entry_senha.get()
    label_resultado_email.config(text=f"Email: {email}")
    label_resultado_senha.config(text=f"Senha: {senha}")

root = tk.Tk()
root.geometry("600x400")
root.title("Ler Entry")

frame_superior = tk.Frame(root, bg="lightgreen")
frame_superior.place(relheight=0.45, relwidth=0.9, relx=0.5, rely=0.1, anchor="n")
label_email = tk.Label(frame_superior, text="Digite seu email:", font=("Helvetica", 14), bg="lightgreen")
label_email.place(relx=0.35, rely=0.3, anchor="e")
entry_email = tk.Entry(frame_superior, font=("Helvetica", 14))
entry_email.place(relwidth=0.5, relx=0.45, rely=0.3, anchor="w")
label_senha = tk.Label(frame_superior, text="Digite sua senha:", font=("Helvetica", 14), bg="lightgreen")
label_senha.place(relx=0.35, rely=0.5, anchor="e")
entry_senha = tk.Entry(frame_superior, font=("Helvetica", 14), show="*")
entry_senha.place(relwidth=0.5, relx=0.45, rely=0.5, anchor="w")
button_submit = tk.Button(frame_superior, text="Submit", font=("Helvetica", 14), bg="green", fg="white", command=submit)
button_submit.place(relwidth=0.5, relx=0.5, rely=0.8, anchor="center")

frame_inferior = tk.Frame(root, bg="lightgreen")
frame_inferior.place(relheight=0.35, relwidth=0.9, relx=0.5, rely=0.6, anchor="n")
label_resultado_email = tk.Label(frame_inferior, text="", font=("Helvetica", 14), bg="lightgreen")
label_resultado_email.place(relx=0.5, rely=0.3, anchor="center")
label_resultado_senha = tk.Label(frame_inferior, text="", font=("Helvetica", 14), bg="lightgreen")
label_resultado_senha.place(relx=0.5, rely=0.7, anchor="center")


root.mainloop()

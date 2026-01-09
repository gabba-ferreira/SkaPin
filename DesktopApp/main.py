import tkinter as tk
from tkinter import messagebox, filedialog


# Interface
window = tk.Tk()
window.title("SkaPin")
window.geometry("740x440")
window.configure(bg='#333333')

# Labels 
title = tk.Label(window, text="SkaPin", bg='#333333', fg="#FFFFFF")
title.pack()

server_label = tk.Label(window, text="Endereço do Servidor")
server_input = tk.Entry(window)


window.mainloop()
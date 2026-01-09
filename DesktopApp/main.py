import tkinter as tk
from tkinter import messagebox, filedialog


# Interface
window = tk.Tk()
window.title("SkaPin")
window.geometry("740x440")
#window.configure(bg='#333333')

#Variaveis
rede_selecionada = tk.StringVar(value="wireless")

# Labels 
title = tk.Label(window, text="SkaPin", bg='#333333', fg="#FFFFFF")


urlServer_label = tk.Label(window, text="Url do Servidor")
urlServer_input = tk.Entry(window)

tagColetor_label = tk.Label(window, text="Tag do Coletor")
urlServer_input = tk.Entry(window)

tipoRede_label = tk.Label(window, text="Tipo de Rede" )

rb_wireless = tk.Radiobutton(window, text="Wireless", variable=rede_selecionada, value="wireless",  width=10)
rb_wireless.grid(row=2, column=1, padx=5)

rb_ethernet = tk.Radiobutton(window, text="Ethernet", variable=rede_selecionada, value="ethernet", width=10)
rb_ethernet.grid(row=2, column=2, padx=5)

dhcp = tk.Radiobutton(window, text="DHCP", width=10)
dhcp.grid(row=2, column=3, padx=5)

ipAddress_label = tk.Label(window, text="Endereço de IP")
ipAddress_input = tk.Entry(window)

mascRede_label = tk.Label(window, text="Mascara de rede")
mascRede_input = tk.Entry(window)

gateway_label = tk.Label(window, text="Gateway")
gateway_input = tk.Entry(window)


# --- FUNÇÃO PARA TESTAR ---
def salvar():
    print(f"Rede: {rede_selecionada.get()}")

btn_salvar = tk.Button(window, text="Salvar Configurações", command=salvar, bg="#e1e1e1")
btn_salvar.grid(row=3, column=0, columnspan=3, pady=20)

window.mainloop()
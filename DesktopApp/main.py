import tkinter as tk
from tkinter import messagebox, filedialog


# Interface
window = tk.Tk()
window.title("SkaPin")
window.geometry("740x440")
#window.configure(bg='#333333')

#Variaveis
rede_selecionada = tk.StringVar(value="wireless")
estado_dhcp = tk.IntVar(value=1)

# --- FUNÇÕES ---
def dchpAtivado():
    if estado_dhcp.get() == 0:
        ipAddress_label.grid(row=6, column=0, pady=20)
        ipAddress_input.grid(row=7, column=0)
        
        mascRede_label.grid(row=6, column=1)
        mascRede_input.grid(row=7, column=1)

        gateway_label.grid(row=6, column=2)
        gateway_input.grid(row=7, column=2)


    else:
        ipAddress_label.grid_forget()
        ipAddress_input.grid_forget()
        mascRede_label.grid_forget()
        mascRede_input.grid_forget()
        gateway_label.grid_forget()
        gateway_input.grid_forget()

# Labels 
title = tk.Label(window, text="SkaPin", font=("Arial", 16, "bold") )

urlServer_label = tk.Label(window, text="Url do Servidor")
urlServer_input = tk.Entry(window)

tagColetor_label = tk.Label(window, text="Tag do Coletor")
tagColetor_input = tk.Entry(window)

tipoRede_label = tk.Label(window, text="Tipo de Rede" )
rb_wireless = tk.Radiobutton(window, text="Wireless", variable=rede_selecionada, value="wireless",  width=10)

rb_ethernet = tk.Radiobutton(window, text="Ethernet", variable=rede_selecionada, value="ethernet", width=10)

dhcp = tk.Checkbutton(window, text="DHCP", width=10, variable=estado_dhcp, command=dchpAtivado)


nomeRede_label = tk.Label(window, text="Nome da Rede")
nomeRede_input = tk.Entry(window)

senhaRede_label = tk.Label(window, text="Senha da Rede")
senhaRede_input = tk.Entry(window)

ipAddress_label = tk.Label(window, text="Endereço de IP")
ipAddress_input = tk.Entry(window)

mascRede_label = tk.Label(window, text="Mascara de rede")
mascRede_input = tk.Entry(window)

gateway_label = tk.Label(window, text="Gateway")
gateway_input = tk.Entry(window)

btn_SavePendrive = tk.Button(window, text="Salvar no Pendrive")

# Grid
title.grid(row=0, column=1)

urlServer_label.grid(row=1, column=0, padx=70, pady=20)
urlServer_input.grid(row=2, column=0)

tagColetor_label.grid(row=1, column=1, padx=60)
tagColetor_input.grid(row=2, column=1)

tipoRede_label.grid(row=1, column=2, padx=40) 
rb_wireless.grid(row=2, column=2)
rb_ethernet.grid(row=2, column=3)

dhcp.grid(row=4, column=0)

nomeRede_label.grid(row=3, column=1, pady=20)
nomeRede_input.grid(row=4, column=1)

senhaRede_label.grid(row=3, column=2)
senhaRede_input.grid(row=4, column=2)

btn_SavePendrive.grid(row=8, column=1, pady=80)

window.mainloop()
import tkinter as tk
from tkinter import messagebox, filedialog


# Interface
window = tk.Tk()
window.title("SkaPin")
window.geometry("740x440")
#window.configure(bg='#333333')

#Variaveis
rede_selecionada = tk.StringVar(value="wireless")
estado_dhcp = tk.IntVar()


# --- FUNÇÕES ---
def dchpAtivado():
    if estado_dhcp.get() == 0:
        ipAddress_label.grid(row=6, column=0, pady=10)
        ipAddress_input.grid(row=7, column=0)
        
        mascRede_label.grid(row=6, column=2, pady=10)
        mascRede_input.grid(row=7, column=2, pady=10)

        gateway_label.grid(row=6, column=4, pady=10)
        gateway_input.grid(row=7, column=4, pady=10)


    else:
        ipAddress_label.grid_forget()
        ipAddress_input.grid_forget()
        mascRede_label.grid_forget()
        mascRede_input.grid_forget()
        gateway_label.grid_forget()
        gateway_input.grid_forget()

# Labels 
title = tk.Label(window, text="SkaPin", font=("Arial", 16, "bold") )
title.grid(row=0, column=3)

urlServer_label = tk.Label(window, text="Url do Servidor")
urlServer_input = tk.Entry(window)
urlServer_label.grid(row=1, column=0, pady=10)
urlServer_input.grid(row=2, column=0, padx=20)

tagColetor_label = tk.Label(window, text="Tag do Coletor")
tagColetor_input = tk.Entry(window)
tagColetor_label.grid(row=1, column=2, pady=10)
tagColetor_input.grid(row=2, column=2, padx=25)

tipoRede_label = tk.Label(window, text="Tipo de Rede" )
tipoRede_label.grid(row=1, column=5, padx=0) 
rb_wireless = tk.Radiobutton(window, text="Wireless", variable=rede_selecionada, value="wireless",  width=10)
rb_wireless.grid(row=2, column=4, padx=0)
rb_ethernet = tk.Radiobutton(window, text="Ethernet", variable=rede_selecionada, value="ethernet", width=10)
rb_ethernet.grid(row=2, column=6, padx=0)

dhcp = tk.Checkbutton(window, text="DHCP", width=10, variable=estado_dhcp, command=dchpAtivado)
dhcp.grid(row=4, column=0, pady=50, padx=2)

ipAddress_label = tk.Label(window, text="Endereço de IP")
ipAddress_input = tk.Entry(window)

mascRede_label = tk.Label(window, text="Mascara de rede")
mascRede_input = tk.Entry(window)

gateway_label = tk.Label(window, text="Gateway")
gateway_input = tk.Entry(window)




window.mainloop()
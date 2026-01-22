import os
from config_writer import write_config

def process_configuration(data: dict, pendrive_path: str):
    if not pendrive_path or not os.path.isdir(pendrive_path):
        raise ValueError("Pendrive inválido ou não selecionado")

    return write_config(pendrive_path,data)


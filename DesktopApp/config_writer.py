import json 
import os

def write_config(pendrive_path: str, data: dict):
    file_path = os.path.join(pendrive_path,"config.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        

    return file_path
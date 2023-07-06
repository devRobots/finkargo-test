"""
Módulo con funciones para la carga de archivos
"""
import json

def load_json_data(file_name):
    """
    Carga los datos de prueba desde un archivo JSON
    """
    file_path = f"tests/json/{file_name}.json"
    with open(file_path, "r", encoding='utf-8') as file:
        return json.load(file)

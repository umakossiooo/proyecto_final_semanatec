import os
import sys
import zipfile
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(data)
        with open(os.path.splitext(file_path)[0], 'wb') as f:
            f.write(decrypted_data)
        os.remove(file_path)
        print(f"Archivo {file_path} desencriptado con éxito.")
    except Exception as e:
        print(f"Error al desencriptar el archivo {file_path}: {str(e)}")

def decrypt_folder(folder_path, key):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
        print("Todos los archivos en la carpeta han sido desencriptados.")
    except Exception as e:
        print(f"Error al desencriptar la carpeta {folder_path}: {str(e)}")

def unzip_file(zip_path, extract_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Archivo {zip_path} descomprimido con éxito en {extract_path}.")
    except Exception as e:
        print(f"Error al descomprimir el archivo {zip_path}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python encriptado.py <archivo_zip>")
        sys.exit(1)

    zip_path = sys.argv[1]
    if not os.path.isfile(zip_path):
        print("El archivo especificado no existe.")
        sys.exit(1)

    key = input("Ingrese la clave de desencriptación: ")

    extract_path = os.path.splitext(zip_path)[0]
    unzip_file(zip_path, extract_path)
    decrypt_folder(extract_path, key)

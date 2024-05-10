import os
import sys
import pyzipper
import time

def desencriptar_carpeta(carpeta_comprimida, password, directorio_destino):
    try:
        archivos_descomprimidos = False
        for archivo_zip in os.listdir(carpeta_comprimida):
            if archivo_zip.endswith('.zip'):
                ruta_completa = os.path.join(carpeta_comprimida, archivo_zip)
                try:
                    with pyzipper.AESZipFile(ruta_completa) as zfile:
                        zfile.setpassword(password.encode())
                        zfile.extractall(directorio_destino)
                    print(f"Archivos descomprimidos correctamente desde: {ruta_completa}")
                    archivos_descomprimidos = True
                except RuntimeError:
                    print(f"Contraseña incorrecta para el archivo: {ruta_completa}")

                # Esperar un segundo para asegurar que el archivo esté completamente cerrado antes de eliminarlo
                time.sleep(1)

                # Eliminar el archivo comprimido original solo si se descomprimió correctamente
                if archivos_descomprimidos:
                    os.remove(ruta_completa)
                    print(f"Archivo comprimido original eliminado: {ruta_completa}")

        if archivos_descomprimidos:
            print(f"Todos los archivos han sido descomprimidos en: {directorio_destino}")
        else:
            print("No se encontraron archivos ZIP válidos para descomprimir.")
    except Exception as e:
        print(f"Error al descomprimir archivos: {str(e)}")

def main():
    if len(sys.argv) != 4:
        print("Uso: python descomprimir.py <carpeta_comprimida> <contraseña> <directorio_destino>")
        sys.exit(1)

    carpeta_comprimida = sys.argv[1]
    password = sys.argv[2]
    directorio_destino = sys.argv[3]

    if not os.path.isdir(carpeta_comprimida):
        print(f"{carpeta_comprimida} no es una carpeta válida.")
        sys.exit(1)

    if not os.path.isdir(directorio_destino):
        print(f"{directorio_destino} no es un directorio válido.")
        sys.exit(1)

    # Descomprimir archivos ZIP protegidos con contraseña en la carpeta especificada
    desencriptar_carpeta(carpeta_comprimida, password, directorio_destino)

if __name__ == "__main__":
    main()

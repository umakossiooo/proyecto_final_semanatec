
import os
import platform
import psutil  # Asegúrate de tener instalado este paquete usando pip

# Obtener la ruta del directorio padre del directorio actual
ruta_padre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Nombre de la carpeta
nombre_carpeta = "info_sistema"

# Combinar la ruta del directorio padre con el nombre de la carpeta
carpeta = os.path.join(ruta_padre, nombre_carpeta)

# Asegúrate de que la carpeta exista o créala si no existe
os.makedirs(carpeta, exist_ok=True)

# Lista de funciones para obtener información del sistema
funciones_info_sistema = [
    platform.system,
    platform.processor,
    platform.release,
    platform.machine,
    platform.version,
    platform.node,
    platform.python_version,
    lambda: f"{psutil.cpu_percent(interval=1)}%",  # Uso de la CPU
    lambda: f"{psutil.virtual_memory().available / (1024.0 ** 3):.2f} GB",  # Memoria RAM disponible
    lambda: f"{psutil.disk_usage('/').free / (1024.0 ** 3):.2f} GB",  # Espacio en disco disponible
]

# Lista de etiquetas para cada tipo de información
etiquetas = [
    "Sistema Operativo",
    "Procesador",
    "Versión del Kernel",
    "Arquitectura",
    "Versión del SO",
    "Nombre del equipo",
    "Versión de Python",
    "Uso de la CPU",
    "Memoria RAM Disponible",
    "Espacio en Disco disponible",
]

# Generar información del sistema en archivos TXT
for i in range(len(funciones_info_sistema)):
    nombre_archivo = f"{carpeta}/info_sistema_{i+1}.txt"
    funcion_info = funciones_info_sistema[i]
    etiqueta = etiquetas[i]
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Información del sistema - Archivo {i+1}:\n")
        archivo.write(f"{etiqueta}: {funcion_info()}\n")
        archivo.write("\n¡Fin de la información!\n")

print("Se han creado 10 archivos con información del sistema en la carpeta 'info_sistema'.")



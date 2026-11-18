
import os
from analizadores.sintactico import analizar_archivo


programas = [
    "programa1_correcto.biblio",
    "programa2_correcto.biblio",
    "programa3_correcto.biblio",
    "programa4_error_lexico.biblio",
    "programa5_error_sintactico.biblio",
    "programa6_error_semantico.biblio"
]

# Crear la carpeta de resultados si no existe
os.makedirs("resultados", exist_ok=True)

print("=== PRUEBAS DEL COMPILADOR BIBLIOCODE ===")

for numero, nombre in enumerate(programas, start=1):
    ruta = os.path.join("programas", nombre)

    try:
        resultado = analizar_archivo(ruta)
    except OSError as error:
        resultado = f"ERROR AL LEER {ruta}: {error}"

    # Guardar cada prueba en su archivo
    salida = os.path.join("resultados", f"prueba{numero}.txt")

    with open(salida, "w", encoding="utf-8") as archivo:
        archivo.write(resultado + "\n")

    print(f"\nPRUEBA {numero}")
    print(resultado)
    print(f"Resultado guardado en: {salida}")

print("\n=== PRUEBAS FINALIZADAS ===")

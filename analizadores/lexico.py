
import re

reservadas = {
    "variable", "si", "entonces", "sino", "fin",
    "ciclo", "veces", "mientras", "leer", "imprimir",
    "registrar", "prestar", "devolver", "consultar",
    "mostrar", "eliminar", "verdadero", "falso",
    "y", "o", "no"
}

patron = re.compile(
    r"==|\d+\.\d+|\d+|[^\W\d]\w*|_[\w]*|[=+\-*();,<>]"
)


def clasificar(palabra):
    if palabra.lower() in reservadas:
        return "RESERVADA"
    elif palabra.isdigit():
        return "ENTERO"
    elif re.fullmatch(r"\d+\.\d+", palabra):
        return "DECIMAL"
    elif palabra.isidentifier():
        return "IDENTIFICADOR"
    else:
        return "SIMBOLO"


def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


def analizar(texto):
    tokens = []
    errores = []

    for numero_linea, linea in enumerate(texto.splitlines(), 1):
        posicion = 0

        while posicion < len(linea):
            caracter = linea[posicion]
            columna = posicion + 1

            # Ignorar espacios
            if caracter.isspace():
                posicion += 1
                continue

            # Ignorar comentarios
            if caracter == "#":
                break

            # Reconocer cadenas
            if caracter in ("'", '"'):
                inicio = posicion
                posicion += 1

                while posicion < len(linea) and linea[posicion] != caracter:
                    posicion += 1

                if posicion >= len(linea):
                    errores.append(
                        f"Cadena sin cerrar en línea {numero_linea}, columna {columna}"
                    )
                    continue

                posicion += 1
                valor = linea[inicio:posicion]
                tipo = "CADENA"

            else:
                encontrado = patron.match(linea, posicion)

                if encontrado is None:
                    errores.append(
                        f"Carácter desconocido '{caracter}' "
                        f"en línea {numero_linea}, columna {columna}"
                    )
                    posicion += 1
                    continue

                valor = encontrado.group()
                tipo = clasificar(valor)
                posicion = encontrado.end()

            # Guardar el token para el analizador sintáctico
            tokens.append({
                "tipo": tipo,
                "valor": valor,
                "linea": numero_linea,
                "columna": columna
            })

    return tokens, errores


# Esta parte solo se ejecuta al abrir lexico.py directamente
if __name__ == "__main__":
    ruta = "programas/programa1_correcto.biblio"

    codigo = leer_archivo(ruta)
    tokens, errores = analizar(codigo)

    print("=== ANÁLISIS LÉXICO ===")
    print("Archivo:", ruta)

    for token in tokens:
        print(
            f"{token['tipo']}: {token['valor']} "
            f"(Línea {token['linea']}, columna {token['columna']})"
        )

    print("\n=== RESULTADOS ===")

    if errores:
        for error in errores:
            print("ERROR LÉXICO:", error)
    else:
        print("No se encontraron errores léxicos.")

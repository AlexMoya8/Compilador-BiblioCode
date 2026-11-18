
try:
    from .lexico import analizar, leer_archivo
except ImportError:
    from lexico import analizar, leer_archivo

FUNCIONES = {
    "imprimir", "leer", "registrar", "prestar",
    "devolver", "consultar", "mostrar", "eliminar"
}


def analizar_sintaxis(tokens):
    posicion = 0
    errores = []

    def actual():
        if posicion < len(tokens):
            return tokens[posicion]
        return None

    def valor():
        token = actual()
        return token["valor"].lower() if token else None

    def aceptar(esperado):
        nonlocal posicion
        if valor() == esperado:
            posicion += 1
            return True
        return False

    def error(mensaje):
        token = actual()
        if token:
            lugar = f"línea {token['linea']}, columna {token['columna']}"
        elif tokens:
            ultimo = tokens[-1]
            lugar = f"después de la línea {ultimo['linea']}"
        else:
            lugar = "archivo vacío"
        raise SyntaxError(f"{mensaje}, {lugar}")

    def esperar(esperado):
        if not aceptar(esperado):
            error(f"Se esperaba '{esperado}'")

    def identificador():
        nonlocal posicion
        token = actual()
        if token and token["tipo"] == "IDENTIFICADOR":
            posicion += 1
        else:
            error("Se esperaba un identificador")

    # Expresiones: números, textos, variables y paréntesis
    def primario():
        nonlocal posicion
        token = actual()

        if aceptar("("):
            expresion()
            esperar(")")
        elif token and (
            token["tipo"] in ("IDENTIFICADOR", "ENTERO", "DECIMAL", "NUMERO", "CADENA")
            or valor() in ("verdadero", "falso")
        ):
            posicion += 1
        else:
            error("Se esperaba una expresión")

    def unario():
        if valor() in ("-", "no"):
            aceptar(valor())
            unario()
        else:
            primario()

    def producto():
        unario()
        while valor() == "*":
            aceptar("*")
            unario()

    def suma():
        producto()
        while valor() in ("+", "-"):
            aceptar(valor())
            producto()

    def comparacion():
        suma()
        if valor() in ("==", ">", "<"):
            aceptar(valor())
            suma()

    def expresion():
        comparacion()
        while valor() in ("y", "o"):
            aceptar(valor())
            comparacion()

    # Declaración: variable nombre = expresión;
    def declaracion():
        esperar("variable")
        identificador()
        esperar("=")
        expresion()
        esperar(";")

    # Asignación: nombre = expresión;
    def asignacion():
        identificador()
        esperar("=")
        expresion()
        esperar(";")

    # Llamadas: imprimir(...); registrar(...); etc.
    def llamada():
        nonlocal posicion

        if valor() not in FUNCIONES:
            error("Función no reconocida")

        posicion += 1
        esperar("(")

        if valor() != ")":
            while True:
                # Argumento con nombre: titulo = "Libro"
                token = actual()
                siguiente = (
                    tokens[posicion + 1]["valor"]
                    if posicion + 1 < len(tokens) else None
                )

                if token and token["tipo"] == "IDENTIFICADOR" and siguiente == "=":
                    identificador()
                    esperar("=")

                expresion()

                if not aceptar(","):
                    break

        esperar(")")
        esperar(";")

    # Procesar instrucciones hasta encontrar un cierre
    def bloque(cierres):
        while actual() is not None and valor() not in cierres:
            instruccion()

    # Condicional: si ... entonces ... sino ... fin
    def condicional():
        esperar("si")
        expresion()
        esperar("entonces")

        bloque({"sino", "fin"})

        if aceptar("sino"):
            bloque({"fin"})

        esperar("fin")

    # Ciclo: ciclo N veces / ciclo mientras condición
    def ciclo():
        esperar("ciclo")

        if aceptar("mientras"):
            expresion()
        else:
            expresion()
            esperar("veces")

        bloque({"fin"})
        esperar("fin")

    def instruccion():
        if valor() == "variable":
            declaracion()
        elif valor() == "si":
            condicional()
        elif valor() == "ciclo":
            ciclo()
        elif valor() in FUNCIONES:
            llamada()
        elif actual() and actual()["tipo"] == "IDENTIFICADOR":
            asignacion()
        else:
            error("Instrucción no válida")

    try:
        bloque(set())
    except SyntaxError as problema:
        errores.append(str(problema))

    return errores


def analizar_archivo(ruta):
    codigo = leer_archivo(ruta)
    tokens, errores_lexicos = analizar(codigo)

    resultado = [f"Archivo: {ruta}"]

    if errores_lexicos:
        for error in errores_lexicos:
            resultado.append(f"ERROR LÉXICO: {error}")
    else:
        errores_sintacticos = analizar_sintaxis(tokens)

        if errores_sintacticos:
            for error in errores_sintacticos:
                resultado.append(f"ERROR SINTÁCTICO: {error}")
        else:
            resultado.append("Análisis sintáctico correcto.")

    return "\n".join(resultado)


if __name__ == "__main__":
    ruta = "programas/programa5_error_sintactico.biblio"
    print("=== ANÁLISIS SINTÁCTICO ===")
    print(analizar_archivo(ruta))

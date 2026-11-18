# BiblioCode — Compilador para la gestión de bibliotecas

## 1. Descripción del proyecto

**BiblioCode** es un lenguaje de programación educativo orientado a la gestión de bibliotecas, desarrollado como parte de la asignatura de Compiladores de la Fundación Universitaria Uniclaretiana.

El proyecto busca aplicar los conceptos de análisis léxico y sintáctico mediante la construcción de un compilador básico en Python.

BiblioCode permite escribir instrucciones para declarar variables, realizar operaciones matemáticas, utilizar condicionales, ejecutar ciclos y representar operaciones de biblioteca, como registrar, consultar, prestar, devolver y eliminar libros.

## 2. Integrantes

- Alex David Moya Bejarano
- Alex David García Chala
- Jilmar Juel Moreno Córdoba

## 3. Tecnologías utilizadas

- **Python 3:** desarrollo de los analizadores.
- **Expresiones regulares (`re`):** reconocimiento de tokens.
- **Gramática EBNF:** definición de las reglas sintácticas del lenguaje.
- **Visual Studio Code:** edición y ejecución del proyecto.
- **Git y GitHub:** control de versiones y trabajo colaborativo.

El proyecto utiliza módulos de la biblioteca estándar de Python, sin requerir dependencias externas para los analizadores actuales.

## 4. Estructura del proyecto

```text
Compilador-BiblioCode/
│
├── analizadores/
│   ├── lexico.py
│   └── sintactico.py
│
├── gramatica/
│   └── gramatica.ebnf
│
├── programas/
│   ├── programa1_correcto.biblio
│   ├── programa2_correcto.biblio
│   ├── programa3_correcto.biblio
│   ├── programa4_error_lexico.biblio
│   ├── programa5_error_sintactico.biblio
│   └── programa6_error_semantico.biblio
│
├── resultados/
│   ├── prueba1.txt
│   ├── prueba2.txt
│   ├── prueba3.txt
│   ├── prueba4.txt
│   ├── prueba5.txt
│   └── prueba6.txt
│
├── main.py
├── README.md
└── BITACORA.md
```

La bitácora actualizada del proyecto también se mantiene en un documento Word independiente.

## 5. Características del lenguaje

BiblioCode incluye las siguientes estructuras:

| Característica | Ejemplo |
|---|---|
| Declaración de variables | `variable cantidad = 5;` |
| Asignación | `cantidad = cantidad + 1;` |
| Operaciones matemáticas | `variable total = (4 + 2) * 3;` |
| Condicionales | `si cantidad > 0 entonces ... fin` |
| Ciclos definidos | `ciclo 3 veces ... fin` |
| Ciclos condicionales | `ciclo mientras cantidad > 0 ... fin` |
| Impresión | `imprimir("Hola");` |
| Operaciones de biblioteca | `mostrar();` |

Las instrucciones simples terminan en punto y coma (`;`). Los bloques de control utilizan palabras como `entonces`, `sino` y `fin`.

## 6. Analizador léxico

El analizador léxico se encuentra en `analizadores/lexico.py`.

Su función es leer el código fuente e identificar los componentes del lenguaje, denominados *tokens*.

Reconoce palabras reservadas, identificadores, números enteros y decimales, cadenas de texto, operadores y símbolos.

También ignora espacios y comentarios que comienzan con `#`.

Cuando encuentra un carácter no reconocido, genera un error léxico que indica su ubicación.

## 7. Analizador sintáctico

El analizador sintáctico se encuentra en `analizadores/sintactico.py`.

Recibe los tokens del analizador léxico y comprueba que las instrucciones respeten las reglas de la gramática.

La implementación utiliza funciones de análisis descendente recursivo para reconocer:

- Declaraciones y asignaciones.
- Expresiones matemáticas y lógicas.
- Condicionales `si`, `entonces`, `sino` y `fin`.
- Ciclos `ciclo ... veces` y `ciclo mientras`.
- Llamadas a las operaciones de biblioteca.
- Uso de paréntesis, argumentos y puntos y coma.

Cuando encuentra una instrucción inválida, informa el primer error sintáctico detectado, incluyendo su ubicación.

## 8. Requisitos

- Python 3.10 o superior.
- Una terminal para ejecutar comandos.
- Visual Studio Code u otro editor de código.

## 9. Instalación y ejecución

### Clonar el repositorio

```bash
git clone https://github.com/AlexMoya8/Compilador-BiblioCode.git
```

Ingresar a la carpeta:

```bash
cd Compilador-BiblioCode
```

### Ejecutar todas las pruebas

```bash
python main.py
```

Este comando analiza los seis programas de prueba y guarda automáticamente los resultados en archivos de texto dentro de la carpeta `resultados/`.

### Ejecutar únicamente el analizador léxico

```bash
python analizadores/lexico.py
```

### Ejecutar únicamente el analizador sintáctico

```bash
python analizadores/sintactico.py
```

Las ejecuciones individuales utilizan el archivo configurado en el bloque principal de cada analizador.

## 10. Programas de prueba

Se prepararon seis programas para comprobar las distintas características del lenguaje y los errores previstos.

| Programa | Objetivo | Resultado esperado |
|---|---|---|
| Programa 1 | Variables y operaciones matemáticas | Sintaxis correcta |
| Programa 2 | Condicionales y ciclos anidados | Sintaxis correcta |
| Programa 3 | Operaciones de biblioteca | Sintaxis correcta |
| Programa 4 | Carácter inválido `@` | Error léxico |
| Programa 5 | Falta de punto y coma | Error sintáctico |
| Programa 6 | Incompatibilidad de tipos | Sintaxis correcta; error semántico pendiente de una fase posterior |

Los seis archivos de resultados se generan mediante `main.py`. Su creación no sustituye la revisión de su contenido para confirmar que coincidan con los resultados esperados.

## 11. Resultados de las pruebas

Cada ejecución genera un archivo independiente:

```text
resultados/prueba1.txt
resultados/prueba2.txt
resultados/prueba3.txt
resultados/prueba4.txt
resultados/prueba5.txt
resultados/prueba6.txt
```

Se verificó que el programa 5 detecta la ausencia del punto y coma después de `imprimir`, en la línea 4, columna 43.

Los demás resultados deben revisarse después de ejecutar la versión final de `main.py`.

## 12. Alcance y limitaciones

La implementación actual corresponde a las fases de análisis léxico y sintáctico.

El proyecto todavía no ejecuta las operaciones de biblioteca ni realiza una comprobación semántica completa de los tipos de datos, variables y demás reglas del lenguaje.

Por tanto, un programa puede ser léxica y sintácticamente válido aunque contenga errores semánticos.

## 13. Control de versiones

El código fuente se administra mediante Git y GitHub para conservar los cambios realizados durante el desarrollo y facilitar el trabajo colaborativo.

**Repositorio:** https://github.com/AlexMoya8/Compilador-BiblioCode

## 14. Registro del desarrollo

El equipo mantiene una bitácora en Word en la que documenta las decisiones, los avances, los problemas encontrados, las correcciones y el uso de herramientas de inteligencia artificial durante el proyecto.

---

**Proyecto académico — BiblioCode | Fundación Universitaria Uniclaretiana | 2026**
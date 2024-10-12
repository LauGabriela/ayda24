#!/usr/bin/env python3

# Diccionarios básicos para transformar números en palabras
numeros_a_palabras = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciséis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa",
    100: "cien",
    200: "doscientos",
    300: "trescientos",
    400: "cuatrocientos",
    500: "quinientos",
    600: "seiscientos",
    700: "setecientos",
    800: "ochocientos",
    900: "novecientos",
}


# Función auxiliar para obtener las palabras de los números
def convertir_a_palabras(n):
    if n == 0:
        return "cero"
    elif n <= 20:
        return numeros_a_palabras[n]
    elif n < 100:
        decenas, resto = divmod(n, 10)
        if resto == 0:
            return numeros_a_palabras[decenas * 10]
        else:
            return f"{numeros_a_palabras[decenas * 10]} y {numeros_a_palabras[resto]}"
    elif n < 1000:
        centenas, resto = divmod(n, 100)
        if resto == 0:
            return numeros_a_palabras[centenas * 100]
        elif centenas == 1:
            return f"ciento {convertir_a_palabras(resto)}"
        else:
            return f"{numeros_a_palabras[centenas * 100]} {convertir_a_palabras(resto)}"
    elif n < 1000000:
        miles, resto = divmod(n, 1000)
        if resto == 0:
            return f"{convertir_a_palabras(miles)} mil"
        elif miles == 1:
            return f"mil {convertir_a_palabras(resto)}"
        else:
            return f"{convertir_a_palabras(miles)} mil {convertir_a_palabras(resto)}"
    elif n < 1000000000:
        millones, resto = divmod(n, 1000000)
        if resto == 0:
            return (
                f"{convertir_a_palabras(millones)} millón"
                if millones == 1
                else f"{convertir_a_palabras(millones)} millones"
            )
        elif resto == 1:
            return (
                "Un millon"
                if millones == 1
                else f"{convertir_a_palabras(millones)} millones"
            )
        else:
            return (
                f"{convertir_a_palabras(millones)} millón {convertir_a_palabras(resto)}"
                if millones == 1
                else f"{convertir_a_palabras(millones)} millones {convertir_a_palabras(resto)}"
            )
    elif n == 1000000000:
        return "mil millones"


# Entry point
if __name__ == "__main__":
    numero = int(input("Introduce un número: "))
    resultado = convertir_a_palabras(numero)

    print(f"El número {numero} en palabras es: {resultado}")

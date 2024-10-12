#!/usr/bin/env python3
def numero_a_letra(n: int) -> str:
    unidades = [
        "cero",
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
    ]
    diez = [
        "diez",
        "once",
        "doce",
        "trece",
        "catorce",
        "quince",
        "dieciséis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
    ]
    decenas = [
        "",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    ]
    centenas = [
        "ciento",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    ]

    if n < 10:
        return unidades[n]

    if n == 100:
        return "cien"

    if n >= 1000000:
        num_millones = n // 1000000
        resto = n - (num_millones * 1000000)

        if num_millones == 1:
            texto = "un millón"
        else:
            texto = numero_a_letra(num_millones) + " millones"

        if resto > 0:
            texto += " " + numero_a_letra(resto)

        return texto

    if n >= 1000:
        num_miles = n // 1000
        resto = n - (num_miles * 1000)

        if num_miles == 1:
            texto = "mil"
        else:
            texto = numero_a_letra(num_miles) + " mil"

        if resto > 0:
            texto += " " + numero_a_letra(resto)

        return texto

    if n < 100:
        if 10 <= n < 20:
            return diez[n - 10]
        else:
            num_decenas = n // 10
            num_unidades = n - (num_decenas * 10)

            if num_unidades > 0:
                return decenas[num_decenas - 1] + " y " + unidades[num_unidades]
            else:
                return decenas[num_decenas - 1]

    else:
        num_centenas = n // 100
        resto = n - (num_centenas * 100)

        if resto == 0:
            return centenas[num_centenas - 1]

        return centenas[num_centenas - 1] + " " + numero_a_letra(resto)


if __name__ == "__main__":
    numero = int(input("Introduce un número: "))
    letra = numero_a_letra(numero)
    print(letra)
